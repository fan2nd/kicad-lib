# Project Rules

KiCad symbol/footprint library. Keep symbols readable and footprint geometry
computed, layer-correct, and verifiable.

## Symbols

- Visible `Reference`, `Value`, properties, pin names, and pin numbers must not
  overlap and must remain readable.
- Use enough body width, pin rows, and pin lead length for opposite-side labels.
- Before visual review, use `g = 2.54 mm`, `char_w = 0.65 * font_size_x`,
  `text_w(s) = len(s) * char_w`, `ceil_grid(x) = ceil(x / g) * g`.
- Visible pin numbers require `lead_length >= ceil_grid(text_w(pin_number) + g)`;
  connector-qualified numbers such as `CN7-38` or `J10-12` must fit outside the
  symbol body.
- Opposite-side pin names require
  `body_width >= ceil_grid(max_left_pin_name_w + max_right_pin_name_w + 2*g)`;
  use `0` for a side with no pin names.
- Keep text at least one practical grid step (`2.54 mm`) from rectangles, lines,
  arcs, and other graphics when possible.
- After editing `.kicad_sym`, review in KiCad or by rendered/parsed check.

## Symbol/Footprint Matching

- Symbol pin `number` fields are the electrical identifiers matched to footprint
  pad names; functional pads such as `GND`, `RX`, or `3V3` require exact
  matching symbol pin numbers.
- After pin/pad renames, verify `set(symbol_pin_numbers) == set(footprint_pad_names)`.

## Footprints

- Draw board outlines, cutouts, notches, and protrusions from datasheet/manual
  dimensions; compute coordinates and do not eyeball offsets.
- Actual carrier-PCB edges, slots, cutouts, and mechanically cut features go on
  `Edge.Cuts`; module placement/assembly outlines use silk/fab as specified.
- Connector/socket silk goes on the physical mounting side: bottom-mounted
  female headers/sockets on `B.SilkS`, top-mounted modules/headers on `F.SilkS`.
- Verify orientation with a named corner pin when available; e.g. lower-right
  `CN10-38` means pad ordering and orientation must match.
- Keep castellated/module-pad and pin-header variants separate unless explicitly
  requested.
- Model carrier-board footprints with the module above the carrier unless the
  user asks otherwise.
- After editing `.kicad_mod`, run KiCad CLI export or equivalent rendered check
  for parsing and intended layers.

## Castellated Pads

- SMD pads must extend past the module outline without running too far under it.
- Via/no-via is based on the original module board's castellated-hole style, not
  whether the carrier footprint uses SMD pads.
- For each pad along the outward normal: `pitch = center-to-center spacing`,
  `c = dot(pad_center - board_edge, outward_normal)` with outside positive,
  `w_n = pad_size_n`, `p_out = w_n / 2 + c`, `p_in = w_n / 2 - c`.
- Standard formulas: with original via/through-hole, `p_in = 0.8 * pitch`;
  without via, `p_in = 0.4 * pitch`; always `p_out = 0.2 * pitch`,
  `w_n = p_in + p_out`, `c = (p_out - p_in) / 2`.
- Derived values: no via gives `w_n = 0.6 * pitch`, `c = -0.1 * pitch`;
  via gives `w_n = 1.0 * pitch`, `c = -0.3 * pitch`.
- Tangential width is `w_t = 0.5 * pitch` unless the datasheet says otherwise.
- Measure outward normals and inside/outside lengths relative to the module
  board outline.
