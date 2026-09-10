#include "cr_common.h"
int main(int argc,char**argv){
  init_binom(); int k=0,verbose=0,copnum=0,maxk=0,early=0;
  for(int i=1;i<argc;i++){ if(!strcmp(argv[i],"-v")) verbose=1; else if(!strcmp(argv[i],"-e")) early=1; else if(!strcmp(argv[i],"-c")){copnum=1;maxk=atoi(argv[++i]);} else k=atoi(argv[i]); }
  char line[8192];
  while(fgets(line,sizeof line,stdin)){
    size_t L=strlen(line);
    while(L&&(line[L-1]=='\n'||line[L-1]=='\r')) line[--L]=0;
    // A graph6 header may share the first graph's line.
    const size_t header_len=sizeof(">>graph6<<")-1;
    if(!strncmp(line,">>graph6<<",header_len)){
      memmove(line,line+header_len,L-header_len+1);
      L-=header_len;
    }
    if(!L) continue;
    if(parse_g6(line)){ fprintf(stderr,"bad g6: %s\n",line); continue; }
    if(copnum){ int c=-1; result_t r; for(int kk=1;kk<=maxk;kk++){ r=solve_staged(kk,verbose,early); if(r.win_cf){c=kk;break;} }
      if(c>0) printf("%s n=%d c=%d capture_rounds=%d\n",line,n,c,r.rounds_cf); else printf("%s n=%d c>%d frac_ct(k=%d)=%.6f\n",line,n,maxk,maxk,r.frac_ct); }
    else { result_t r=solve_staged(k,verbose,early);
      printf("%s n=%d k=%d win_cf=%d rounds_cf=%d win_rf=%d rounds_rf=%d frac_ct=%.6f mean_ct=%.4f M=%llu nwin=%llu",line,n,k,r.win_cf,r.rounds_cf,r.win_rf,r.rounds_rf,r.frac_ct,r.mean_ct_round,(unsigned long long)r.M,(unsigned long long)r.nwin_place); if(r.win_cf){ printf(" placement="); for(int i=0;i<k;i++) printf("%d%s",r.place[i],i<k-1?",":""); printf(" maxround=%d",r.maxround_place);} printf("\n"); }
    fflush(stdout); }
  return 0; }
