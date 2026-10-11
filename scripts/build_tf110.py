"""TF-110 rev A manufacturer recommended PCB land pattern, dimensions in mm.
Origin: rear-edge centre x=0,y=-5.625. Dimensions follow docs/XUNPU_TF-110_Datasheet_RevA.pdf.
"""
from pathlib import Path
import json,hashlib,math
R=Path(__file__).resolve().parents[1];name='XUNPU_TF-110';lib='3rd.connector';url='https://datasheet.lcsc.com/datasheet/pdf/f61401d73ff07d6fa7a26c89f45b113b.pdf?productCode=C266613'
y0=-5.625
pads=[]
def land(n,x1,y1,x2,y2):pads.append(dict(number=n,x=(x1+x2)/2,y=(y1+y2)/2+y0,w=x2-x1,h=y2-y1,rect=(x1,y1,x2,y2)))
func=['DAT2','CD/DAT3','CMD','VDD','CLK','VSS','DAT0','DAT1']
for i,n in enumerate(func):
 x=3.2-i*1.1;land(n,x-.375,8.35,x+.375,9.70)
land('CD/SWA',4.2-.325,8.35,4.2+.325,9.70)
# top outer pads: (11.95-9.80)/2 = 1.075 wide; inner top pads dimensioned separately
land('SHELL',-5.975,0,-4.90,1.05);land('SHELL',-4.50,0,-3.10,1.05)
land('SHELL',2.30,0,3.70,1.05);land('SHELL',4.90,0,5.975,1.05)
land('GND/SWB',4.95,2.40,5.975,3.55)
land('SHELL',-5.975,4.15,-5.36,5.35)
land('SHELL',5.25,4.85,5.975,6.05)
land('SHELL',-5.975,10.05,-4.35,11.55)
land('SHELL',4.19,10.05,5.975,11.55)
def ln(a,b,layer,w=.12):return f'(fp_line (start {a[0]:.6f} {a[1]:.6f}) (end {b[0]:.6f} {b[1]:.6f}) (stroke (width {w}) (type solid)) (layer "{layer}"))'
def poly(v,layer,w=.1):return [ln(a,b,layer,w) for a,b in zip(v,v[1:]+v[:1])]
def text(kind,t,x,y,layer,size=.7,angle=0,hide=False):return f'(fp_text {kind} "{t}" (at {x} {y} {angle}) (layer "{layer}")'+(' hide' if hide else '')+f' (effects (font (size {size} {size}) (thickness .1))))'
f=[f'(footprint "{name}" (version 20240108) (generator "project_library") (layer "F.Cu") (attr smd)', '(descr "XUNPU TF-110 Rev A, C266613; 11.35x11.25mm H1.32; push-pull microSD; SWA-SWB closed without card, open inserted. Legacy pad identifier GND/SWB means SWB only, not an internal GND connection.")',text('reference','REF**',0,-6.8,'F.SilkS',1),text('value','TF-110',0,7.0,'F.Fab',1)]
for p in pads:
 ratio=min(.25*min(p['w'],p['h']),.25)/min(p['w'],p['h'])
 f.append(f'(pad "{p["number"]}" smd roundrect (at {p["x"]:.6f} {p["y"]:.6f}) (size {p["w"]:.6f} {p["h"]:.6f}) (layers "F.Cu" "F.Mask" "F.Paste") (roundrect_rratio {ratio:.9f}))')
# Housing contour digitized from the manufacturer's top-view vectors, calibrated
# to the dimensioned 11.35 x 11.25 mm envelope. Minor stamped details omitted.
def xy(x,y):return ((x-163.5115)*11.35/102.943,(y-136.5765)*11.25/102.103)
def arc(a,m,b,layer,w=.12):
 return f'(fp_arc (start {a[0]:.6f} {a[1]:.6f}) (mid {m[0]:.6f} {m[1]:.6f}) (end {b[0]:.6f} {b[1]:.6f}) (stroke (width {w}) (type solid)) (layer "{layer}"))'
