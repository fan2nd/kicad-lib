"""Clean local original LCSC STEP files; FreeCAD Python required."""
from pathlib import Path
import json
import FreeCAD as A
import Part,Import
R=Path(__file__).resolve().parents[1];out=R/'3dmodels/3rd.connector.3dshapes'
for part,dy,dz,si in [('C34',-6.05,-.55,5),('C225',-13.6,-2.24,4),('C345',-13.15,-3.45,4)]:
 name='HongCheng_HC-USB3.0-'+part+'-P'
 raw=Part.Shape();raw.read(str(R/'docs'/(name+'_Model_LCSC.step')));solids=list(raw.Solids);old=solids[si]
 if part=='C34':
  tool=Part.makeBox(4.6,1.7,.03,A.Vector(-2.3,2.1,2.85))
 else:
  tool=Part.makeBox(.03,2.8,.85,A.Vector(6.55,.3,3.85))
 before=old.Volume
 solids[si]=old.cut(tool).removeSplitter()
 assert solids[si].isValid() and abs(before-solids[si].Volume)<.1
 print(part,'logo volume removed',before-solids[si].Volume)
 d=A.newDocument(part);objects=[];vr=['#VRML V2.0 utf8'];mesh=[]
 for i,shape in enumerate(solids):
  m=A.Matrix();m.move(A.Vector(0,dy,dz));shape=shape.transformGeometry(m)
  assert shape.isValid()
  o=d.addObject('PartDesign::Feature','Part%d'%i);o.Shape=shape;objects.append(o)
  color=(.72,.75,.78) if i==si else ((.05,.23,.65) if i>=4 else (.85,.69,.3))
  o.addProperty('App::PropertyColor','ModelColor').ModelColor=color
  vs,fs=shape.tessellate(.035);xyz=[[v.x,v.y,v.z] for v in vs]
  mesh.append(dict(color=color,vertices=xyz,faces=fs))
  coords=','.join(' '.join(str(t/2.54) for t in v) for v in xyz);indices=','.join(' '.join(map(str,f))+' -1' for f in fs)
  vr.append('Shape { appearance Appearance { material Material { diffuseColor %s } } geometry IndexedFaceSet { solid TRUE coord Coordinate { point [%s] } coordIndex [%s] } }'%(' '.join(map(str,color)),coords,indices))
 d.recompute();d.saveAs(str(out/(name+'.FCStd')));Import.export(objects,str(out/(name+'.step')))
 (out/(name+'.wrl')).write_text('\n'.join(vr)+'\n');Path('/tmp/'+name+'-mesh.json').write_text(json.dumps(mesh))
 s=Part.Shape();s.read(str(out/(name+'.step')));assert s.isValid();print(part,s.BoundBox)
 A.closeDocument(d.Name)
