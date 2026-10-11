# 命名检查记录

检查日期：2026-10-05。范围：10 个分类、29 个符号文件、31 个封装。已按用户确认实施全部 15 项建议更名：11 个符号、4 个封装。

## 检查结论

- 31 个封装文件名与内部名称完全一致。
- 29 个符号的顶层名称和全部单元名称结构正确，库内无重名，名称字符合法。
- 25 个本地封装引用有效，符号引脚与焊盘编号完全一致。外部标准库引用与有意留空的封装字段保留。
- 全部 29 个符号文件名符合“公开名称转小写、下划线转连字符”的规则，Waveshare 前缀已统一。
- 原 13 项风格差异及 2 项可选简称均已处理，无待处理的建议项。
- 已核对现代 `property "Value"` 和旧式 `fp_text value`。Value 仅显示基础型号的情况是允许的，无须机械地改成完整库名称。

## 已执行更名对照

以下全部已实施。已有设计的旧库标识需按表中对照另行迁移；本次没有修改其他项目。

| 原名称 | 现名称 | 原因 |
| --- | --- | --- |
| `JLC-DiQiXing-RA6E2` | `JLC_DiQiXing-RA6E2` | 厂商字段与型号用下划线分隔 |
| `JLC-DiWenXing-CW32F030C8T6` | `JLC_DiWenXing-CW32F030C8T6` | 厂商字段与型号用下划线分隔 |
| `WeAct-STM32G431CBT6_Standard` | `WeAct_STM32G431CBT6_Standard` | 厂商字段分隔符 |
| `WeAct-STM32G431CBU6_Standard` | `WeAct_STM32G431CBU6_Standard` | 厂商字段分隔符 |
| `NUCLEO-C542RC-ST-MORPHO` | `NUCLEO-C542RC_ST-MORPHO` | 板卡型号与接口范围分隔 |
| `NUCLEO-U545RE-Q-ST-MORPHO` | `NUCLEO-U545RE-Q_ST-MORPHO` | 板卡型号与接口范围分隔 |
| `ESP32-C5-Zero` | `Waveshare_ESP32-C5-Zero` | 与文件、封装的厂商前缀统一 |
| `ESP32-H2-Zero` | `Waveshare_ESP32-H2-Zero` | 与文件、封装的厂商前缀统一 |
| `RP2350-Zero` | `Waveshare_RP2350-Zero` | 与文件、封装的厂商前缀统一 |
| `A4988-STEPSTICK` | `A4988` | 与已确认的封装简称统一 |
| `TMC2209-STEPSTICK` | `TMC2209` | 与已确认的封装简称统一 |
| `JLC-DiQiXing-RA6E2_P2.54` | `JLC_DiQiXing-RA6E2_P2.54mm` | 厂商字段分隔符；节距补 mm |
| `JLC-DiWenXing-CW32F030C8T6_P2.54` | `JLC_DiWenXing-CW32F030C8T6_P2.54mm` | 厂商字段分隔符；节距补 mm |
| `WeAct-STM32G431CoreBoard_Standard_P2.54` | `WeAct_STM32G431CoreBoard_Standard_P2.54mm` | 厂商字段分隔符；节距补 mm；保留实际板型标识 |
| `Enclosure_JTAG_50x50_M2_IDC20_Provisional` | `Enclosure_JTAG_50x50mm_M2_IDC20_Provisional` | 外形尺寸补 mm；估算状态必须保留 |

## 有意保留的命名

- `doBT-M03` 的大小写、`TMC*-BOB` 和官方型号中的连字符保留。
- `E73-2G4M54LP_Physical` 与普通符号代表相同器件，Value 同为 `E73-2G4M54LP` 合理。
- `LFE5U-25F-BG256` 中的容量和封装后缀决定球位定义，不应缩成 `LFE5U`。
- `Castellated`、`PinHeader`、`Folded`、`ThroughPCB_1.6mm`、`Left`、`Right` 区分实际安装方式，不能省略。现有 `ThroughPCB_1.6mm` 作为明确带单位的历史写法保留。
- `NUCLEO-ST-MORPHO` 是共用接口封装，不绑定某颗 MCU；继续保留通用名。
- `A4988`、`TMC2209`、`TB6612` 为用户已确认的模块封装简称；类别已明确其并非裸 IC。
- `Provisional` 表示估算结构，不能因追求简短而删除。
- `fontprints` 为既有目录名，继续保留；它不再用作库昵称。

## 厂商前缀更新

随后已核实并补充 30 项有效厂商前缀（17 个符号、13 个封装；TMC2209 的两项厂商命名已撤回），依据和迁移对照见 [厂商命名记录](vendor-naming.md)。上方 15 项对照是前一轮历史记录，下方为当前名称。

## 完整清单

