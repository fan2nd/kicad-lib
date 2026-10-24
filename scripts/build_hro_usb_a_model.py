"""Clean C530628 LCSC STEP logo regions and align to HRO_U-A-24DS-W-1.
Run with FreeCAD Python. Original downloaded STEP remains unchanged in docs/.
"""
from pathlib import Path
import json
import FreeCAD as A
import Part,Import
ROOT=Path(__file__).resolve().parents[1]
name='HRO_U-A-24DS-W-1'
out=ROOT/'3dmodels/3rd.connector.3dshapes'
s=Part.Shape();s.read(str(ROOT/'docs'/(name+'_Model_LCSC.step')))
assert len(s.Solids)==10
shell=s.Solids[9]
# Raised side lettering, x=6.525 support plane.
shell=shell.cut(Part.makeBox(.02,1.3,3.9,A.Vector(6.525,.65,-1.95)))
print("after side",shell.Volume)
# Bottom lettering in the small central region; preserve all spring apertures.
shell=shell.fuse(Part.makeBox(2.2,.6,.15,A.Vector(-1.2,2,-2.85)))
print("after fill",shell.Volume)
shell=shell.cut(Part.makeBox(2.2,.6,.05,A.Vector(-1.2,2,-2.9))).removeSplitter()
print("after bottom",shell.Volume)
assert shell.isValid() and shell.Volume>90
assert abs(s.Solids[9].Volume-shell.Volume)<.01
print('Shell net volume change',shell.Volume-s.Solids[9].Volume)
parts=[];mesh=[];vrml=['#VRML V2.0 utf8']
d=A.newDocument('HRO_USB_A')
for i,shape in enumerate(list(s.Solids[:9])+[shell]):
 # Front housing at KiCad Y=+10.25; rear shell tabs at Y=0.
 # KiCad model Y is opposite footprint Y. Tail bottom z=-1.24 -> PCB z=0.
 m=A.Matrix();m.move(A.Vector(0,-10.25,1.24));shape=shape.transformGeometry(m)
 assert shape.isValid()
 ob=d.addObject('PartDesign::Feature','Part%d'%i);ob.Shape=shape;parts.append(ob)
 color=(.1,.1,.1) if i==4 else ((.72,.74,.77) if i==9 else (.83,.68,.3))
 ob.addProperty('App::PropertyColor','ModelColor').ModelColor=color
 vs,fs=shape.tessellate(.04);xyz=[[v.x,v.y,v.z] for v in vs]
 mesh.append(dict(color=color,vertices=xyz,faces=fs))
 coords=','.join(' '.join(str(t/2.54) for t in v) for v in xyz)
 faces=','.join(' '.join(map(str,f))+' -1' for f in fs)
 vrml.append('Shape { appearance Appearance { material Material { diffuseColor %s } } geometry IndexedFaceSet { solid TRUE coord Coordinate { point [%s] } coordIndex [%s] } }'%(' '.join(map(str,color)),coords,faces))
 if 5<=i<=8:assert abs(shape.BoundBox.ZMin)<1e-5
out.mkdir(exist_ok=True,parents=True);d.recompute()
d.saveAs(str(out/(name+'.FCStd')));Import.export(parts,str(out/(name+'.step')))
(out/(name+'.wrl')).write_text('\n'.join(vrml)+'\n')
Path('/tmp/'+name+'-mesh.json').write_text(json.dumps(mesh))
check=Part.Shape();check.read(str(out/(name+'.step')));assert check.isValid()
print('Final bbox',check.BoundBox)
A.closeDocument(d.Name)
