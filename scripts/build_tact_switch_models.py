"""Build footprints from datasheets; clean and align original LCSC STEP models.

Run with FreeCAD's Python, with its Resources/lib on PYTHONPATH.
VRML uses KiCad's 0.1 inch units; STEP and FCStd use mm. Z=0 is seating plane.
"""
import json
from pathlib import Path
import FreeCAD as App
import Part
import Import

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '3dmodels/3rd.switch.3dshapes'
OUT.mkdir(parents=True, exist_ok=True)
SPECS = [
    # name, body Y, terminal span, PCB outer span, base/cover height, LCSC
    ('XUNPU_TS-1089S-02526', 3.25, 5.1, 5.5, 1.7, 'C455282'),
    ('Shouhan_TS3425BA', 3.2, 4.6, 5.2, 1.8, 'C2681476'),
]

def box(w, d, h, z=0, x=0, y=0):
    return Part.makeBox(w, d, h, App.Vector(x-w/2, y-d/2, z))

def rounded(w, d, h, z, radius):
    shape = box(w, d, h, z)
    vertical = [e for e in shape.Edges if abs(e.Vertexes[-1].Point.z-e.Vertexes[0].Point.z) > h-.001]
    return shape.makeFillet(radius, vertical)

def capsule(w, d, h, z):
    r = d/2
    s = box(w-d, d, h, z)
    for x in [-(w-d)/2, (w-d)/2]:
        s = s.fuse(Part.makeCylinder(r,h,App.Vector(x,0,z)))
    return s.removeSplitter()

for name, depth, span, landspan, top, lcsc in SPECS:
    doc = App.newDocument(name.replace('-','_'))
    parts = []
    def add(label, shape, color):
        assert shape.isValid() and shape.Volume > 0, label
        ob = doc.addObject('PartDesign::Feature',label)
        ob.Shape = shape
        ob.addProperty('App::PropertyColor','ModelColor').ModelColor = color
        parts.append((ob,color))
    source = Part.Shape()
    source.read(str(ROOT/'docs'/(name+'_Model_LCSC.step')))
    original = source.copy()
    if name.startswith('Shouhan'):
        # Raised bottom lettering only; do not trim the -0.01 mm terminal feet.
        tool = Part.makeBox(1.5,.4,.03,App.Vector(-.7,.4,-.03))
        source = source.cut(tool).removeSplitter()
        shift = .01
    else:
        # Fill recessed bottom lettering, keeping the three mechanical recesses.
        fill = Part.makeBox(1.3,.6,.13,App.Vector(-.55,-1.43,-1.7))
        source = source.fuse(fill).removeSplitter()
        # Side logo is raised 0.001 mm above the x=2.09 body wall.
        tool = Part.makeBox(.02,1.5,.5,App.Vector(2.09,-.8,-.88))
        source = source.cut(tool).removeSplitter()
        shift = 1.7
    assert source.isValid()
    # Geometry outside the three logo regions must remain original.
    removed = original.cut(source)
    added = source.cut(original)
    print(name, 'removed/filled volume', removed.Volume, added.Volume)
    transform = App.Matrix()
    transform.move(App.Vector(0,0,shift))
    source = source.transformGeometry(transform)
    add('LCSC_NoLogo',source,(.8,.8,.78))
    doc.recompute()
    doc.saveAs(str(OUT/(name+'.FCStd')))
    Import.export([p[0] for p in parts],str(OUT/(name+'.step')))
    mesh=[]
    vrml=['#VRML V2.0 utf8']
    for ob,color in parts:
        vertices,faces=ob.Shape.tessellate(.025)
        xyz=[[v.x,v.y,v.z] for v in vertices]
        mesh.append({'name':ob.Label,'color':color,'vertices':xyz,'faces':faces})
        coords=',\n'.join(' '.join(f'{v/2.54:.7f}' for v in pt) for pt in xyz)
        idx=',\n'.join(' '.join(map(str,f))+' -1' for f in faces)
        vrml.append('Shape { appearance Appearance { material Material { diffuseColor %s } } geometry IndexedFaceSet { solid TRUE coord Coordinate { point [%s] } coordIndex [%s] } }'%(' '.join(map(str,color)),coords,idx))
    (OUT/(name+'.wrl')).write_text('\n'.join(vrml)+'\n')
    Path('/tmp/'+name+'-mesh.json').write_text(json.dumps(mesh))
    check=Part.Shape();check.read(str(OUT/(name+'.step')))
    assert check.isValid()
    bb=check.BoundBox
    print("bounds",bb)
    assert abs(bb.ZMin)<1e-4
    assert abs(bb.ZMax-(2.51 if name.startswith('Shouhan') else 2.5))<1e-5
    print(name,'STEP envelope',bb.XLength,bb.YLength,bb.ZLength)
    App.closeDocument(doc.Name)

    lines=[f'(footprint "{name}" (version 20241229) (generator "project_library") (layer "F.Cu") (attr smd)',
      f'(descr "{lcsc}; manufacturer recommended land pattern; top row pads share pin 1; bottom row pads share pin 2; normally open between rows; compatible with Switch:SW_Push.")',
      '(tags "tactile switch push button SPST NO")',
      '(fp_text reference "REF**" (at 0 -2.5) (layer "F.SilkS") (effects (font (size .8 .8) (thickness .12))))',
      f'(fp_text value "{name}" (at 0 2.7) (layer "F.Fab") (effects (font (size .8 .8) (thickness .12))))']
    def line(x1,y1,x2,y2,layer,width):
        lines.append(f'(fp_line (start {x1} {y1}) (end {x2} {y2}) (stroke (width {width}) (type solid)) (layer "{layer}"))')
    def rect(x,y,layer,width):
        for a,b in [((-x,-y),(x,-y)),((x,-y),(x,y)),((x,y),(-x,y)),((-x,y),(-x,-y))]:line(*a,*b,layer,width)
    rect(2.1,depth/2,'F.Fab',.1)
    rect(landspan/2+.25,depth/2+.25,'F.CrtYd',.05)
    # Continuous top/bottom body contour; side strokes stop clear of solder mask.
    for y in [-depth/2-.1,depth/2+.1]:line(-2.1,y,2.1,y,'F.SilkS',.12)
    for x in [-2.2,2.2]:line(x,-.45,x,.45,'F.SilkS',.12)
    # Oval actuator as two lines and true semicircular arcs.
    for layer,width in [('F.Fab',.1),('F.SilkS',.12)]:
        line(-.4,-1.1,.4,-1.1,layer,width);line(-.4,1.1,.4,1.1,layer,width)
        for sign in [-1,1]:
            lines.append(f'(fp_arc (start {sign*.4} -1.1) (mid {sign*1.5} 0) (end {sign*.4} 1.1) (stroke (width {width}) (type solid)) (layer "{layer}"))')
    # Manufacturer drawing provides outer and inner pad edges.
    w=(landspan-3.1)/2;h=(2.8-1.5)/2;x=(landspan+3.1)/4;y=(2.8+1.5)/4
    for n,px,py in [(1,-x,-y),(1,x,-y),(2,-x,y),(2,x,y)]:
        lines.append(f'(pad "{n}" smd roundrect (at {px:.6f} {py:.6f}) (size {w:.6f} {h:.6f}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio .25))')
    # WRL supplies colors in viewer; matching STEP is used by KiCad STEP export.
    lines.append(f'(model "{OUT/name}.wrl" (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz 0 0 0)))')
    lines.append(')')
    (ROOT/'fontprints/3rd.switch.pretty'/(name+'.kicad_mod')).write_text('\n'.join(lines)+'\n')
