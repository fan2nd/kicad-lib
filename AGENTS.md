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
- Place all symbol property text outside the symbol body and pin/name/number
  area, including hidden Footprint, Datasheet, Description, keywords and filters.
  Hidden fields must remain readable without overlap when "show hidden fields"
  is enabled: stack them on separate horizontal rows below the full symbol and
  visible properties, with at least 2.54 mm text-to-graphics clearance and enough
  row spacing for the font height. Do not leave metadata at the body origin.
  Preserve property values and intended visibility; move fields rather than
  deleting or shortening electrical/library identifiers to solve overlap.
- After editing `.kicad_sym`, review in KiCad or by rendered/parsed check.

## Symbol/Footprint Matching

- For all module and non-generic coreboard symbols and footprints, use functional identifiers for
  symbol pin numbers and footprint pad names (e.g. GND, VCC, SCL, SDA, SCLK,
  MOSI, RES, DC, CS), rather than arbitrary sequential numbers. Use the same
  identifier for multiple contacts on a verified common net. Apply this to new entries and requested edits; migrate existing designs separately.
  Generic interchangeable interfaces (e.g. NUCLEO ST-MORPHO and mikroBUS)
  retain their standard connector/contact numbering. GPIO identifiers use the
  port name; alternate-function labels may remain in the visible pin name.
  Keep distinct NC/unverified contacts unique (e.g. NC_5); never merge them
  merely because their display labels match. Preserve separate voltage rails.

- Symbol pin `number` fields are the electrical identifiers matched to footprint
  pad names; functional pads such as `GND`, `RX`, or `3V3` require exact
  matching symbol pin numbers.
- After pin/pad renames, verify `set(symbol_pin_numbers) == set(footprint_pad_names)`.

## Footprints

- Use `roundrect` for rectangular electrical pads, including rectangular pin-1
  through-hole pads and exposed-pad (EP) lands. Preserve intentional circular,
  oval, and non-plated mechanical holes; do not change them merely for style.
- Use `roundrect` for rectangular EP solder-paste apertures on `F.Paste` or
  `B.Paste`, including separate unnumbered window pads. Paste is distinct from
  solder mask (`F.Mask`/`B.Mask`); keep the designed paste coverage and window
  arrangement. Choose radius `min(0.25 * min(width, height), 0.25 mm)` and set
  `roundrect_rratio = radius / min(width, height)` for new conversions.
- Preserve pad numbers, centers, sizes, drills, layer membership and explicit
  mask/paste margins when rounding. Verify annular rings and pin-1 visibility.
  Document any datasheet-required shape exception. These rules apply to local
  footprints; use installed official footprints without editing their sources.
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

- For sparse, individually sized power contacts, do not treat the distance
  between remote terminals as a regular castellated-pad pitch. Size lands from
  the actual terminal geometry and required solder extension; document estimates
  and retain `_Provisional` where dimensions are unverified. MP2225GJ-Z 18x13mm
  is an approved exception: four power lands 4x2.4mm, 0.8mm out / 3.2mm in.

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

## Naming and Library Classification

- Library nicknames use lowercase dot-separated paths: `3rd.<category>` or
  `3rd.<category>.<subcategory>`. Use meaningful product categories, not vendors
  or individual part numbers. Reuse an existing category before adding one.
- Current categories are `3rd.ic`, `3rd.coreboard`, `3rd.crystal`, `3rd.module.ble`,
  `3rd.module.rf`, `3rd.module.wifi`, `3rd.module.motor`, `3rd.module.sensor`, `3rd.connector`,
  `3rd.display`, `3rd.module.display`, `3rd.module.interface`, `3rd.module.power`, `3rd.switch`, and `3rd.mechanical`.
- Classify the actual object: a bare IC belongs to `3rd.ic`; a complete core or
  development board belongs to `3rd.coreboard`; a functional module belongs to
  the applicable `3rd.module.*` library. FT232H and MCP2221A Adafruit boards are
  explicitly coreboards. Wireless coreboards also remain in `3rd.coreboard`.
- Display modules with a carrier board/headers belong to `3rd.module.display`;
  bare display panels and their FPC landing patterns remain in `3rd.display`.
- Use `symbols/<nickname>.kicad_symdir/` and
  `fontprints/<nickname>.pretty/`. Preserve the existing `fontprints` spelling.
  Symbol and footprint libraries for the same category use the same nickname;
  a category need not have both. Do not create empty libraries.

### Public Symbol and Footprint Names

- Prefer `[Vendor_]<OfficialModel>[_<Interface>][_<Variant>][_<Geometry>]`.
  Preserve official model spelling, case, digits and hyphens (e.g. `doBT-M03`,
  `E73-2G4M54LP`, `LFE5U-25F-BG256`, `TMC5160-BOB`). Use underscores between
  added fields; do not rewrite hyphens inside an official model number.
- Add a vendor only when it identifies a particular board or distinguishes
  products. When used, keep the same vendor/model stem across symbol and
  footprint; e.g. `Adafruit_FT232H`, `Waveshare_RP2350-Zero`.
- Avoid redundant category words such as `IC`, `Module` or `CoreBoard` when the
  library already conveys them, unless they are part of the official product
  name or needed to distinguish designs. Do not shorten a name so far that
  distinct pinouts or board revisions become indistinguishable.
- Retain user-approved model stems `A4988`, `TMC2209` and `TB6612` for their
  motor modules. A4988, TMC2209 and TB6612 remain unprefixed until their
  board vendors are verified. The user explicitly confirmed that the current
  TMC2209 module is not BIGTREETECH; do not restore that attribution.
  These names describe modules in `3rd.module.motor`, not bare IC footprints.
