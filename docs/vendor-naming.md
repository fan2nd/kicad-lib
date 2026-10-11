# 厂商前缀核对与迁移

日期：2026-10-05。已为 17 个符号和 13 个封装补充厂商／品牌前缀。Value 保留基础型号；未改变引脚、焊盘、丝印和其他图形。分类保持不变。

前缀按实际产品确定：裸 IC 使用芯片厂商，板卡／模块使用板卡品牌，不能用所搭载芯片的厂商代替。Maxim 和 Trinamic 使用原产品品牌，相关产品现由 ADI 提供资料；不同时混用 ADI、AnalogDevices 等前缀。

## 核对依据

| 前缀 | 产品 | 依据 |
| --- | --- | --- |
| `CrossChip` | CC6201ST | [原厂 CC6201 数据手册（分销商托管）](https://datasheet.lcsc.com/lcsc/1811061532_Cross-chip-CC6201ST_C285995.pdf) |
| `Lattice` | LFE5U-25F-BG256 | [原厂引脚表](https://www.latticesemi.com/view_document?document_id=50485) |
| `ST` | NUCLEO 两款符号及共用接口封装 | [ST Nucleo 系列资料](https://www.st.com/resource/en/data_brief/nucleo-c542rc.pdf)；通用 Morpho 封装仍保留通用性 |
| `Maxim` | MAX32655-FTHR | [原厂 MAX32655FTHR 数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX32655FTHR.pdf) |
| `Ebyte` | E73 LP/LX、E01C-ML01D | [E73 LX 产品页](https://www.ebyte.com/product/2770.html)、[LP 产品页](https://www.ebyte.com/product/2769.html)、[E01C 手册](https://www.ebyte.com/Uploadfiles/Files/2020-7-24/20207241550514292.pdf) |
| `DOIT` | ESPC2-01 | [原厂手册（分销商托管）](https://datasheet.lcsc.com/datasheet/pdf/af9a502314895ca31a553af62bb710df.pdf?productCode=C19949077)，页脚 Doctors of Intelligence & Technology / doit.am |
| `Trinamic` | TMC2160/4361A/5160-BOB | [2160 手册](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC2160-BOB_datasheet_Rev1.00.pdf)、[4361A 官方页](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/tmc4361a-bob.html)、[5160 手册](https://www.analog.com/media/en/technical-documentation/data-sheets/TMC5160-BOB_datasheet_rev1.10.pdf) |
| `XUNPU` | TF-110 | [原厂产品页](https://en.xunpu.com.cn/product/173.html) |
| `Tag-Connect` | TC2030-ESP/JTAG 接口符号 | [原厂 TC2030 资料](https://www.tag-connect.com/wp-content/uploads/bsk-pdf-manager/2022/06/TC2030-MCP.pdf)；前缀指连接器系列来源，不表示自定义 ESP/JTAG 引脚分配是原厂成品型号 |
| `Zhongjingyuan` | ZJY096T-IG11 | [原厂中景园手册（经销商托管）](https://www.smart-prototyping.com/image/data/2020/11/102106%200.96%20TFT%20IPS%20Bare%20Display/ZJY096T-IG11%20ST7735S%2013P%20datasheet.pdf)；本地 docs 亦保留原始手册 |

| `DOIOT` | doBT-M03 | 用户于 2026-10-05 明确确认：DOIOT（度云） |

## 未强行添加

- A4988、TB6612：现有资料不能确认所用模块的生产商，不能因芯片型号而加 Allegro 或 Toshiba。
- doBT-M03 已由用户确认厂商为 DOIOT（度云），已补上前缀。
- 两款夹板连接器封装、外壳适配板框：属于通用／自绘机械结构，没有可确认的厂商。
- 滑动开关已有 Shouhan 字段；Adafruit、JLC、Waveshare、WeAct 已有品牌，不重复添加。

## 已执行对照

| 类型 | 原名称 | 新名称 |
| --- | --- | --- |
| symbol | `TMC4361A-BOB` | [Trinamic_TMC4361A-BOB](../symbols/3rd.module.motor.kicad_symdir/trinamic-tmc4361a-bob.kicad_sym) |
| symbol | `TMC5160-BOB` | [Trinamic_TMC5160-BOB](../symbols/3rd.module.motor.kicad_symdir/trinamic-tmc5160-bob.kicad_sym) |
| symbol | `TMC2160-BOB` | [Trinamic_TMC2160-BOB](../symbols/3rd.module.motor.kicad_symdir/trinamic-tmc2160-bob.kicad_sym) |
| symbol | `ESPC2-01` | [DOIT_ESPC2-01-N2](../symbols/3rd.module.wifi.kicad_symdir/doit-espc2-01-n2.kicad_sym) |
| symbol | `LFE5U-25F-BG256` | [Lattice_LFE5U-25F-BG256](../symbols/3rd.ic.kicad_symdir/lattice-lfe5u-25f-bg256.kicad_sym) |
| symbol | `CC6201ST` | [CrossChip_CC6201ST](../symbols/3rd.ic.kicad_symdir/crosschip-cc6201st.kicad_sym) |
| symbol | `ZJY096T-IG11` | [Zhongjingyuan_ZJY096T-IG11](../symbols/3rd.display.kicad_symdir/zhongjingyuan-zjy096t-ig11.kicad_sym) |
| symbol | `E73-2G4M54LP` | [Ebyte_E73-2G4M54LP](../symbols/3rd.module.ble.kicad_symdir/ebyte-e73-2g4m54lp.kicad_sym) |
| symbol | `E73-2G4M54LP_Physical` | [Ebyte_E73-2G4M54LP_Physical](../symbols/3rd.module.ble.kicad_symdir/ebyte-e73-2g4m54lp-physical.kicad_sym) |
| symbol | `E01C-ML01D` | [Ebyte_E01C-ML01D](../symbols/3rd.module.rf.kicad_symdir/ebyte-e01c-ml01d.kicad_sym) |
| symbol | `TF-110` | [XUNPU_TF-110](../symbols/3rd.connector.kicad_symdir/xunpu-tf-110.kicad_sym) |
| symbol | `TC2030-JTAG` | [Tag-Connect_TC2030-JTAG](../symbols/3rd.connector.kicad_symdir/tag-connect-tc2030-jtag.kicad_sym) |
| symbol | `TC2030-ESP` | [Tag-Connect_TC2030-ESP](../symbols/3rd.connector.kicad_symdir/tag-connect-tc2030-esp.kicad_sym) |
| symbol | `NUCLEO-C542RC_ST-MORPHO` | [ST_NUCLEO-C542RC_ST-MORPHO](../symbols/3rd.coreboard.kicad_symdir/st-nucleo-c542rc-st-morpho.kicad_sym) |
| symbol | `MAX32655-FTHR` | [Maxim_MAX32655-FTHR](../symbols/3rd.coreboard.kicad_symdir/maxim-max32655-fthr.kicad_sym) |
| symbol | `NUCLEO-U545RE-Q_ST-MORPHO` | [ST_NUCLEO-U545RE-Q_ST-MORPHO](../symbols/3rd.coreboard.kicad_symdir/st-nucleo-u545re-q-st-morpho.kicad_sym) |
| footprint | `ZJY096T-IG11_Solder_ThroughPCB_1.6mm` | [Zhongjingyuan_ZJY096T-IG11_Solder_ThroughPCB_1.6mm](../fontprints/3rd.display.pretty/Zhongjingyuan_ZJY096T-IG11_Solder_ThroughPCB_1.6mm.kicad_mod) |
| footprint | `ZJY096T-IG11_Solder_Folded` | [Zhongjingyuan_ZJY096T-IG11_Solder_Folded](../fontprints/3rd.display.pretty/Zhongjingyuan_ZJY096T-IG11_Solder_Folded.kicad_mod) |
| footprint | `NUCLEO-ST-MORPHO` | [ST_NUCLEO-ST-MORPHO](../fontprints/3rd.coreboard.pretty/ST_NUCLEO-ST-MORPHO.kicad_mod) |
| footprint | `MAX32655-FTHR` | [Maxim_MAX32655-FTHR](../fontprints/3rd.coreboard.pretty/Maxim_MAX32655-FTHR.kicad_mod) |
| footprint | `TF-110` | [XUNPU_TF-110](../fontprints/3rd.connector.pretty/XUNPU_TF-110.kicad_mod) |
| footprint | `TMC2160-BOB` | [Trinamic_TMC2160-BOB](../fontprints/3rd.module.motor.pretty/Trinamic_TMC2160-BOB.kicad_mod) |
| footprint | `TMC5160-BOB` | [Trinamic_TMC5160-BOB](../fontprints/3rd.module.motor.pretty/Trinamic_TMC5160-BOB.kicad_mod) |
| footprint | `TMC4361A-BOB` | [Trinamic_TMC4361A-BOB](../fontprints/3rd.module.motor.pretty/Trinamic_TMC4361A-BOB.kicad_mod) |
| footprint | `E73-2G4M54LX` | [Ebyte_E73-2G4M54LX](../fontprints/3rd.module.ble.pretty/Ebyte_E73-2G4M54LX.kicad_mod) |
| footprint | `E73-2G4M54LP` | [Ebyte_E73-2G4M54LP](../fontprints/3rd.module.ble.pretty/Ebyte_E73-2G4M54LP.kicad_mod) |
| footprint | `E01C-ML01D` | [Ebyte_E01C-ML01D](../fontprints/3rd.module.rf.pretty/Ebyte_E01C-ML01D.kicad_mod) |
| footprint | `ESPC2-01` | [DOIT_ESPC2-01-N2](../fontprints/3rd.module.wifi.pretty/DOIT_ESPC2-01-N2.kicad_mod) |

已验证：全部 29 个符号文件、31 个封装成功导出；25 组本地符号／封装关联一致。旧设计中的库标识需要按以上映射单独迁移。

追加迁移：符号和封装 `doBT-M03` → `DOIOT_doBT-M03`。

用户纠正：当前 TMC2209 模块不是 BIGTREETECH，已撤回两项厂商更名，符号及封装均恢复为 `TMC2209`；描述中厂商名和符号中的对应厂商 Datasheet 链接已移除。历史参考资料不代表该模块的厂商归属。

## 新增器件厂商

- `SiliconLabs`：CP2102C，Silicon Labs 官方数据手册。
- `TI`：DRV8311H、DRV8837DSGR，Texas Instruments 官方数据手册。
- `WuhanXinyuan`：CW32L012C8U6，武汉芯源官方产品页及手册。
- `Ai-Thinker`：NF-03，安信可官方 NF 系列规格书与封装库。

来源链接及验证记录见 [新增器件核对记录](new-parts-2026-10-05.md)。

2026-10-05：用户确认完整型号为 ESPC2-01-N2；符号与封装现名均为 `DOIT_ESPC2-01-N2`（原 `DOIT_ESPC2-01`），Value 同步为 `ESPC2-01-N2`。引脚编号和封装几何未改变。

2026-10-05 新增已确认厂商 `Kailh`（凯华）：`3rd.switch:Kailh_PG1350`、`3rd.switch:Kailh_PG1353` 符号及对应 `_Solder` 封装。命名、引脚对应、导出检查通过；尺寸来源见 [凯华轴体记录](kailh-choc.md)。当前全库 37 个符号、37 个封装。

2026-10-05：新增 `KZT_SOP8_Narrow` 符号及 `KZT_SOP8_Narrow_20x14.4mm` 封装，分类 `3rd.connector`。厂商凯智通由用户确认，`KZT` 为其公开品牌缩写；完整料号未提供，保留描述性名称。[绘制依据](kzt-sop8.md)。

2026-10-05 更新：KZT 烧录座按用户要求使用 `150mil`、`208mil`、`295mil` 后缀，公开符号/封装名为 `KZT_SOP8_150mil`、`KZT_SOP8_208mil`、`KZT_SOP8_295mil`。原 Narrow 名称已迁移至 150mil，当前共 40 个符号、40 个封装。详见 [尺寸记录](kzt-sop8.md)。

2026-10-05：虹成 DC 座补齐厂商前缀 `HongCheng`，符号和封装现名 `HongCheng_HC-DC-044-2.5-03B`。依据厂商手册“深圳市虹成电子有限公司”、立创商品 C55014014 的 HC(虹成电子) 品牌及 LCSC 英文 Hong Cheng 名称。原厂型号 HC-DC-044-2.5-03B 完整保留，Value 保留基础型号；文件名、内部名、嵌套单元、封装字段和筛选条件同步更新。

2026-10-09: VL53L0X_4Plus2 sensor module: board vendor unknown from the user photograph. No ST prefix: ST identifies the sensor IC, not the module manufacturer.

2026-10-09: SHT3x-DIS_4Plus2 is an unbranded sensor module; no Sensirion prefix is inferred from the sensor manufacturer. The footprint is marked Provisional for photograph-derived dimensions.

2026-10-09：mikroBUS 为标准接口，新增条目不加具体板卡厂商前缀；Socket/Module 区分底座与模块，S/M/L 区分官方板框尺寸，归入 `3rd.connector`。
