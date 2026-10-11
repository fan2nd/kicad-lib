# 第三方 KiCad 符号与封装库

按器件实际形态和用途分类。符号采用 KiCad 10 的 `.kicad_symdir` 目录库，封装采用 `.pretty` 库；库昵称与目录名保持一致。

| 库名称 | 内容 | 符号文件 | 封装 |
| --- | --- | ---: | ---: |
| `3rd.ic` | 独立芯片符号：CC6201ST、LFE5U-25F、CP2102C QFN28、CW32L012；使用官方 IC 封装 | 4 | 0 |
| `3rd.coreboard` | 核心板、开发板和扩展板接口：JLC、NUCLEO、WeAct、Waveshare、MAX32655、FT232H、MCP2221A | 12 | 13 |
| `3rd.module.ble` | 蓝牙模块：E73、doBT-M03（含双模蓝牙） | 3 | 3 |
| `3rd.module.rf` | 2.4 GHz 射频模块：E01C-ML01D、NF-03 | 2 | 2 |
| `3rd.module.wifi` | Wi-Fi/BLE 无线模块：ESPC2-01-N2 | 1 | 1 |
| `3rd.module.sensor` | 传感器模块：VL53L0X、SHT3x-DIS 4+2 排针板 | 2 | 2 |
| `3rd.module.motor` | 电机驱动及运动控制模块：A4988、TB6612、TMC 系列 | 6 | 6 |
| `3rd.connector` | TF 卡座、Tag-Connect 接口、夹板连接器、KZT SOP8 三种烧录座、HC DC 座、mikroBUS 接口 | 9 | 13 |
| `3rd.display` | ZJY096T 裸屏及两种排线安装封装 | 1 | 2 |
| `3rd.switch` | 单刀双掷滑动开关、Kailh Choc V1/V2 轴体 | 2 | 3 |
| `3rd.mechanical` | 外壳适配板框、安装结构 | 0 | 1 |

核心板按整体板卡分类，即使带 Wi-Fi 或 BLE，也归入 `3rd.coreboard`；小型无线模组按主要通信功能分类。裸 IC 与采用该 IC 的功能板分开。

## 目录和库注册

- `symbols/<库名称>.kicad_symdir/`：每个文件保存一个符号及其全部单元。
- `fontprints/<库名称>.pretty/`：封装。保留原有 `fontprints` 目录拼写。
- 根目录 `sym-lib-table`、`fp-lib-table`：项目级注册表，使用 `${KIPRJMOD}` 相对路径。放在本目录中的 KiCad 项目可直接使用。
- 其他项目可在“管理符号库／管理封装库”中添加所需库，昵称应与上表一致；符号的封装引用使用这些昵称。

## 迁移说明

原 `3rd.kicad_symdir` 与 `3rd.pretty` 已拆分。符号名、引脚定义、封装名、焊盘及图形保持原样，仅更新库位置、封装引用和封装筛选条件。

同时修复两条原有失效引用：`A4988-STEPSTICK-2x8` → `3rd.module.motor:A4988`、`TMC2209-STEPSTICK-2x8` → `3rd.module.motor:TMC2209`。原 `fontprints:` 引用全部替换为对应的新库昵称；标准库引用保留。

已有原理图／PCB 中保存的旧库标识不会随本库自动变化。需要从库更新旧项目时，应将旧 `3rd:<符号名>`、`3rd:<封装名>` 或 `fontprints:<封装名>` 映射到对应新昵称。完整文件迁移清单见 `scripts/data/library-classification.json`。

## 验证

运行 `python3 scripts/check_library_links.py --export`，检查分类表、封装引用、符号引脚与封装焊盘一致性，并调用 KiCad 导出全部库文件。初次分类后全部 29 个符号文件、31 个封装通过检查。

TB6612 模块的符号与封装现统一命名为 `TB6612`，库标识为 `3rd.module.motor:TB6612`；原符号 `TB6612FNG-MODULE` 和封装 `TB6612FNG-Module_18x21_P2.54` 已更名。

## 命名规范

