"""Merge seed hints + finder candidates into verifier batches (vbatch format)."""
import json, sys, glob, os
S = os.path.dirname(os.path.abspath(__file__))  # expects new_nodes.json + statuses.json (see RELATIONS.md)
existing = {n['id']: n for n in json.load(open('data/relations_work/nodes.json'))}
new = {n['id']: n for n in json.load(open(f'{S}/new_nodes.json'))}
nodes = {**existing, **new}
# live statuses for existing nodes come from the build (captured in statuses.json)
status = json.load(open(f'{S}/statuses.json'))
def card(i):
    n = nodes[i]
    return {"id": i, "name": n.get("name"), "kind": n.get("kind"), "statement": n.get("statement", ""),
            "context": (n.get("context") or "")[:3000], "status": status.get(i, n.get("status"))}
cands = {}
for s in json.load(open(f'{S}/seed_pairs.json')):
    key = frozenset((s['a'], s['b']))
    cands[key] = {"claimed_relation": "unspecified (seed hint)", "via": "bm_hint", "origin": "bm_hint",
                  "finder_confidence": None, "sketches": [f"Bondy–Murty cross-check note on {s['a']}: {s['b']} — {s['hint']}"],
                  "pair": (s['a'], s['b'])}
for f in sorted(glob.glob(f'{S}/finder_*.json')):
    for c in json.load(open(f)):
        if c['source'] not in nodes or c['target'] not in nodes:
            print('skip unknown id', c); continue
        key = frozenset((c['source'], c['target']))
        if key in cands:
            cands[key]['sketches'].append(f"[{c['relation']} {c['source']} -> {c['target']}] {c['sketch']}")
            continue
        cands[key] = {"claimed_relation": c['relation'], "via": c.get('via'), "origin": "bm_finder",
                      "finder_confidence": c.get('confidence'), "sketches": [c['sketch']],
                      "pair": (c['source'], c['target'])}
out = []
for k, (key, c) in enumerate(cands.items()):
    a, b = c.pop('pair')
    out.append({"edge_id": f"b{k:03d}", **c, "n_finders": len(c['sketches']), "source": card(a), "target": card(b)})
json.dump(out, open(f'{S}/candidates_bm.json', 'w'), ensure_ascii=False, indent=1)
per = int(sys.argv[1]) if len(sys.argv) > 1 else 10
os.makedirs(f'{S}/verify', exist_ok=True)
for j in range(0, len(out), per):
    json.dump(out[j:j+per], open(f'{S}/verify/bm_vbatch_{j//per:02d}.json', 'w'), ensure_ascii=False, indent=1)
print(len(out), 'candidates', (len(out)+per-1)//per, 'batches')
