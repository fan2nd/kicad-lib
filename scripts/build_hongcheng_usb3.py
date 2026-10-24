"""HongCheng USB3 recessed connectors: manufacturer recommended lands, mm.
C34/C225 open notch dimensions from LCSC CAD; verify carrier fit before production.
"""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
for part,lc,front,rear,nw,ny,edge in [('C34','C7501852',13.55,-.65,13.2,2.05,11.57),('C225','C7501855',13.6,-.6,13.2,1.435,13.6),('C345','C7501863',13.2,.8,13.6,1.7,13.2)]:
 name='HongCheng_HC-USB3.0-'+part+'-P'
 a=[f'(footprint "{name}" (version 20241229) (generator "project_library") (layer "F.Cu") (attr smd)',f'(descr "{lc}; recessed USB3 Type A; integrate open U notch into carrier outline. '+('No independent external pin 7; do not assume connection to shell.' if part=='C345' else 'Notch based on LCSC CAD, width 13.2 to clear shell lands; verify fit.')+'")']
 def txt(k,t,x,y,l):a.append(f'(fp_text {k} "{t}" (at {x} {y}) (layer "{l}") (effects (font (size .8 .8) (thickness .12))))')
 def line(x,y,xx,yy,l,w=.1):a.append(f'(fp_line (start {x} {y}) (end {xx} {yy}) (stroke (width {w}) (type solid)) (layer "{l}"))')
 def poly(ps,l,w=.1):
  for p,q in zip(ps,ps[1:]):line(*p,*q,l,w)
 def smd(n,x,y,w,h):a.append(f'(pad "{n}" smd roundrect (at {x} {y}) (size {w} {h}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio {min(.25,.25*min(w,h))/min(w,h):.9f}))')
 def slot(x,y,w,h,dw,dh):a.append(f'(pad "SH" thru_hole oval (at {x} {y}) (size {w} {h}) (drill oval {dw} {dh}) (layers "*.Cu" "*.Mask"))')
 txt('reference','REF**',0,-3.2,'F.SilkS');txt('value',name,0,front+2.4,'F.Fab')
 poly([(-6.55,rear),(6.55,rear),(6.55,front),(-6.55,front),(-6.55,rear)],'F.Fab')
 if part!='C345':
  for n,x in zip([9,1,8,2,7,3,6,4,5],range(-4,5)):smd(n,x,0,.7,1.6)
  px=-3
  for x in [-1,1]:
   slot(x*(6.4 if part=='C34' else 8),.1 if part=='C34' else .8,1.2,2.5 if part=='C34' else 3,.6,2 if part=='C34' else 2.5)
   for y in ([7.9] if part=='C34' else [4.75,7.95]):smd('SH',x*7.45,y,1.6,1.5)
 else:
  for n,x in [(1,-3),(2,-.7),(3,.7),(4,3)]:smd(n,x,0,1,2.2)
  for n,x in [(9,-5.135),(8,-4.435),(6,4.435),(5,5.135)]:smd(n,x,0,.45,2.2)
  px=-3
  for x in [-7.95,7.95]:
   for y in [1.5,7]:slot(x,y,1.8,2.8,.6,1.6)
 # Pin 1 dot, above lands; body silk only on solid PCB, outside contact row.
 a.append(f'(fp_circle (center {px} -1.65) (end {px+.15} -1.65) (stroke (width .1) (type solid)) (fill solid) (layer "F.SilkS"))')
 for sign in [-1,1]:
  line(sign*5.7,-1.65,sign*6.55,-1.65,'F.SilkS',.12)

 poly([(-nw/2,edge),(-nw/2,ny),(nw/2,ny),(nw/2,edge)],'Edge.Cuts',.05)
 txt('user','PCB EDGE',0,edge,'Dwgs.User')
 for sign in [-1,1]:line(sign*nw/2,edge,sign*9.5,edge,'Dwgs.User')
 poly([(-9.2,-2.1),(9.2,-2.1),(9.2,front+.3),(-9.2,front+.3),(-9.2,-2.1)],'F.CrtYd',.05)
 a.append(f'(model "{R}/3dmodels/3rd.connector.3dshapes/{name}.wrl" (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 0)))')
 a.append(')');(R/'fontprints/3rd.connector.pretty'/(name+'.kicad_mod')).write_text('\n'.join(a)+'\n')