left=[(-5.675,-5.625),(-5.675,5.625),xy(118.159,187.628),xy(119.359,186.788),xy(124.158,177.190),xy(125.238,176.470)]
right=[xy(201.665,176.470),xy(202.745,177.190),xy(207.545,186.788),xy(208.744,187.629),(5.675,5.625),(5.675,-5.625)]
for chain in [left,right]:f += [ln(a,b,'F.Fab',.1) for a,b in zip(chain,chain[1:])]
f += [ln(left[0],right[-1],'F.Fab',.1),arc(left[-1],xy(163.4515,174.910),right[0],'F.Fab',.1)]
# General segment/rectangle clipping, including the sloping mouth edges.
def clear_intervals(a,b):
 intervals=[(0.,1.)]
 for p in pads:
  box=(p['x']-p['w']/2-.26,p['y']-p['h']/2-.26,p['x']+p['w']/2+.26,p['y']+p['h']/2+.26)
  lo,hi=0.,1.
  for i in range(2):
   d=b[i]-a[i]
   if abs(d)<1e-12:
    if not box[i]<=a[i]<=box[i+2]:lo,hi=1.,0.;break
   else:
    u,v=sorted(((box[i]-a[i])/d,(box[i+2]-a[i])/d));lo=max(lo,u);hi=min(hi,v)
  if lo<=hi:
   intervals=[part for u,v in intervals for part in [(u,min(v,lo)),(max(u,hi),v)] if part[1]-part[0]>1e-8]
 return intervals
def lerp(a,b,t):return tuple(a[i]+t*(b[i]-a[i]) for i in range(2))
def silk_segment(a,b):return [ln(lerp(a,b,u),lerp(a,b,v),'F.SilkS') for u,v in clear_intervals(a,b) if math.dist(a,b)*(v-u)>.02]
# Move side/back silk .15 mm outward. Mouth curve offset toward card by .20 mm
# so its central section clears the row of signal lands.
for a,b in [((-5.825,-5.775),(5.825,-5.775)),((-5.825,-5.775),(-5.825,5.825)),((5.825,-5.775),(5.825,5.825))]:f+=silk_segment(a,b)
for chain in [left[1:],right[:-1]]:
 shifted=[(x,y+.20) for x,y in chain]
 for a,b in zip(shifted,shifted[1:]):f+=silk_segment(a,b)
a=left[-1];b=right[0];m=xy(163.4515,174.910)
# Symmetric shallow circular arc fitted to the PDF mouth profile.
cx=(a[0]+b[0])/2;half=(b[0]-a[0])/2;sag=a[1]-m[1]
r=(half*half+sag*sag)/(2*sag);cy=m[1]+r
rr=r-.20;ang=math.asin(half/r)
def mouth(t):
 theta=-ang+2*ang*t;return (cx+rr*math.sin(theta),cy-rr*math.cos(theta))
# Retain true KiCad arcs, splitting only where required by copper clearance.
for i in range(80):
 u=i/80;v=(i+1)/80
 for lo,hi in clear_intervals(mouth(u),mouth(v)):
  q=u+(v-u)*lo;z=u+(v-u)*hi
  if (z-q)*2*ang*rr>.005:f.append(arc(mouth(q),mouth((q+z)/2),mouth(z),'F.SilkS'))
# Fully inserted card: visible portion, width 11.00 mm and protrusion 3.90 mm.
# Bottom corner radius .8 mm is derived from the manual's drawing, not a tolerance.
card=[(-5.5,5.625),(-5.5,8.725)]
for i in range(1,25):
 t=math.pi-math.pi/2*i/24;card.append((-4.7+.8*math.cos(t),8.725+.8*math.sin(t)))
card.append((4.7,9.525))
for i in range(1,25):
 t=math.pi/2-math.pi/2*i/24;card.append((4.7+.8*math.cos(t),8.725+.8*math.sin(t)))
card.append((5.5,5.625))
# Explicit dashed strokes give identical previews in KiCad and other viewers.
phase=0.
for a,b in zip(card,card[1:]):
 length=math.dist(a,b);pos=0.
 while pos<length-1e-9:
  on=phase<.6;step=min(length-pos,(.6 if on else 1.)-phase)
  aa=lerp(a,b,pos/length);bb=lerp(a,b,(pos+step)/length)
  if on:
   f.append(ln(aa,bb,'Dwgs.User',.1));f+=silk_segment(aa,bb)
  pos+=step;phase=(phase+step)%1.
f.append(text('user','CARD INSERTED',0,10.3,'Dwgs.User',.65))
f += [ln((0,5.70),(0,4.95),'F.SilkS'),ln((0,4.95),(-.30,5.25),'F.SilkS'),ln((0,4.95),(.30,5.25),'F.SilkS')]
f+=poly([(-6.25,-5.9),(6.25,-5.9),(6.25,6.2),(-6.25,6.2)],'F.CrtYd',.05)
for i,n in enumerate(func+['CD/SWA']):
 x=3.2-i*1.1 if i<8 else 4.2
 # End the vertical labels before signal lands; keep inside the socket body.
 label={'CD/DAT3':'DAT3','CD/SWA':'SWA'}.get(n,n)
 f.append(text('user',label,x,1.05,'F.SilkS',.6,90))
