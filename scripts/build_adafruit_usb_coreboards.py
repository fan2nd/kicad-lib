"""Carrier footprints derived from Adafruit's Eagle boards, top view, USB left."""
from pathlib import Path
import xml.etree.ElementTree as E
import math,json,hashlib,re
R=Path(__file__).resolve().parents[1]
def line(a,b,l='F.SilkS',w=.12):return f'(fp_line (start {a[0]:.6f} {a[1]:.6f}) (end {b[0]:.6f} {b[1]:.6f}) (stroke (width {w}) (type solid)) (layer "{l}"))'
def arc(a,m,b,l):return f'(fp_arc (start {a[0]:.6f} {a[1]:.6f}) (mid {m[0]:.6f} {m[1]:.6f}) (end {b[0]:.6f} {b[1]:.6f}) (stroke (width .12) (type solid)) (layer "{l}"))'
def text(k,s,x,y,size=.75,l='F.SilkS',hide=False):return f'(fp_text {k} "{s}" (at {x} {y}) (layer "{l}")'+(' hide' if hide else '')+f' (effects (font (size {size} {size}) (thickness .12))))'
def rect(x1,y1,x2,y2,l):
 p=[(x1,y1),(x2,y1),(x2,y2),(x1,y2)];return [line(a,b,l) for a,b in zip(p,p[1:]+p[:1])]
