"""Generate the Raspberry Pi PCIe FPC interface, per specification v1.1 Fig. 1.
RX/TX names are relative to the Raspberry Pi host; mounting tabs are not FFC contacts.
"""
from pathlib import Path
import json
import math
ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://pip-assets.raspberrypi.com/categories/892-raspberry-pi-5/documents/RP-008298-DS-1-pcie-connector-standard.pdf'
PINS = ['5V', '5V', 'GND', 'PCIE_CLK_P', 'PCIE_CLK_N', 'GND',
        'PCIE_RX_P', 'PCIE_RX_N', 'GND', 'PCIE_TX_P', 'PCIE_TX_N', 'GND',
        'PCIE_PWR_EN', 'PCIE_DET_WAKE', 'PCIE_CLKREQ_N', 'PCIE_RST_B']

def build():
    name = 'RaspberryPi_PCIe_FPC_16Pin'
    pins = PINS
    g, fs = 2.54, 1.27
    ceil_grid = lambda x: math.ceil(x / g) * g
    lead = ceil_grid(len('22') * .65 * fs + g)
    width = ceil_grid(max(map(len, pins)) * .65 * fs + 2 * g)
    top, bottom = g, -len(pins) * g
    desc = ('Raspberry Pi PCIe x1 FPC/FFC interface, 16 contacts, 0.5mm pitch; '
            'RX/TX relative to Pi host; 1/2=5V; control signals 3.3V. '
            'Mechanical mounting tabs omitted; select connector footprint separately.')
    props = [('Reference', 'J', top + 2*g, False),
             ('Value', name, top + 4*g, False),
             ('Footprint', '', bottom - 2*g, True),
             ('Datasheet', SOURCE, bottom - 4*g, True),
             ('Description', desc, bottom - 6*g, True),
             ('ki_keywords', 'Raspberry Pi5 PCIe FPC FFC 16', bottom - 8*g, True)]
    out = ['(kicad_symbol_lib (version 20231120) (generator "build_raspberrypi_pcie_symbol")',
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
