"""Validate classified KiCad library links, ball/pad identities and parsing."""
import json,re,sys,subprocess,tempfile,hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[1]
def parse(s):
 stack=[];root=[];cur=root
 for a in re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',s):
  if a=='(':n=[];cur.append(n);stack.append(cur);cur=n
  elif a==')':cur=stack.pop()
  else:cur.append(json.loads(a) if a.startswith('"') else a)
 assert not stack
 return root[0]
def many(n,k):return [v for v in n if isinstance(v,list) and v[0]==k]
def walk(n,k):
 for v in n:
  if isinstance(v,list):
   if v and v[0]==k:yield v
   yield from walk(v,k)
def get(n,k):return next((v for v in n if isinstance(v,list) and v[0]==k),None)
fps={};symbols=list(ROOT.glob('symbols/*.kicad_symdir/*.kicad_sym'));footprints=list(ROOT.glob('fontprints/*.pretty/*.kicad_mod'))
for p in footprints:
 n=parse(p.read_text());assert n[1]==p.stem,(p,n[1]);fps[p.parent.stem+':'+p.stem]={v[1] for v in many(n,'pad') if v[1]}
 for pad in many(n,'pad'):
  assert pad[3]!='rect',f'{p.name}: rectangular pad {pad[1]} must use roundrect (see AGENTS.md)'
  if pad[3]=='roundrect':
   ratio=get(pad,'roundrect_rratio')
   assert ratio and 0<float(ratio[1])<=0.5,f'{p.name}: invalid corner radius for {pad[1]}'
errors=[];linked=0
for p in symbols:
 for sym in many(parse(p.read_text()),'symbol'):
  ref=next((v[2] for v in many(sym,'property') if v[1]=='Footprint'),'')
  if not ref:continue
  if not ref.startswith('3rd.'):
   if ref.startswith(('3rd:','fontprints:')):errors.append(f'{p.name}: stale {ref}')
   continue
  if ref not in fps:errors.append(f'{p.name}: missing {ref}');continue
  nums={get(v,'number')[1] for v in walk(sym,'pin')};pads=fps[ref]
  if nums!=pads:errors.append(f'{p.name}: symbol-only {sorted(nums-pads)}, pad-only {sorted(pads-nums)}')
  linked+=1
for row in json.loads((ROOT/'scripts/data/library-classification.json').read_text()):
 if row['kind']=='footprint':
  content=(ROOT/row['new_path']).read_bytes()
  if row.get('approved_geometry_sha256'):
   assert row.get('geometry_changes'), 'Geometry approval requires a recorded reason'
   assert hashlib.sha256(content).hexdigest()==row['approved_geometry_sha256']
   continue
  for old,new in row.get('name_changes',{}).items():
   for prefix in ['(footprint ', '(property "Value" ']:
    content=content.replace((prefix+'"'+new+'"').encode(),(prefix+'"'+old+'"').encode())
  for old,new in row.get('text_changes',{}).items():
   content=content.replace(('\"'+new+'\"').encode(),('\"'+old+'\"').encode())
  assert hashlib.sha256(content).hexdigest()==row['before_sha256']
for filename,tag,ext in [('sym-lib-table','sym_lib_table','.kicad_symdir'),('fp-lib-table','fp_lib_table','.pretty')]:
 for lib in many(parse((ROOT/filename).read_text()),'lib'):
  uri=get(lib,'uri')[1].replace('${KIPRJMOD}',str(ROOT));assert Path(uri).exists(),uri
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(symbols)} symbol files; {len(footprints)} footprints; {linked} symbol-footprint mappings; footprint baselines validated; library tables resolve.')
if '--export' in sys.argv:
 cli='/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli';tmp=Path(tempfile.mkdtemp(prefix='classified-kicad-'))
 jobs=[([cli,'sym','export','svg','--output',str(tmp/p.stem),str(p)],p) for p in symbols]+[([cli,'fp','export','svg','--layers','F.SilkS,F.Cu','--footprint',p.stem,'--output',str(tmp/p.stem),str(p.parent)],p) for p in footprints]
 def run(job):
  args,p=job;Path(args[args.index('--output')+1]).mkdir(exist_ok=True);r=subprocess.run(args,capture_output=True,text=True);return p,r
 with ThreadPoolExecutor(max_workers=4) as ex:
  results=list(ex.map(run,jobs))
 bad=[str(p)+': '+r.stderr+r.stdout for p,r in results if r.returncode or not list((tmp/p.stem).glob('*.svg'))]
 if bad:print('\n'.join(bad));sys.exit(1)
 print(f'PASS: all {len(jobs)} files exported by KiCad; outputs {tmp}')