for model,src,W,H in [('MCP2221A','MCP2221',25.4,17.78),('FT232H','FT232H',38.1,22.86)]:
 name='Adafruit_'+model;b=E.parse(R/f'docs/Adafruit_{model}_PCB.brd').find('.//board')
 f=[f'(footprint "{name}" (version 20240108) (generator "project_library") (layer "F.Cu") (attr through_hole)',f'(descr "Adafruit {model} USB-C board above carrier; official Eagle outline and header coordinates; mounting holes shown as reference circles, no carrier drilling")',text('reference','REF**',W/2,-2,1),text('value',name,W/2,H+2,1,'F.Fab',True)]
 def cv(x,y):return (x,H-y)
 for w in b.findall('./plain/wire'):
  if w.get('layer')!='20':continue
  x1,y1,x2,y2=[float(w.get(k)) for k in ['x1','y1','x2','y2']];a=cv(x1,y1);z=cv(x2,y2)
  for layer in ['F.SilkS','F.Fab']:
   if not w.get('curve'):f.append(line(a,z,layer))
   else:
    theta=math.radians(float(w.get('curve')));dx=x2-x1;dy=y2-y1;cx=(x1+x2)/2-dy/(2*math.tan(theta/2));cy=(y1+y2)/2+dx/(2*math.tan(theta/2));u=x1-cx;v=y1-cy;t=theta/2;m=cv(cx+u*math.cos(t)-v*math.sin(t),cy+u*math.sin(t)+v*math.cos(t));f.append(arc(a,m,z,layer))
 nets={(r.get('element'),r.get('pad')):sig.get('name') for sig in b.findall('./signals/signal') for r in sig.findall('contactref')}
 holes=[(float(h.get('x')),float(h.get('y')),float(h.get('drill'))) for h in b.findall('./plain/hole')];rows={};records=[]
 for e in b.findall('./elements/element'):
  if not (e.get('name').startswith('JP') or e.get('name') in ['X6','CONN1'] or 'MOUNTINGHOLE' in e.get('package')):continue
  pkg=b.find('./libraries/library[@name="'+e.get('library')+'"]/packages/package[@name="'+e.get('package')+'"]');ang=math.radians(float(e.get('rot','R0').replace('R','')))
  def pos(x,y):return (float(e.get('x'))+x*math.cos(ang)-y*math.sin(ang),float(e.get('y'))+x*math.sin(ang)+y*math.cos(ang))
  if 'MOUNTINGHOLE' in e.get('package'):
   for p in pkg.findall('pad'):holes.append((*pos(float(p.get('x')),float(p.get('y'))),float(p.get('drill'))))
  if e.get('name') in ['X6','CONN1']:
   for w in pkg.findall('wire'):
    if w.get('layer')=='51':
     f.append(line(cv(*pos(float(w.get('x1')),float(w.get('y1')))),cv(*pos(float(w.get('x2')),float(w.get('y2')))),'F.Fab'))
  if not e.get('name').startswith('JP'):continue
  for p in pkg.findall('pad'):
   net=nets[e.get('name'),p.get('name')];n={'+5V':'5V','+3V3':'3V','!RST':'~{R}','GP0':'G0','GP1':'G1','GP2':'G2','GP3':'G3'}.get(net,net.split('/')[0]);x,y=cv(*pos(float(p.get('x')),float(p.get('y'))));x=round(x,6);y=round(y,6);d=float(p.get('diameter'));f.append(f'(pad "{n}" thru_hole circle (at {x} {y}) (size {d} {d}) (drill 1) (layers "*.Cu" "*.Mask"))');rows.setdefault(y,[]).append(x);records.append((n,x,y))
   f.append(text('user',{'~{R}':'RST','3V':'3V3'}.get(n,n),x,y+(2.8 if y<H/2 else -2.8)))
 for y,xs in rows.items():
  for a,z in [((min(xs)-1.27,y-1.27),(max(xs)+1.27,y-1.27)),((max(xs)+1.27,y-1.27),(max(xs)+1.27,y+1.27)),((max(xs)+1.27,y+1.27),(min(xs)-1.27,y+1.27)),((min(xs)-1.27,y+1.27),(min(xs)-1.27,y-1.27))]:
   if abs(a[1]-z[1])<1e-8 and (abs(a[1])<1e-6 or abs(a[1]-H)<1e-6):continue
   f.append(line(a,z))
 for x,y,d in holes:
  x,y=cv(x,y)
  for layer in ['F.SilkS','F.Fab']:f.append(f'(fp_circle (center {x} {y}) (end {x+d/2} {y}) (stroke (width .12) (type solid)) (layer "{layer}"))')
 f += [text('user',model,W/2,H/2,1),text('user','USB',2.7,H/2,.65),text('user','Qwiic',W-2.7,H/2,.65)]
 # USB shell projects beyond the board's left edge, as in its official package.
 usb=next(e for e in b.findall('./elements/element') if e.get('name')=='X6');xmin=min(0,float(usb.get('x'))-3.81)
 f+=rect(xmin-.25,-.25,W+.25,H+.25,'F.CrtYd');f.append(')')
 path=R/f'fontprints/3rd.coreboard.pretty/{name}.kicad_mod';content='\n'.join(f)+'\n'
 # Rotate the whole module clockwise: USB at top, board top-centre origin.
 # All pads are circular; text angles remain zero for horizontal reading.
 def rotate(m):
  tag,x,y=m.group(1),float(m.group(2)),float(m.group(3))
  return f'({tag} {H/2-y:.6f} {x:.6f})'
 content=re.sub(r'\((at|start|mid|end|center) ([-0-9.]+) ([-0-9.]+)\)',rotate,content)
 content=re.sub(r'(\(fp_text reference "REF\*\*" )\(at [^)]+\)',r'\g<1>(at 0 -2)',content)
 content=re.sub(r'(\(fp_text value "[^"]+" )\(at [^)]+\)',lambda m:m.group(1)+f'(at 0 {W+2})',content)
 path.write_text(content)
 jf=R/'scripts/data/library-classification.json';j=json.loads(jf.read_text())
 for r in j:
  if r.get('new_path')==str(path.relative_to(R)):
   r['approved_geometry_sha256']=hashlib.sha256(path.read_bytes()).hexdigest();r['geometry_changes']=r.get('geometry_changes','')+' 2026-10-10: redraw from official Adafruit Eagle USB-C boards; header coordinates/net names verified, rounded board outline and mounting reference circles, horizontal internal labels including MCP RST; USB-C and Qwiic outlines on fab only (silk outlines reverted at user request); no Edge.Cuts or mandatory mounting drills.'
 jf.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
 print(name,records)
