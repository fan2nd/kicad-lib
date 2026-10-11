"""Apply mikroBUS v2.00 graphics from the archived PDF; preserves electrical pads."""
from pathlib import Path
import json, math, re, hashlib
R=Path(__file__).resolve().parents[1]
contours=json.loads((R/'scripts/data/mikrobus-logo-contours.json').read_text())['contours']
def line(a,b,layer,w=.12):return f'(fp_line (start {a[0]:.6f} {a[1]:.6f}) (end {b[0]:.6f} {b[1]:.6f}) (stroke (width {w}) (type solid)) (layer "{layer}"))'
def arc(c,a,b,layer):
 def pt(t):return f'{c[0]+2.54*math.cos(t):.6f} {c[1]+2.54*math.sin(t):.6f}'
 return f'(fp_arc (start {pt(a)}) (mid {pt((a+b)/2)}) (end {pt(b)}) (stroke (width .12) (type solid)) (layer "{layer}"))'
def logo(cx,cy,layer):
 # Filled vector strips use even-odd contour intersections, preserving glyph holes.
 # <= 0.02 mm discretization, without dependence on installed fonts or bitmap files.
 ys=[y for p in contours for x,y in p];lo,hi=min(ys),max(ys);n=math.ceil((hi-lo)/.02);dy=(hi-lo)/n;out=[]
 for i in range(n):
  y=lo+(i+.5)*dy;hits=[]
  for p in contours:
   for (x1,y1),(x2,y2) in zip(p,p[1:]+p[:1]):
    if (y1<=y<y2) or (y2<=y<y1):hits.append(x1+(x2-x1)*(y-y1)/(y2-y1))
  hits.sort();assert len(hits)%2==0
  for a,b in zip(hits[::2],hits[1::2]):
   if b-a<.001:continue
   if layer=='B.SilkS':a,b=-b,-a
   pts=[(cx+a,cy+y-dy/2),(cx+b,cy+y-dy/2),(cx+b,cy+y+dy/2),(cx+a,cy+y+dy/2)]
   out.append('(fp_poly (pts '+' '.join(f'(xy {x:.5f} {yy:.5f})' for x,yy in pts)+f') (stroke (width 0) (type solid)) (fill solid) (layer "{layer}"))')
 return out
changed=[]
for p in (R/'fontprints/3rd.connector.pretty').glob('mikroBUS_*.kicad_mod'):
 host='_Socket_' in p.name;s=p.read_text();pads=[l for l in s.splitlines() if l.startswith('(pad')];out=[]
 for l in s.splitlines():
  if l==')':continue
  if l.startswith('(fp_poly'):continue
  if l.startswith('(fp_text user "mikroBUS'):continue
  if l.startswith('(fp_text value') and not host:
   # Preserve the separate hidden Value and BoardName-driven user text.
   pass
  if l.startswith('(fp_text user') and '(layer "F.SilkS")' in l and not host:
   l=re.sub(r'(\(at [-.\d]+ [-.\d]+) 0\)',r'\1 90)',l).replace('(size 0.8 0.8)','(size 0.65 0.65)')
  if host and l.startswith('(fp_arc'):continue
  if host and l.startswith('(fp_line') and ('(layer "F.SilkS")' in l or '(layer "B.SilkS")' in l):
   m=re.search(r'\(start ([-.\d]+) ([-.\d]+)\) \(end ([-.\d]+) ([-.\d]+)\)',l);x,y,xx,yy=map(float,m.groups())
   # Keep physical 2.54 x 20.32 mm female-header rectangles, replace socket graphics.
   if not (x in [-1.27,1.27,21.59,24.13] and xx in [-1.27,1.27,21.59,24.13] and y in [-1.27,19.05] and yy in [-1.27,19.05] and abs(x-xx)<=2.541):continue
  out.append(l)
 if host:
  for layer in ['F.SilkS','B.SilkS']:
   # Official fixed socket envelope: 27.94 x 28.575 mm; open across the top.
   out.extend([arc((0,-3.175),math.pi,math.pi*1.5,layer),line((-2.54,-3.175),(-2.54,20.32),layer),arc((0,20.32),math.pi/2,math.pi,layer),line((0,22.86),(22.86,22.86),layer),arc((22.86,20.32),0,math.pi/2,layer),line((25.4,20.32),(25.4,-3.175),layer),arc((22.86,-3.175),-math.pi/2,0,layer),line((21.59,21.59),(24.13,19.05),layer)])
   out.extend(logo(11.43,-3.55,layer))
 else:
  out.extend(logo(11.43,-3.55,'F.SilkS'))
  out.extend(logo(11.43,-3.55,'B.SilkS'))
 out.append(')');new='\n'.join(out)+'\n';assert pads==[l for l in new.splitlines() if l.startswith('(pad')];p.write_text(new);changed.append(str(p.relative_to(R)))
p=R/'scripts/data/library-classification.json';j=json.loads(p.read_text())
for row in j:
 if row.get('new_path') in changed:
  row['approved_geometry_sha256']=hashlib.sha256((R/row['new_path']).read_bytes()).hexdigest();row['geometry_changes']+=' 2026-10-10: user requests official manual markings, overriding prior horizontal-front choice. Official PDF vector logo, open-top fixed socket silk, vertical module-front labels, horizontal rear labels, editable BOARD_NAME; original electrical pads and board outlines preserved.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