f += [text('user','SWB',3.55,-2.65,'F.SilkS',.65),text('user','TF-110',-.6,-3.8,'F.SilkS',.8)]
# User-requested single rectangular rule area covering the central hatched field.
# Keep signal lands and their escape routing outside; no tiled pad subtraction.
rects=[(-5.28,1.70,5.25,6.90)]
for a,b,c,d in rects:
 pts=[(a,b+y0),(c,b+y0),(c,d+y0),(a,d+y0)]
 f.append('(zone (net 0) (net_name "") (layer "F.Cu") (hatch edge 0.5) (keepout (tracks not_allowed) (vias not_allowed) (pads allowed) (copperpour not_allowed) (footprints allowed)) (polygon (pts '+' '.join(f'(xy {x:.6f} {y:.6f})' for x,y in pts)+')))')
f.append('(model "/Users/fan/KiCad/lib/3dmodels/3rd.connector.3dshapes/XUNPU_TF-110.step" (offset (xyz 0 0 0.05)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 0)))')
f.append(')');fp=R/f'fontprints/{lib}.pretty/{name}.kicad_mod';fp.write_text('\n'.join(f)+'\n')
# Preserve legacy functional electrical identifiers for existing designs.
s=[f'(kicad_symbol_lib (version 20231120) (generator "project_library") (symbol "{name}" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)']
for k,v,y,hide in [('Reference','J',27.94,False),('Value','TF-110',24.13,False),('Footprint',lib+':'+name,0,True),('Datasheet',url,0,True),('Description','TF-110 Rev A microSD socket; switch closed without card, open with card; GND/SWB legacy identifier denotes SWB; datasheet does not specify an internal GND connection',0,True),('ki_fp_filters',lib+':'+name,0,True)]:s.append(f'(property "{k}" "{v}" (at 0 {y} 0) (effects (font (size 1.27 1.27))'+(' hide' if hide else '')+'))')
s += [f'(symbol "{name}_0_1" (rectangle (start -15.24 20.32) (end 15.24 -25.4) (stroke (width .254) (type default)) (fill (type background)))', '(polyline (pts (xy 2.54 -10.16) (xy 15.24 -10.16)) (stroke (width .254) (type default)) (fill (type none)))','(polyline (pts (xy 2.54 -20.32) (xy 15.24 -20.32)) (stroke (width .254) (type default)) (fill (type none)))','(polyline (pts (xy 2.54 -20.32) (xy 2.54 -10.16)) (stroke (width .254) (type default)) (fill (type none)))']
for y in [-10.16,-20.32]:s.append(f'(circle (center 2.54 {y}) (radius .4) (stroke (width .254) (type default)) (fill (type background)))')
for t,x,y,size in [('SWA/CD',9,-7.62,1.1),('SWB',9,-17.78,1.1),('NO CARD: CLOSED',-6,-16.51,.85),('INSERTED: OPEN',-6,-21.59,.85)]:s.append(f'(text "{t}" (at {x} {y} 0) (effects (font (size {size} {size}))))')
s.append(')');s.append(f'(symbol "{name}_1_1"')
items=[('DAT2','DAT2',-25.4,15.24,0,'passive',False),('CD/DAT3','DAT3/CD',-25.4,10.16,0,'passive',False),('CMD','CMD',-25.4,5.08,0,'passive',False),('CLK','CLK',-25.4,0,0,'passive',False),('DAT0','DAT0',-25.4,-5.08,0,'passive',False),('DAT1','DAT1',-25.4,-10.16,0,'passive',False),('VDD','VDD',25.4,15.24,180,'power_in',False),('VSS','VSS',25.4,10.16,180,'power_in',False),('SHELL','SHELL',25.4,5.08,180,'passive',False),('CD/SWA','',25.4,-10.16,180,'passive',True),('GND/SWB','',25.4,-20.32,180,'passive',True)]
for num,label,x,y,angle,typ,hide in items:s.append(f'(pin {typ} line (at {x} {y} {angle}) (length 10.16) (name "{label}" (effects (font (size 1.27 1.27))'+(' hide' if hide else '')+f')) (number "{num}" (effects (font (size 1.27 1.27)))))')
s.append(')))');(R/f'symbols/{lib}.kicad_symdir/xunpu-tf-110.kicad_sym').write_text('\n'.join(s)+'\n')
p=R/'scripts/data/library-classification.json';j=json.loads(p.read_text())
for row in j:
 if row.get('new_path')==str(fp.relative_to(R)):
  row['approved_geometry_sha256']=hashlib.sha256(fp.read_bytes()).hexdigest();row['geometry_changes']='2026-10-10 user requested redraw from TF-110 Rev A datasheet: recomputed recommended lands, keepouts and outlines, corrected normally-closed card detect symbol; legacy electrical identifiers preserved. See docs/XUNPU_TF-110_Datasheet_RevA.pdf.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
