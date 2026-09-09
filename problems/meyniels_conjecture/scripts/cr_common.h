// cr_common.h -- shared code: graph6 parsing, multiset ranking, exact k-cop solver with staged propagation.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <omp.h>
typedef uint64_t u64; typedef uint32_t u32; typedef uint16_t u16; typedef uint8_t u8;

static int n;
static u64 cl[64];
static int nbl[64][64], nbc[64];
static u64 binom[100][20];
static void init_binom(void){ for(int a=0;a<100;a++){ binom[a][0]=1; for(int b=1;b<20;b++) binom[a][b]=(a==0)?0:binom[a-1][b-1]+binom[a-1][b]; } }
static void build_lists(void){ for(int v=0;v<n;v++){ nbc[v]=0; for(int u=0;u<n;u++) if(cl[v]>>u&1) nbl[v][nbc[v]++]=u; } }
static int parse_g6(const char*s){
  int N=s[0]-63; if(N<1||N>62) return -1; n=N; for(int i=0;i<n;i++) cl[i]=1ULL<<i;
  int bitpos=0; const char*p=s+1;
  for(int j=1;j<n;j++) for(int i=0;i<j;i++){ int byte=bitpos/6, bit=5-(bitpos%6); int v=(p[byte]-63)>>bit&1; bitpos++; if(v){ cl[i]|=1ULL<<j; cl[j]|=1ULL<<i; } }
  build_lists(); return 0;
}
static void to_g6(char*out){ // n<=62
  out[0]=(char)(n+63); int bitpos=0; int L=(n*(n-1)/2+5)/6; for(int b=0;b<L;b++) out[1+b]=63; 
  for(int j=1;j<n;j++) for(int i=0;i<j;i++){ if(cl[i]>>j&1) out[1+bitpos/6]+= (1<<(5-bitpos%6)); bitpos++; }
  out[1+L]=0;
}
static inline u64 rank_sorted(const u8*c,int k){ u64 r=0; for(int i=0;i<k;i++) r+=binom[c[i]+i][i+1]; return r; }
static inline void sort_small(u8*a,int k){ for(int i=1;i<k;i++){ u8 x=a[i]; int j=i-1; while(j>=0&&a[j]>x){a[j+1]=a[j];j--;} a[j+1]=x; } }
static inline void set_bit(u64*a,u64 i){ __atomic_fetch_or(&a[i>>6],1ULL<<(i&63),__ATOMIC_RELAXED); }
static inline int test_and_set(u64*a,u64 i){ u64 old=__atomic_fetch_or(&a[i>>6],1ULL<<(i&63),__ATOMIC_RELAXED); return (old>>(i&63))&1; }

typedef struct { int win_cf, rounds_cf, win_rf, rounds_rf; double frac_ct; double mean_ct_round; u64 M; int rounds_total; u64 nwin_place; int place[20]; int maxround_place; } result_t;