| 类型 | 分类 | 当前公开名称 | 结果 |
| --- | --- | --- | --- |
| 符号 | `3rd.connector` | [Tag-Connect_TC2030-ESP](../symbols/3rd.connector.kicad_symdir/tag-connect-tc2030-esp.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.connector` | [Tag-Connect_TC2030-JTAG](../symbols/3rd.connector.kicad_symdir/tag-connect-tc2030-jtag.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.connector` | [XUNPU_TF-110](../symbols/3rd.connector.kicad_symdir/xunpu-tf-110.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [Adafruit_FT232H](../symbols/3rd.coreboard.kicad_symdir/adafruit-ft232h.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [Adafruit_MCP2221A](../symbols/3rd.coreboard.kicad_symdir/adafruit-mcp2221a.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [JLC_DiQiXing-RA6E2](../symbols/3rd.coreboard.kicad_symdir/jlc-diqixing-ra6e2.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [JLC_DiWenXing-CW32F030C8T6](../symbols/3rd.coreboard.kicad_symdir/jlc-diwenxing-cw32f030c8t6.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [Maxim_MAX32655-FTHR](../symbols/3rd.coreboard.kicad_symdir/maxim-max32655-fthr.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [ST_NUCLEO-C542RC_ST-MORPHO](../symbols/3rd.coreboard.kicad_symdir/st-nucleo-c542rc-st-morpho.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [ST_NUCLEO-U545RE-Q_ST-MORPHO](../symbols/3rd.coreboard.kicad_symdir/st-nucleo-u545re-q-st-morpho.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [Waveshare_ESP32-C5-Zero](../symbols/3rd.coreboard.kicad_symdir/waveshare-esp32-c5-zero.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [Waveshare_ESP32-H2-Zero](../symbols/3rd.coreboard.kicad_symdir/waveshare-esp32-h2-zero.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [Waveshare_RP2350-Zero](../symbols/3rd.coreboard.kicad_symdir/waveshare-rp2350-zero.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [WeAct_STM32G431CBT6_Standard](../symbols/3rd.coreboard.kicad_symdir/weact-stm32g431cbt6-standard.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.coreboard` | [WeAct_STM32G431CBU6_Standard](../symbols/3rd.coreboard.kicad_symdir/weact-stm32g431cbu6-standard.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.display` | [Zhongjingyuan_ZJY096T-IG11](../symbols/3rd.display.kicad_symdir/zhongjingyuan-zjy096t-ig11.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.ic` | [CrossChip_CC6201ST](../symbols/3rd.ic.kicad_symdir/crosschip-cc6201st.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.ic` | [Lattice_LFE5U-25F-BG256](../symbols/3rd.ic.kicad_symdir/lattice-lfe5u-25f-bg256.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.ble` | [DOIOT_doBT-M03](../symbols/3rd.module.ble.kicad_symdir/doiot-dobt-m03.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.ble` | [Ebyte_E73-2G4M54LP_Physical](../symbols/3rd.module.ble.kicad_symdir/ebyte-e73-2g4m54lp-physical.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.ble` | [Ebyte_E73-2G4M54LP](../symbols/3rd.module.ble.kicad_symdir/ebyte-e73-2g4m54lp.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.motor` | [A4988](../symbols/3rd.module.motor.kicad_symdir/a4988.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.motor` | [TMC2209](../symbols/3rd.module.motor.kicad_symdir/tmc2209.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.motor` | [TB6612](../symbols/3rd.module.motor.kicad_symdir/tb6612.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.motor` | [Trinamic_TMC2160-BOB](../symbols/3rd.module.motor.kicad_symdir/trinamic-tmc2160-bob.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.motor` | [Trinamic_TMC4361A-BOB](../symbols/3rd.module.motor.kicad_symdir/trinamic-tmc4361a-bob.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.motor` | [Trinamic_TMC5160-BOB](../symbols/3rd.module.motor.kicad_symdir/trinamic-tmc5160-bob.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.rf` | [Ebyte_E01C-ML01D](../symbols/3rd.module.rf.kicad_symdir/ebyte-e01c-ml01d.kicad_sym) | 符合／有依据保留 |
| 符号 | `3rd.module.wifi` | [DOIT_ESPC2-01-N2](../symbols/3rd.module.wifi.kicad_symdir/doit-espc2-01-n2.kicad_sym) | 符合／有依据保留 |
| 封装 | `3rd.connector` | [PinHeaderSocket_2x05_P2.00mm_ClampBoard_PCB_Left](../fontprints/3rd.connector.pretty/PinHeaderSocket_2x05_P2.00mm_ClampBoard_PCB_Left.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.connector` | [PinHeaderSocket_2x05_P2.00mm_ClampBoard_PCB_Right](../fontprints/3rd.connector.pretty/PinHeaderSocket_2x05_P2.00mm_ClampBoard_PCB_Right.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.connector` | [XUNPU_TF-110](../fontprints/3rd.connector.pretty/XUNPU_TF-110.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Adafruit_FT232H](../fontprints/3rd.coreboard.pretty/Adafruit_FT232H.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Adafruit_MCP2221A](../fontprints/3rd.coreboard.pretty/Adafruit_MCP2221A.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [JLC_DiQiXing-RA6E2_P2.54mm](../fontprints/3rd.coreboard.pretty/JLC_DiQiXing-RA6E2_P2.54mm.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [JLC_DiWenXing-CW32F030C8T6_P2.54mm](../fontprints/3rd.coreboard.pretty/JLC_DiWenXing-CW32F030C8T6_P2.54mm.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Maxim_MAX32655-FTHR](../fontprints/3rd.coreboard.pretty/Maxim_MAX32655-FTHR.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [ST_NUCLEO-ST-MORPHO](../fontprints/3rd.coreboard.pretty/ST_NUCLEO-ST-MORPHO.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Waveshare_ESP32-C5-Zero_Castellated](../fontprints/3rd.coreboard.pretty/Waveshare_ESP32-C5-Zero_Castellated.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Waveshare_ESP32-C5-Zero_PinHeader](../fontprints/3rd.coreboard.pretty/Waveshare_ESP32-C5-Zero_PinHeader.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Waveshare_ESP32-H2-Zero_Castellated](../fontprints/3rd.coreboard.pretty/Waveshare_ESP32-H2-Zero_Castellated.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Waveshare_ESP32-H2-Zero_PinHeader](../fontprints/3rd.coreboard.pretty/Waveshare_ESP32-H2-Zero_PinHeader.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Waveshare_RP2350-Zero_Castellated](../fontprints/3rd.coreboard.pretty/Waveshare_RP2350-Zero_Castellated.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [Waveshare_RP2350-Zero_PinHeader](../fontprints/3rd.coreboard.pretty/Waveshare_RP2350-Zero_PinHeader.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.coreboard` | [WeAct_STM32G431CoreBoard_Standard_P2.54mm](../fontprints/3rd.coreboard.pretty/WeAct_STM32G431CoreBoard_Standard_P2.54mm.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.display` | [Zhongjingyuan_ZJY096T-IG11_Solder_Folded](../fontprints/3rd.display.pretty/Zhongjingyuan_ZJY096T-IG11_Solder_Folded.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.display` | [Zhongjingyuan_ZJY096T-IG11_Solder_ThroughPCB_1.6mm](../fontprints/3rd.display.pretty/Zhongjingyuan_ZJY096T-IG11_Solder_ThroughPCB_1.6mm.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.mechanical` | [Enclosure_JTAG_50x50mm_M2_IDC20_Provisional](../fontprints/3rd.mechanical.pretty/Enclosure_JTAG_50x50mm_M2_IDC20_Provisional.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.ble` | [Ebyte_E73-2G4M54LP](../fontprints/3rd.module.ble.pretty/Ebyte_E73-2G4M54LP.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.ble` | [Ebyte_E73-2G4M54LX](../fontprints/3rd.module.ble.pretty/Ebyte_E73-2G4M54LX.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.ble` | [DOIOT_doBT-M03](../fontprints/3rd.module.ble.pretty/DOIOT_doBT-M03.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.motor` | [A4988](../fontprints/3rd.module.motor.pretty/A4988.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.motor` | [TMC2209](../fontprints/3rd.module.motor.pretty/TMC2209.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.motor` | [TB6612](../fontprints/3rd.module.motor.pretty/TB6612.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.motor` | [Trinamic_TMC2160-BOB](../fontprints/3rd.module.motor.pretty/Trinamic_TMC2160-BOB.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.motor` | [Trinamic_TMC4361A-BOB](../fontprints/3rd.module.motor.pretty/Trinamic_TMC4361A-BOB.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.motor` | [Trinamic_TMC5160-BOB](../fontprints/3rd.module.motor.pretty/Trinamic_TMC5160-BOB.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.rf` | [Ebyte_E01C-ML01D](../fontprints/3rd.module.rf.pretty/Ebyte_E01C-ML01D.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.module.wifi` | [DOIT_ESPC2-01-N2](../fontprints/3rd.module.wifi.pretty/DOIT_ESPC2-01-N2.kicad_mod) | 符合／有依据保留 |
| 封装 | `3rd.switch` | [SW_SPDT_Shouhan_MSK12CO2](../fontprints/3rd.switch.pretty/SW_SPDT_Shouhan_MSK12CO2.kicad_mod) | 符合／有依据保留 |

## 2026-10-05 新增器件

新增 6 个符号和 4 个封装；当前共 35 个符号、35 个封装，29 个本地符号—封装引用。新增项文件名、内部名称、单元名称和引脚/焊盘匹配已检查。上文计数为更名操作当时的历史快照。

- `symbols/3rd.ic.kicad_symdir/siliconlabs-cp2102c-gqfn24.kicad_sym`
- `symbols/3rd.ic.kicad_symdir/siliconlabs-cp2102c-gqfn28.kicad_sym`
- `symbols/3rd.ic.kicad_symdir/ti-drv8311h.kicad_sym`
- `symbols/3rd.ic.kicad_symdir/ti-drv8837dsgr.kicad_sym`
- `symbols/3rd.ic.kicad_symdir/wuhanxinyuan-cw32l012c8u6.kicad_sym`
- `symbols/3rd.module.rf.kicad_symdir/ai-thinker-nf-03.kicad_sym`
- `fontprints/3rd.ic.pretty/SiliconLabs_CP2102C-GQFN24.kicad_mod`
- `fontprints/3rd.ic.pretty/SiliconLabs_CP2102C-GQFN28.kicad_mod`
- `fontprints/3rd.ic.pretty/TI_DRV8837DSGR.kicad_mod`
- `fontprints/3rd.module.rf.pretty/Ai-Thinker_NF-03_Castellated.kicad_mod`

2026-10-05：用户确认完整型号为 ESPC2-01-N2；符号与封装现名均为 `DOIT_ESPC2-01-N2`（原 `DOIT_ESPC2-01`），Value 同步为 `ESPC2-01-N2`。引脚编号和封装几何未改变。

2026-10-05 新增已确认厂商 `Kailh`（凯华）：`3rd.switch:Kailh_PG1350`、`3rd.switch:Kailh_PG1353` 符号及对应 `_Solder` 封装。命名、引脚对应、导出检查通过；尺寸来源见 [凯华轴体记录](kailh-choc.md)。当前全库 37 个符号、37 个封装。

2026-10-05：新增 `KZT_SOP8_Narrow` 符号及 `KZT_SOP8_Narrow_20x14.4mm` 封装，分类 `3rd.connector`。厂商凯智通由用户确认，`KZT` 为其公开品牌缩写；完整料号未提供，保留描述性名称。[绘制依据](kzt-sop8.md)。

2026-10-05 更新：KZT 烧录座按用户要求使用 `150mil`、`208mil`、`295mil` 后缀，公开符号/封装名为 `KZT_SOP8_150mil`、`KZT_SOP8_208mil`、`KZT_SOP8_295mil`。原 Narrow 名称已迁移至 150mil，当前共 40 个符号、40 个封装。详见 [尺寸记录](kzt-sop8.md)。

2026-10-05 后续去重：已删除本地 CP2102C-GQFN24、DRV8311H、DRV8837DSGR 三个重复符号，改用官方库符号。本地封装保留。上文含历史创建记录；当前符号清单以实际目录为准。详见 [对比记录](official-library-comparison.md)。

2026-10-05：虹成 DC 座补齐厂商前缀 `HongCheng`，符号和封装现名 `HongCheng_HC-DC-044-2.5-03B`。依据厂商手册“深圳市虹成电子有限公司”、立创商品 C55014014 的 HC(虹成电子) 品牌及 LCSC 英文 Hong Cheng 名称。原厂型号 HC-DC-044-2.5-03B 完整保留，Value 保留基础型号；文件名、内部名、嵌套单元、封装字段和筛选条件同步更新。

DC 座封装按用户确认改为通用名 `DC-044_5521_5525_Horizontal`，不带单一厂商／内针直径料号；符号保留 `HongCheng_HC-DC-044-2.5-03B`。

DC 座封装按官方 `BarrelJack_CUI_PJ-079BH_Horizontal` 的命名格式调整：`3rd.connector:DC-044_5521_5525_Horizontal` → `3rd.connector:BarrelJack_DC-044_Horizontal`。5521／5525 兼容信息保留于描述；符号型号及焊盘几何不变。

2026-10-09: Added 3rd.module.sensor:VL53L0X_4Plus2 and VL53L0X_4Plus2_PinHeader_P2.54mm_13x10mm_Provisional. 4Plus2 distinguishes this board pinout from single-row breakouts. Provisional marks photograph-derived mechanical offsets and row-spacing estimate.

2026-10-09: SHT3x-DIS_4Plus2 is an unbranded sensor module; no Sensirion prefix is inferred from the sensor manufacturer. The footprint is marked Provisional for photograph-derived dimensions.

2026-10-09：mikroBUS 为标准接口，新增条目不加具体板卡厂商前缀；Socket/Module 区分底座与模块，S/M/L 区分官方板框尺寸，归入 `3rd.connector`。

2026-10-09：按用户要求，mikroBUS 底座增加 S/M/L 变体；原 `mikroBUS_Socket_2x08_P2.54mm` 更名为 `mikroBUS_Socket_S_2x08_P2.54mm`，另增 M/L，焊盘几何不变。
