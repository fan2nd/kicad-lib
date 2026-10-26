"""Generate the standard Grove_IIC interface symbol; numeric connector contacts."""
from pathlib import Path
import json
import math
ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://wiki.seeedstudio.com/Grove_System/'
PINS = ['SCL', 'SDA', 'VCC', 'GND']

def build():
    name = 'Grove_IIC'
    pins = PINS
    g, fs = 2.54, 1.27
    ceil_grid = lambda x: math.ceil(x / g) * g
    lead = ceil_grid(len(str(len(pins))) * .65 * fs + g)
    width = ceil_grid(max(map(len, pins)) * .65 * fs + 2 * g)
    top, bottom = g, -len(pins) * g
    desc = 'Grove_IIC I2C interface, 4-pin 2mm; 1=SCL, 2=SDA, 3=VCC, 4=GND; VCC depends on system (3.3V or 5V). Select connector footprint separately.'
    props = [('Reference', 'J', top + 2*g, False),
             ('Value', name, top + 4*g, False),
             ('Footprint', '', bottom - 2*g, True),
             ('Datasheet', SOURCE, bottom - 4*g, True),
             ('Description', desc, bottom - 6*g, True),
             ('ki_keywords', 'Grove_IIC I2C 4pin 2mm VCC', bottom - 8*g, True)]
    out = ['(kicad_symbol_lib (version 20231120) (generator "build_grove_iic_symbol")',
           f'(symbol "{name}" (pin_names (offset 1.27)) (in_bom yes) (on_board yes)']
    for key, value, y, hide in props:
        out.append(f'(property {json.dumps(key)} {json.dumps(value)} (at {width/2:g} {y:g} 0) '
                   f'(effects (font (size {fs} {fs})) {"hide" if hide else ""}))')
    out.append(f'(symbol "{name}_0_1" (rectangle (start 0 {top:g}) (end {width:g} {bottom:g}) '
               '(stroke (width 0.254) (type default)) (fill (type background))))')
    out.append(f'(symbol "{name}_1_1"')
    for number, label in enumerate(pins, 1):
        out.append(f'(pin passive line (at {width+lead:g} {-(number-1)*g:g} 180) (length {lead:g}) '
                   f'(name "{label}" (effects (font (size {fs} {fs})))) '
                   f'(number "{number}" (effects (font (size {fs} {fs})))))')
    out.append(')))')
    path = ROOT / 'symbols/3rd.connector.kicad_symdir' / (name.lower().replace('_', '-') + '.kicad_sym')
    path.write_text('\n'.join(out) + '\n')
    return path


if __name__ == '__main__':
    print(build().relative_to(ROOT))
