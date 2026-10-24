"""C530628: datasheet lands; 13.2 mm notch width cross-checked against LCSC CAD."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
name='HRO_U-A-24DS-W-1'
a=[f'(footprint "{name}" (version 20241229) (generator "project_library") (layer "F.Cu") (attr smd)',
'(descr "C530628; recessed USB-A receptacle; Connector:USB_A pins 1/2/3/4/SH. Open Edge.Cuts notch must join carrier outline at y=9.5; notch width 13.2 from LCSC reference CAD.")',
'(tags "USB Type-A recessed HRO C530628")']
def text(kind,s,x,y,layer,size=.8):a.append(f'(fp_text {kind} "{s}" (at {x} {y}) (layer "{layer}") (effects (font (size {size} {size}) (thickness .12))))')
def line(x,y,xx,yy,layer,w=.1,style='solid'):a.append(f'(fp_line (start {x} {y}) (end {xx} {yy}) (stroke (width {w}) (type {style})) (layer "{layer}"))')
def poly(points,layer,w=.1):
 for (x,y),(xx,yy) in zip(points,points[1:]):line(x,y,xx,yy,layer,w)
text('reference','REF**',0,-4.1,'F.SilkS')
text('value',name,0,11.5,'F.Fab')
# Body envelope: front extends 0.75 mm past recommended PCB edge.
poly([(-6.55,-.8),(6.55,-.8),(6.55,10.25),(-6.55,10.25),(-6.55,-.8)],'F.Fab')
# Shell tabs in fabrication view.
for x in [-7.775,7.775]:
 for y in [0,5.5]:
  xx=6.55 if x>0 else -6.55
  poly([(xx,y-.9),(x,y-.9),(x,y+.9),(xx,y+.9)],'F.Fab')
for x0,x1 in [(-6.55,-4.35),(-2.65,-1.85),(-.15,.15),(1.85,2.65),(4.35,6.55)]:line(x0,-.8,x1,-.8,'F.SilkS',.12)
# Silk stays on the PCB outside the notch and clear of the shell lands.
for x in [-6.9,6.9]:
 for ya,yb in [(1.5,4),(7,9.2)]:line(x,ya,x,yb,'F.SilkS',.12)
a.append('(fp_circle (center -4.6 -2.1) (end -4.4 -2.1) (stroke (width .1) (type solid)) (fill solid) (layer "F.SilkS"))')
# Nominal manufacturer lands, 2.5 / 2.0 / 2.5 mm contact pitch.
for n,x in enumerate([-3.5,-1,1,3.5],1):
 a.append(f'(pad "{n}" smd roundrect (at {x} -1.825) (size 1.15 2.45) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio {0.25/1.15:.9f}))')
# 0.8 x 1.8 mm plated slots, 0.25 mm copper annulus, all shell contacts common.
for x in [-7.775,7.775]:
 for y in [0,5.5]:a.append(f'(pad "SH" thru_hole oval (at {x} {y}) (size 1.3 2.3) (drill oval .8 1.8) (layers "*.Cu" "*.Mask"))')
# Open U notch, not a closed rectangular cutout. Integrate endpoints into board outline.
poly([(-6.6,9.5),(-6.6,0),(6.6,0),(6.6,9.5)],'Edge.Cuts',.05)
for x0,x1 in [(-9,-6.6),(6.6,9)]:line(x0,9.5,x1,9.5,'Dwgs.User',.1,'dash')
text('user','PCB EDGE',0,9.5,'Dwgs.User')
poly([(-8.7,-3.3),(8.7,-3.3),(8.7,10.5),(-8.7,10.5),(-8.7,-3.3)],'F.CrtYd',.05)
a.append(f'(model "{ROOT}/3dmodels/3rd.connector.3dshapes/HRO_U-A-24DS-W-1.wrl" (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 0)))')
a.append(')')
(ROOT/'fontprints/3rd.connector.pretty'/(name+'.kicad_mod')).write_text('\n'.join(a)+'\n')