- Symbols should omit footprint-only geometry. Keep package/pinout identifiers
  when necessary to select the correct electrical part, e.g. `BG256`.
- Use explicit variant suffixes: `_Physical` for spatial symbols; `_Castellated`
  and `_PinHeader` for distinct mounting styles; `_Left`/`_Right` for handed
  parts; `_Standard`/`_Long` only for real board variants. Keep revisions only
  when they distinguish incompatible geometry or pinouts.
- Geometry fields include units: `_P2.54mm`, `_18x21mm`, `_PCB1.6mm`.
  Use decimal points and lowercase `x`; use `2x05` for row/contact counts,
  `M2` for a screw size, and `_Provisional` for estimated mechanical designs.
- Public identifiers use ASCII letters, digits, hyphens, underscores and decimal
  points; do not use whitespace, slashes, colons or Chinese text. This rule does
  not apply to readable descriptions, pin names, pin numbers or silkscreen text.

### Filenames, Values and References

- A `.kicad_mod` basename must exactly equal its internal footprint name,
  including case. Symbol files contain one top-level symbol plus its units;
  use the lowercase public symbol name with underscores converted to hyphens
  as the `.kicad_sym` basename. All current symbol filenames comply; record any future exceptions in the audit.
- Nested symbol identifiers must retain the top-level name followed by KiCad's
  `_<unit>_<style>` suffix. Keep public symbol names unique within each library.
- `Value` normally carries the public name or the official base model. Omitting
  layout/mounting/geometry suffixes from `Value` is valid (e.g. a `_Physical`
  symbol still displays the same part number). Do not treat this as a broken
  association. Legacy `fp_text value` and modern `property "Value"` are both
  valid footprint representations.
- Local `Footprint` references use `<nickname>:<exact-footprint-name>`.
  Update qualified `ki_fp_filters` too. Do not use obsolete `fontprints:` or
  `3rd:` nicknames. Preserve valid standard-library references and intentionally
  empty footprint fields. Electrical pin/pad identifiers are independent of
  public names and must never be renamed merely for naming consistency.

### Audits and Renaming

- A request to inspect naming or document rules does not itself require mass
  renaming. Record legacy style deviations and suggested names in
  `README.md`; preserve existing public identifiers during an audit.
  Apply this convention to new entries and requested renames.
- For a rename, update the filename, internal name, nested symbol identifiers,
  applicable `Value`, footprint links, qualified filters and migration records.
  Keep genuine base-model `Value` text and descriptive technical facts intact.
- For category changes, update both library tables and classification records;
  retain the KiCad default-library registration. Back up global tables before
  editing them. Do not edit unrelated existing designs or create duplicate
  compatibility libraries automatically.
- Preserve old-to-new mappings in `scripts/data/library-classification.json` (file
  moves and approved name changes) and explain public identifier migrations in
  `README.md`. Existing schematic/PCB references need separate migration.
- Run `python3 scripts/check_library_links.py` after naming changes. Export
  affected symbols/footprints with KiCad CLI; for bulk reclassification use
  `python3 scripts/check_library_links.py --export`. Check all local references,
  pin/pad matching, case-sensitive names, and unchanged geometry. Apply the
  symbol readability rules above if visible text changes.

### Verified Vendor Prefixes

- Add a missing vendor when manufacturer documentation or the user's identified
  board establishes it. Bare ICs use the IC manufacturer; complete boards and
  modules use the board vendor. Never infer module provenance from its main IC.
- Use stable verified spellings: `Adafruit`, `JLC`, `Waveshare`, `WeAct`, `ST`,
  `Maxim`, `Trinamic`, `Ebyte`, `DOIT`, `Lattice`, `CrossChip`,
  `XUNPU`, `Tag-Connect`, `Zhongjingyuan`, `DOIOT` (度云, user-confirmed
  for doBT-M03), and existing `Shouhan`. New verified IC/module vendors: `SiliconLabs`,
  `TI`, `WuhanXinyuan` (武汉芯源), `Ai-Thinker` (安信可), `Kailh` (凯华), `KZT` (凯智通), `HongCheng` (虹成电子), and `YXC` (扬兴).
  Keep original product brands Maxim and Trinamic even when documentation is
  hosted by ADI; do not alternate prefixes for the same product family.
- Keep unknown vendors and generic/custom mechanical items unprefixed. Record
  evidence and unresolved identities in `README.md`.
- A vendor prefix is part of the library identifier; visible Value text may
  remain the base model to preserve readability. Update symbol/footprint names,
  references, filters, normalized filenames and migration records together.

## Source Documents

- Keep `docs/` exclusively for original manufacturer/user-supplied source
  documents: datasheets, manuals, dimension drawings, schematics, PCB sources,
  reference images and original pinout tables. Preserve their bytes on rename.
- Name sources `[Vendor_]<OfficialModel>_<DocumentType>[_<Version>].<ext>`;
  use ASCII names, underscores between fields and lowercase extensions.
  Reuse verified vendor/model spellings above; never infer an unknown vendor.
  Use `Datasheet`, `UserManual`, `Dimensions`, `Schematic`, `PCB`, `Mounting`,
  `Pinout` or `StandardSpecification` as appropriate. Preserve source revisions.
- Do not put generated previews, working notes, backup snapshots, audit exports
  or redundant JSON into `docs/`. Store previews outside it (e.g. `/tmp`).
  Keep only script-required machine data in `scripts/data/`; record essential
  usage caveats, attribution and migration guidance in `README.md`.
- After document renames or cleanup, update script inputs and documentation
  links. Do not recreate removed JSON reports from generators.
