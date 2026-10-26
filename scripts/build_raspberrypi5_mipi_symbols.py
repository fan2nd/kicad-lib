"""Pi 5 CAM/DISP 22-contact interfaces; numbers are FPC contacts, not GPIO IDs.

Source: https://www.raspberrypi.com/documentation/accessories/camera.html
Pi 5 combined ports: https://www.raspberrypi.com/documentation/computers/sbcs.html
Both uses retain the same physical D-PHY lanes and auxiliary contacts.
"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://www.raspberrypi.com/documentation/accessories/camera.html'
PINS = ['GND', 'D0_N', 'D0_P', 'GND', 'D1_N', 'D1_P', 'GND',
        'CLK_N', 'CLK_P', 'GND', 'D2_N', 'D2_P', 'GND', 'D3_N',
        'D3_P', 'GND', 'CAM_IO0', 'CAM_IO1', 'GND', 'SCL', 'SDA', '3V3']


def build(interface, legacy=False):
    name = f'RaspberryPi_{interface}_15Pin' if legacy else 'RaspberryPi_MIPI_22Pin'
    pins = PINS
    if legacy:
        pins = (PINS[:10] + ['CAM_IO0', 'CAM_IO1', 'SCL', 'SDA', '3V3']
                if interface == 'CSI' else
                ['GND', 'D1_N', 'D1_P', 'GND', 'CLK_N', 'CLK_P', 'GND',
                 'D0_N', 'D0_P', 'GND', 'SCL', 'SDA', 'GND', '3V3', '3V3'])
    g, fs = 2.54, 1.27
    ceil_grid = lambda x: math.ceil(x / g) * g
    lead = ceil_grid(len('22') * .65 * fs + g)
    width = ceil_grid(max(map(len, pins)) * .65 * fs + 2 * g)
    top, bottom = g, -len(pins) * g
    desc = ('Raspberry Pi 5 CAM/DISP0 or CAM/DISP1, combined CSI/DSI interface, '
            '22 contacts, 0.5mm pitch, 4 D-PHY lanes; numeric contact numbering; '
            'CAM_IO0/1 are auxiliary GPIO, not grounds. Select footprint separately.')
    source = SOURCE
    if legacy:
        desc = (f'Raspberry Pi legacy {interface} interface, 15 contacts, 1mm pitch, '
                '2 D-PHY lanes; numeric contact numbering; CSI and DSI are NOT pin-compatible.')
        if interface == 'DSI':
            source = 'https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-reduced-schematics.pdf'
    props = [('Reference', 'J', top + 2*g, False),
             ('Value', name, top + 4*g, False),
             ('Footprint', '', bottom - 2*g, True),
             ('Datasheet', source, bottom - 4*g, True),
             ('Description', desc, bottom - 6*g, True),
             ('ki_keywords', f'Raspberry Pi CSI DSI MIPI CAM DISP FPC {len(pins)}', bottom - 8*g, True)]
    out = ['(kicad_symbol_lib (version 20231120) (generator "build_raspberrypi5_mipi_symbols")',
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
    print(build('CSI_DSI').relative_to(ROOT))
    for interface in ('CSI', 'DSI'):
        print(build(interface, legacy=True).relative_to(ROOT))
