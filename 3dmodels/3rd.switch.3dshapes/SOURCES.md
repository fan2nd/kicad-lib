# Keyswitch 3D model sources

Added 2026-10-23. No footprint pad/hole geometry changed.

- `SW_Kailh_Choc_V1.wrl`, `SW_Cherry_MX_PCB.wrl`,
  `SW_Hotswap_Kailh_MX.wrl`, `SW_Hotswap_Kailh_Choc_V1.wrl`:
  https://github.com/kiswitch/kiswitch/tree/main/library/3dmodels/3d-library.3dshapes
  Original files retained byte-for-byte. Distributed under the project's MIT option;
  notice in `licenses/KiSwitch-MIT.txt`.

## Placement

PG1350 switch and socket are rotated 180 degrees around Z to match the local
LED-north footprint: contact holes at (0, +5.9), (-5, +3.8) in PCB coordinates.
The hot-swap footprint holes use (+5.95 / +3.75) Y as documented in README;
the source socket is an assembly reference and retains its original geometry.
MX switch/socket have zero rotation and offset. KiCad PCB Y is the
opposite of model Cartesian Y. Sockets already include a negative Z placement
for approximately 1.6 mm PCB thickness; do not flip them or add another -1.6 mm.
Other PCB thicknesses require revisiting socket model placement.

MX uses the **generic Cherry MX PCB switch** model as an interchangeable
assembly illustration, not an exact Kailh variant. The socket is the Kailh
MX hot-swap model. Source socket terminal extents differ slightly from the
local manufacturer-drawing lands; local lands are deliberately unchanged.
All four KiSwitch assets are VRML meshes, not STEP solids.