命名、分类及迁移规则见 [AGENTS.md](AGENTS.md#naming-and-library-classification)。本次全量检查结果、历史差异和建议名称见 命名检查记录（历史记录见 Git）。

2026-10-05 已实施命名检查中的全部 15 项建议（11 个符号、4 个封装），包括 A4988/TMC2209 符号简称、厂商前缀及尺寸单位统一。详见 Git 中的历史记录 的已执行对照表和 Git 中的历史记录。

已进一步为 17 个符号、13 个封装保留已确认的厂商前缀。当前名称、来源及未确认项见 厂商命名记录（历史记录见 Git）。此前更名表属于迁移历史，当前完整清单以 Git 中的历史记录 为准；Value 可保留基础型号。

TMC2209 模块经用户确认不是 BIGTREETECH，已恢复无厂商前缀的 `3rd.module.motor:TMC2209`，不再据历史参考手册推断模块生产商。

2026-10-05 新增 CP2102C 两种 QFN 符号及推荐焊盘封装、DRV8311H 符号、CW32L012C8U6 符号、DRV8837DSGR 符号与封装、Ai-Thinker NF-03 符号与半孔封装。当前共 35 个符号、35 个封装。尺寸依据和使用注意见 新增器件核对记录（历史记录见 Git）。

型号补全：`3rd.module.wifi:DOIT_ESPC2-01` → `3rd.module.wifi:DOIT_ESPC2-01-N2`，同时用于符号与封装；既有设计如需更新，须迁移旧库引用。

2026-10-05 新增凯华 Choc V1（PG1350）与 V2（PG1353）直接焊接符号及封装，见 尺寸与验证记录（历史记录见 Git）。全库现有 37 个符号和 37 个封装。

新增 `KZT_SOP8_Narrow` 符号与 `KZT_SOP8_Narrow_20x14.4mm` 封装；尺寸记录（历史记录见 Git）。宽体及 295mil 已按用户后续指定的中线加宽规则完成。当前共 38 个符号、38 个封装。

KZT 烧录座现统一为 `KZT_SOP8_150mil`、`KZT_SOP8_208mil`、`KZT_SOP8_295mil`（符号和封装同名，位于 `3rd.connector`）。旧 `KZT_SOP8_Narrow` 符号和 `KZT_SOP8_Narrow_20x14.4mm` 封装迁移至 `KZT_SOP8_150mil`；已有设计需更新引用。当前共 40 个符号、40 个封装。

已按用户要求删除官方库已有的 3 个符号，改用 `Interface_USB:CP2102C-Axx-xQFN24`、`Driver_Motor:DRV8311H`、`Driver_Motor:DRV8837`。当时保留对应本地封装，后续已按以下记录删除。旧原理图中的符号需按 重复项对比记录（历史记录见 Git） 另行迁移；未改动其他设计。

2026-10-05 按用户确认删除 CP2102C QFN24、CP2102C QFN28、DRV8837DSGR 三个重复封装，改用官方封装，替代标识见上述对比记录。CP2102C QFN28 本地符号的封装字段与筛选条件已更新。空的 `3rd.ic.pretty` 及其项目／全局注册已移除，`3rd.ic` 符号库保留。已有 PCB 中的封装需另行更新。当前共 37 个符号、37 个封装。

同时将 22 个本地封装中的 57 个矩形焊盘改为圆角矩形，保留编号、中心、尺寸、孔径、层和其余图形；圆形／椭圆形焊盘保留。焊盘和 EP 锡膏开口规则已加入 AGENTS.md，检查脚本检查矩形焊盘遗漏和圆角参数。变更记录见 焊盘检查记录（历史记录见 Git）。官方源文件未修改。

新增 `3rd.connector:HongCheng_HC-DC-044-2.5-03B` 符号和封装，按用户最终选型替换本次尚未发布的 03A 草稿。内部关系及尺寸来源见 DC 座核对记录（历史记录见 Git）。当前共 38 个符号、38 个封装。

命名修正：符号及封装 `3rd.connector:HC-DC-044-2.5-03B` → `3rd.connector:HongCheng_HC-DC-044-2.5-03B`，补齐虹成厂商前缀；Value 保留原厂型号。已有设计如使用旧标识，需更新库链接；引脚和几何未变。

按用户确认，DC 座封装通用于 5521／5525，封装标识 `3rd.connector:HongCheng_HC-DC-044-2.5-03B` → `3rd.connector:DC-044_5521_5525_Horizontal`。保留 DC-044 系列及卧式结构标识，避免误用于其他脚位的 5521／5525 座。具体器件符号名称不变，关联与筛选字段已同步更新。

DC 座封装按官方 `BarrelJack_CUI_PJ-079BH_Horizontal` 的命名格式调整：`3rd.connector:DC-044_5521_5525_Horizontal` → `3rd.connector:BarrelJack_DC-044_Horizontal`。5521／5525 兼容信息保留于描述；符号型号及焊盘几何不变。

新增 `3rd.module.sensor:VL53L0X_4Plus2`，关联 `VL53L0X_4Plus2_PinHeader_P2.54mm_13x10mm_Provisional`。未知板厂不冠以 ST 厂商名；传感器模块分类独立于裸芯片。排针列距按照片推算为 10.16 mm；安装孔仅作装配参考，不在底板自动钻孔。见 尺寸记录（历史记录见 Git）。

新增 `3rd.module.sensor:SHT3x-DIS_4Plus2` 符号与对应 `_PinHeader_P2.54mm_13x10mm_Provisional` 封装；根据正反面照片核对 ALERT/ADDR，板形及列距为估算。详见 SHT3x 模块记录（历史记录见 Git）。

2026-10-09：新增 mikroBUS 底座与模块接口符号、底座封装及 S/M/L 模块板框，均位于 `3rd.connector`。尺寸、方向和使用方法见 mikroBUS 说明（历史记录见 Git）。当前共 42 个符号、44 个封装。

2026-10-09：mikroBUS 封装文字统一横向；底座拆为 S/M/L 三种占位尺寸。旧 `3rd.connector:mikroBUS_Socket_2x08_P2.54mm` → `3rd.connector:mikroBUS_Socket_S_2x08_P2.54mm`，另增 M/L；符号默认关联 S 型并允许筛选三种规格，已有设计需更新旧引用。当前共 42 个符号、46 个封装。

2026-10-10：mikroBUS 按官方 v2.00 手册修订丝印，加入从 PDF 提取的完整 Logo、开口底座轮廓及模块正面竖排／背面横排标注。S/M/L 底座统一接口丝印，模块投影及空间预留按尺寸区分；实际板名、NC 与多底座编号由具体设计填写，见 规范核对记录（历史记录见 Git）。

2026-10-10：`3rd.connector:XUNPU_TF-110` 按原厂 Rev A 手册重绘符号与推荐焊盘，修正检测开关未插卡闭合状态、右上内侧壳焊盘位置、SWA 宽度等尺寸，并补顶层禁布区。名称及功能电气标识不变；已有 PCB 更新后需检查走线与禁布区。见 TF-110 核对记录（历史记录见 Git）。

## 原始资料与数据

`docs/` 仅保留原始资料，文件名统一为 `[厂商_]<型号>_<资料类型>[_版本].扩展名`；整理时只改名称，保留原文件内容。生成预览、过程笔记、备份及重复 JSON 已移除，历史内容可从 Git 查阅。脚本必需的迁移表和 mikroBUS Logo 轮廓数据保留在 `scripts/data/`。

Adafruit PCB 原文件来源：[MCP2221](https://github.com/adafruit/Adafruit-MCP2221-PCB)、[FT232H](https://github.com/adafruit/Adafruit-FT232H-Breakout-PCB)。Designed by Limor Fried/Ladyada for Adafruit Industries. Adafruit invests time and resources providing this open source design; please support Adafruit and open-source hardware by purchasing products from Adafruit. 原始文件及派生几何遵循源仓库 Creative Commons Attribution/Share-Alike 条款。两块核心板当前 USB 朝上，安装孔圆仅作位置参考，载板需自行添加实际安装孔。

TF-110 3D 模型来源于 LCSC C266613 的 EasyEDA 配套模型，UUID `6f3af1915f434bde9fc3a32e8e3a97c0`；按用户要求去除独立标识实体。模型关联 Z 偏移 +0.05 mm，当前使用本机绝对路径，迁移库时需更新。TF-110 的历史电气编号 `GND/SWB` 仅代表 SWB 开关端，不能据此认定内部接地；规则域为用户指定的中央矩形简化范围。