// early: 1 => stop as soon as cops (moving first after placement) are known to win.
static result_t solve_staged(int k, int verbose, int early){
  result_t res; memset(&res,0,sizeof res); res.rounds_cf=-1; res.rounds_rf=-1;
  u64 M=binom[n+k-1][k]; res.M=M;
  // all sorted tuples of size k stored by rank
  u8 *tup=malloc(M*k);
  { u8 c[20]; for(int i=0;i<k;i++) c[i]=0;
    while(1){ u64 r=rank_sorted(c,k); memcpy(tup+r*k,c,k); int i=k-1; while(i>=0&&c[i]==n-1) i--; if(i<0) break; c[i]++; for(int j=i+1;j<k;j++) c[j]=c[i]; } }
  u64 NS=M*(u64)n;
  u16 *ct=calloc(NS,2); u16 *rt=calloc(NS,2); u8 *cnt=malloc(NS);
  // intermediate levels 1..k-1: (U of size k-j, V of size j, r)
  u64 *lvl_mark[20], *lvl_done[20]; u64 lvl_cnt[20], MU[20], MV[20];
  for(int j=1;j<k;j++){ MU[j]=binom[n+k-j-1][k-j]; MV[j]=binom[n+j-1][j]; lvl_cnt[j]=MU[j]*MV[j]*(u64)n;
    lvl_mark[j]=calloc((lvl_cnt[j]+63)/64,8); lvl_done[j]=calloc((lvl_cnt[j]+63)/64,8);
    if(!lvl_mark[j]||!lvl_done[j]){ fprintf(stderr,"alloc failed level %d\n",j); exit(1);} }
  if(!ct||!rt||!cnt){ fprintf(stderr,"alloc failed\n"); exit(1); }
  // tuples for U-sizes and V-sizes: we need unranking for scanning intermediate levels. Precompute tuple tables for sizes 1..k-1.
  u8 *tabs[20]; for(int s=1;s<k;s++){ u64 Ms=binom[n+s-1][s]; tabs[s]=malloc(Ms*s); u8 c[20]; for(int i=0;i<s;i++) c[i]=0;
    while(1){ u64 r=rank_sorted(c,s); memcpy(tabs[s]+r*s,c,s); int i=s-1; while(i>=0&&c[i]==n-1) i--; if(i<0) break; c[i]++; for(int j=i+1;j<s;j++) c[j]=c[i]; } }
  #pragma omp parallel for schedule(static)
  for(u64 C=0;C<M;C++){ const u8*c=tup+C*k; u64 cm=0,nm=0; for(int i=0;i<k;i++){ cm|=1ULL<<c[i]; nm|=cl[c[i]]; }
    for(int r=0;r<n;r++){ u64 idx=C*n+r; if(cm>>r&1){cnt[idx]=0;continue;} cnt[idx]=(u8)__builtin_popcountll(cl[r]&~cm); if(nm>>r&1) ct[idx]=1; } }
  int round=1, done_cf=0, done_rf=0;
  while(1){
    u64 newrt=0;
    #pragma omp parallel for schedule(dynamic,4096) reduction(+:newrt)
    for(u64 idx=0;idx<NS;idx++){ if(ct[idx]!=round) continue; u64 C=idx/n; int rp=idx%n; const u8*c=tup+C*k; u64 cm=0; for(int i=0;i<k;i++) cm|=1ULL<<c[i];
      for(int t=0;t<nbc[rp];t++){ int r=nbl[rp][t]; if(cm>>r&1) continue; u64 j=C*n+r; if(__atomic_sub_fetch(&cnt[j],1,__ATOMIC_RELAXED)==0){ rt[j]=(u16)round; newrt++; } } }
    if(!done_rf){ int ok=0;
      #pragma omp parallel for schedule(static) reduction(|:ok)
      for(u64 C=0;C<M;C++){ if(ok) continue; const u8*c=tup+C*k; u64 cm=0; for(int i=0;i<k;i++) cm|=1ULL<<c[i]; int all=1; for(int r=0;r<n;r++){ if(cm>>r&1) continue; if(!rt[C*n+r]){all=0;break;} } if(all) ok=1; }
      if(ok){ done_rf=1; res.win_rf=1; res.rounds_rf=round; } }
    if(!done_cf){ int ok=0;
      #pragma omp parallel for schedule(static) reduction(|:ok)
      for(u64 C=0;C<M;C++){ if(ok) continue; const u8*c=tup+C*k; u64 cm=0; for(int i=0;i<k;i++) cm|=1ULL<<c[i]; int all=1; for(int r=0;r<n;r++){ if(cm>>r&1) continue; if(!ct[C*n+r]){all=0;break;} } if(all){ ok=1;
          #pragma omp critical
          { for(int i=0;i<k;i++) res.place[i]=c[i]; res.maxround_place=round; } } }
      if(ok){ done_cf=1; res.win_cf=1; res.rounds_cf=round; } }
    if(verbose) fprintf(stderr,"round %d: new RT %llu\n",round,(unsigned long long)newrt);
    if(newrt==0) break;
    if(early && done_cf) break;
    // staged propagation. Level 0 frontier: RT states with stamp==round.
    u64 newct=0;
    for(int j=0;j<k;j++){
      // iterate frontier of level j
      if(j==0){
        #pragma omp parallel for schedule(dynamic,1024) reduction(+:newct)
        for(u64 idx=0;idx<NS;idx++){ if(rt[idx]!=round) continue; u64 C=idx/n; int r=idx%n; const u8*U=tup+C*k;
          // move one cop u (distinct) to u'
          for(int a=0;a<k;a++){ if(a>0&&U[a]==U[a-1]) continue; u8 Up[20]; int m=0; for(int b=0;b<k;b++) if(b!=a) Up[m++]=U[b];
            for(int t=0;t<nbc[U[a]];t++){ u8 v=(u8)nbl[U[a]][t];
              if(k==1){ if(v==r) continue; u64 jdx=(u64)v*n+r; u16 z=0; if(__atomic_compare_exchange_n(&ct[jdx],&z,(u16)(round+1),0,__ATOMIC_RELAXED,__ATOMIC_RELAXED)) newct++; }
              else { u64 rU=rank_sorted(Up,k-1); u64 idx1=(rU*MV[1]+v)*(u64)n+r; test_and_set(lvl_mark[1],idx1); } } } }
      } else {
        u64 words=(lvl_cnt[j]+63)/64;
        #pragma omp parallel for schedule(dynamic,256) reduction(+:newct)
        for(u64 w=0;w<words;w++){ u64 fr=lvl_mark[j][w]&~lvl_done[j][w]; if(!fr) continue; lvl_done[j][w]|=fr;
          while(fr){ int b=__builtin_ctzll(fr); fr&=fr-1; u64 idx=w*64+b; int r=idx%n; u64 uv=idx/n; u64 rV=uv%MV[j], rU=uv/MV[j];
            const u8*U=tabs[k-j]+rU*(k-j); const u8*V=tabs[j]+rV*j; int su=k-j;
            for(int a=0;a<su;a++){ if(a>0&&U[a]==U[a-1]) continue; u8 Up[20]; int m=0; for(int bb=0;bb<su;bb++) if(bb!=a) Up[m++]=U[bb];
              for(int t=0;t<nbc[U[a]];t++){ u8 v=(u8)nbl[U[a]][t]; u8 Vp[20]; memcpy(Vp,V,j); Vp[j]=v; sort_small(Vp,j+1);
                if(j+1==k){ int on=0; for(int q=0;q<k;q++) if(Vp[q]==r){on=1;break;} if(on) continue; u64 P=rank_sorted(Vp,k); u64 jdx=P*n+r; u16 z=0;
                  if(__atomic_compare_exchange_n(&ct[jdx],&z,(u16)(round+1),0,__ATOMIC_RELAXED,__ATOMIC_RELAXED)) newct++; }
                else { u64 rUp=(su-1==0)?0:rank_sorted(Up,su-1); u64 rVp=rank_sorted(Vp,j+1); u64 idx1=(rUp*MV[j+1]+rVp)*(u64)n+r; test_and_set(lvl_mark[j+1],idx1); } } } } }
      }
    }
    if(verbose) fprintf(stderr,"round %d: new CT %llu\n",round,(unsigned long long)newct);
    if(newct==0) break;
    round++; if(round>=65000){ fprintf(stderr,"round overflow\n"); break; }
  }
  res.rounds_total=round;
  u64 wct=0,tot=0; double sum=0;
  #pragma omp parallel for reduction(+:wct,tot,sum)
  for(u64 idx=0;idx<NS;idx++){ u64 C=idx/n; int r=idx%n; const u8*c=tup+C*k; int on=0; for(int i=0;i<k;i++) if(c[i]==r){on=1;break;} if(on) continue; tot++; if(ct[idx]){ wct++; sum+=ct[idx]; } else sum+=(round+1); }
  res.frac_ct=(double)wct/(double)tot; res.mean_ct_round=sum/(double)tot;
  { u64 nw=0;
    #pragma omp parallel for reduction(+:nw)
    for(u64 C=0;C<M;C++){ const u8*c=tup+C*k; u64 cm=0; for(int i=0;i<k;i++) cm|=1ULL<<c[i]; int all=1; for(int r=0;r<n;r++){ if(cm>>r&1) continue; if(!ct[C*n+r]){all=0;break;} } nw+=all; }
    res.nwin_place=nw;
    // best placement = minimal max round over robber starts
    int bestmr=1<<30; u64 bestC=0; int found=0;
    for(u64 C=0;C<M;C++){ const u8*c=tup+C*k; u64 cm=0; for(int i=0;i<k;i++) cm|=1ULL<<c[i]; int all=1, mr=0; for(int r=0;r<n;r++){ if(cm>>r&1) continue; if(!ct[C*n+r]){all=0;break;} if(ct[C*n+r]>mr) mr=ct[C*n+r]; } if(all && mr<bestmr){ bestmr=mr; bestC=C; found=1; } }
    if(found){ for(int i=0;i<k;i++) res.place[i]=tup[bestC*k+i]; res.maxround_place=bestmr; } }
  free(tup); free(ct); free(rt); free(cnt); for(int j=1;j<k;j++){ free(lvl_mark[j]); free(lvl_done[j]); } for(int s=1;s<k;s++) free(tabs[s]);
  return res;
}
