# 第三方 KiCad 符号与封装库

按器件实际形态和用途分类。符号采用 KiCad 10 的 `.kicad_symdir` 目录库，封装采用 `.pretty` 库；库昵称与目录名保持一致。

## 待检查清单

- [ ] `Trinamic_TMC4361A-BOB`：核对模块实际引脚顺序、功能与当前符号引脚编号／封装焊盘名的对应关系，复核数字编号迁移为功能编号的映射。
- [ ] `Trinamic_TMC2160-BOB`：核对模块实际引脚顺序、功能与当前符号引脚编号／封装焊盘名的对应关系，复核数字编号迁移为功能编号的映射。

以上项目尚未完成核实；符号与封装的编号集合一致性检查不代表物理引脚映射已经确认。

SSD1306 OLED 模块迁入 `3rd.module.display`，裸屏仍在 `3rd.display`。按用户确认的控制器型号命名，未由外观推断板厂或更改控制器。`SSD1306_I2C_128x64` 配套 0.96 寸 27.3×27.8 mm 封装；`SSD1306_SPI_128x64` 配套 0.96 寸 27.3×27.8 mm。符号引脚编号和封装焊盘名采用功能标识：I2C 为 GND/VCC/SCL/SDA；SPI 为 GND/VCC/SCLK/MOSI/RES/DC/CS，显示面朝上、排针在上方时从左至右。板上 D0/D1 对应 SCLK/MOSI。


0.96 寸封装已按新图纸校正：[I2C](docs/SSD1306_I2C_128x64_0.96inch_Dimensions.png)、[SPI](docs/SSD1306_SPI_128x64_0.96inch_Dimensions.png)。两者板体 27.30×27.80 mm，安装孔径 2 mm、横距 23.30 mm；I2C 安装孔纵距 **23.90 mm**，SPI 为 **23.80 mm**。两者上排安装孔距顶边 2 mm；I2C 下排 y=12.0 mm，SPI 下排 y=11.9 mm（板中心为原点）。排针距顶边 1.50 mm，首针距左边 I2C=9.84 mm、SPI=6.03 mm，节距均为 2.54 mm。玻璃 26.70×19.26 mm，距左边 0.30 mm、距顶边 4.27 mm；显示区 I2C 按图为 21.74×10.86 mm，SPI 按参数表为 21.744×10.864 mm。缺口宽 14 mm，深度按图中与下排安装孔中心对齐推导 I2C=1.9 mm、SPI=2.0 mm（未单独标注深度）。SPI 移除 `_Provisional`。底板排针焊盘为 1.8 mm、钻孔 1 mm，GND 首脚圆角矩形，功能丝印水平排在板内。

迁移：SSD1306 的符号与封装库前缀 `3rd.display:` → `3rd.module.display:`，已有设计须更新引用；SPI 旧带 `_Provisional` 名称迁至同名无该后缀封装。项目库表和分类记录同步更新，不复制旧分类兼容库。

ADS1115 最新尺寸覆盖：按用户指定，两个安装版本均采用 BMP280 的 **15×12 mm** 板体及对应焊盘几何；排针列距仍为 12.70 mm，贴片焊盘列中心改为 ±6.738 mm。旧 `ZY-ADS1115_*_14x11mm_Provisional` 迁至 `ZY-ADS1115_*_15x12mm_Provisional`。本次按专用模块规则同步将符号编号/焊盘名改为 VCC、GND、SCL、SDA、AIN0～AIN3，已有设计需更新映射，详细编号映射 1→VCC、2→GND、3→SCL、4→SDA、5→AIN3、6→AIN2、7→AIN1、8→AIN0。先前照片 14×11 mm 及其比例估算仅作历史记录，以用户最新指定为准。

MAX30102 模块：新增 `3rd.module.sensor:MH-ET-LIVE_MAX30102`，默认排针封装，另提供独立半孔贴片版。板厂前缀按用户照片 MH-ET LIVE 标识及其 [官方代码仓库](https://github.com/MHEtLive/MH-ET-LIVE-max30102) 确定。以用户第二张尺寸图的元件面为方向（不是第一张大图元件面的方向，两者相差 180°）：上排左至右 VIN/SDA/SCL/GND 编为 1/2/3/4；下排左至右 GND/RD/IRD/INT 编为 5/6/7/8，模块编号由本库定义。背面文字已翻面对应，不直接照搬背面左右关系。

名义本体 20×15 mm，排针孔中心 x=±3.81/±1.27 mm、y=±5.08 mm（节距 2.54 mm、排距 10.16 mm）；底板通孔焊盘 1.8 mm、钻孔 1 mm。半孔贴片版按有孔规则取 1.27×2.54 mm 焊盘，y=±6.738 mm，内伸 2.032 mm、外伸 0.508 mm。照片估算 R2 mm 板角、四孔中心 (±6.1,±6.1) mm/直径 1.5 mm、侧槽中心 x=±8.7 mm/1.2×9.5 mm；孔槽及中央器件仅画在 F.Fab 作装配参考，不在底板生成钻孔或 Edge.Cuts，也不将侧槽擅自接地。未标注尺寸和实物公差待核对，封装保留 `_Provisional`。

RD/IRD 保留板上名称并设为 passive，内部网络未核实，不按 LED 驱动输出接线；[MAX30102 原厂手册](https://www.analog.com/media/en/technical-documentation/data-sheets/max30102.pdf) 的芯片引脚表没有 RD/IRD，不能套用 MAX30100 的引脚功能。INT 为开漏低有效。原始图片：[正反面](docs/MH-ET-LIVE_MAX30102_Pinout.jpg)、[尺寸](docs/MH-ET-LIVE_MAX30102_Dimensions.jpg)。

NF-03 辅助焊点：`Ai-Thinker_NF-03_Castellated` 右侧辅助 GND 焊盘按用户指定为 1.3×1.3 mm 圆角贴片焊盘（F.Cu/F.Mask/F.Paste），复用 2 号 GND。保持右边缘贴齐 12 mm 模块板边 x=6 mm，因此底板焊盘中心为 (5.35, -2.532) mm。原模块孔中心按手册为 (5.081, -2.532) mm；底板焊盘中心相对孔中心向右偏移 0.269 mm。丝印保留 0.2 mm 铜皮间距，天线禁布区局部留出 0.25 mm 间距，底板不新增钻孔。

新增传感器模块：`ZY-MPU6050`、`ZY-BMP280`、`ZY-ADS1115`，各提供独立的 `_PinHeader` 与 `_Castellated` 封装，符号默认关联排针版。未知板厂不增加厂商前缀。三者均以元件面为准，左上向下为 1=VCC、2=GND、3=SCL、4=SDA；右上向下编号为 8、7、6、5。MPU6050 右侧依次 INT、AUX_DA、AUX_CL、AD0；BMP280 为 3V3、GND、SDO、NC；ADS1115 为 AIN0、AIN1、AIN2、AIN3。MPU6050 丝印 DA/CL 对应 AUX_DA/AUX_CL。BMP280 的 3V3 是板载稳压器输出，NC 保持无连接类型，不作为额外 SPI 接口。

MPU6050/BMP280 板体 15×12 mm，ADS1115 为 14×11 mm。纵向节距 2.54 mm；列距按照片和整倍数条件推定为 12.70 mm，排针中心 x=±6.35、y=±3.81/±1.27 mm。排针焊盘直径 1.8 mm、钻孔 1.0 mm 为常用排针设计值。贴片版按有孔边缘触点计算：内伸 2.032 mm、外伸 0.508 mm、焊盘 2.54×1.27 mm；15 mm 宽板中心 x=±6.738，14 mm 宽板中心 x=±6.238 mm。模块位于底板上方，外形在 F.Fab/F.SilkS，无 Edge.Cuts；采用尺寸图矩形包络，不虚构未标注的边缘缺口。图中标注手工测量有误差，排距、孔径适配与边缘触点位置需实物核对，保留 `_Provisional`。

原始资料：[MPU6050 正反面](docs/ZY-MPU6050_Pinout.jpg)、[MPU6050 原理图及尺寸](docs/ZY-MPU6050_Dimensions.jpg)、[BMP280 原理图及尺寸](docs/ZY-BMP280_Dimensions.jpg)、[ADS1115 原理图及尺寸](docs/ZY-ADS1115_Dimensions.jpg)。

2026-10-14 复核排针版：ADS1115 照片的左右孔中心跨度约 438 px，纵向单节距约 87.3 px，比例约 5.02；BMP280 分别约 313 px、62 px，比例约 5.05。以已知 2.54 mm 纵向节距标定，估计列距分别约 12.74 mm、12.82 mm，均支持 12.70 mm（5×2.54）设计值。图像比例与标注的手测整数板宽有偏差，故这是照片估算而非精密尺寸确认，继续保留 Provisional。三个排针版丝印改为闭合框，侧边位于 x=±7.6 mm，与通孔铜皮净距 0.29 mm；该丝印是外扩的放置包络，F.Fab 保留真实名义板体 15×12 / 14×11 mm。通孔孔位、孔径、焊盘尺寸与电气编号保持不变，贴片版丝印不变。

| 库名称 | 内容 | 符号文件 | 封装 |
| --- | --- | ---: | ---: |
| `3rd.crystal` | YXC 有源振荡器及无源晶体；2520/3225 本地封装 | 3 | 4 |
| `3rd.ic` | 独立芯片符号：CC6201ST、LFE5U-25F、CP2102C QFN28、CW32L012；使用官方 IC 封装 | 4 | 0 |
| `3rd.coreboard` | 核心板、开发板和扩展板接口：JLC、NUCLEO、WeAct、Waveshare、MAX32655、FT232H、MCP2221A | 12 | 13 |
| `3rd.module.ble` | 蓝牙模块：E73、doBT-M03（含双模蓝牙） | 3 | 3 |
| `3rd.module.rf` | 2.4 GHz 射频模块：E01C-ML01D、NF-03 | 2 | 2 |
| `3rd.module.wifi` | Wi-Fi/BLE 无线模块：ESPC2-01-N2 | 1 | 1 |
| `3rd.module.sensor` | 传感器与采集模块：VL53L0X、GY-SHT3x、ZY-MPU6050、BMP280、ADS1115、MAX30102 | 6 | 10 |
| `3rd.module.motor` | 电机驱动及运动控制模块：A4988、TB6612、TMC 系列 | 6 | 6 |
| `3rd.connector` | TF 卡座、Tag-Connect 接口、夹板连接器、KZT SOP8 三种烧录座、HC DC 座、mikroBUS 接口 | 9 | 13 |
| `3rd.display` | ZJY096T 裸屏及两种排线安装封装 | 1 | 2 |
| `3rd.module.display` | SSD1306 I2C/SPI OLED 模块，1.3/0.96 寸 | 2 | 3 |
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

KZT 烧录座现统一为 `KZT_SOP8_150mil`、`KZT_SOP8_208mil`、`KZT_SOP8_295mil`（符号和封装同名，位于 `3rd.connector`）。旧 `KZT_SOP8_Narrow` 符号和 `KZT_SOP8_Narrow_20x14.4mm` 封装迁移至 `KZT_SOP8_150mil`；已有设计需更新引用。当前共 43 个符号、49 个封装。

已按用户要求删除官方库已有的 3 个符号，改用 `Interface_USB:CP2102C-Axx-xQFN24`、`Driver_Motor:DRV8311H`、`Driver_Motor:DRV8837`。当时保留对应本地封装，后续已按以下记录删除。旧原理图中的符号需按 重复项对比记录（历史记录见 Git） 另行迁移；未改动其他设计。

2026-10-05 按用户确认删除 CP2102C QFN24、CP2102C QFN28、DRV8837DSGR 三个重复封装，改用官方封装，替代标识见上述对比记录。CP2102C QFN28 本地符号的封装字段与筛选条件已更新。空的 `3rd.ic.pretty` 及其项目／全局注册已移除，`3rd.ic` 符号库保留。已有 PCB 中的封装需另行更新。当前共 37 个符号、37 个封装。

同时将 22 个本地封装中的 57 个矩形焊盘改为圆角矩形，保留编号、中心、尺寸、孔径、层和其余图形；圆形／椭圆形焊盘保留。焊盘和 EP 锡膏开口规则已加入 AGENTS.md，检查脚本检查矩形焊盘遗漏和圆角参数。变更记录见 焊盘检查记录（历史记录见 Git）。官方源文件未修改。

新增 `3rd.connector:HongCheng_HC-DC-044-2.5-03B` 符号和封装，按用户最终选型替换本次尚未发布的 03A 草稿。内部关系及尺寸来源见 DC 座核对记录（历史记录见 Git）。当前共 38 个符号、38 个封装。

命名修正：符号及封装 `3rd.connector:HC-DC-044-2.5-03B` → `3rd.connector:HongCheng_HC-DC-044-2.5-03B`，补齐虹成厂商前缀；Value 保留原厂型号。已有设计如使用旧标识，需更新库链接；引脚和几何未变。

按用户确认，DC 座封装通用于 5521／5525，封装标识 `3rd.connector:HongCheng_HC-DC-044-2.5-03B` → `3rd.connector:DC-044_5521_5525_Horizontal`。保留 DC-044 系列及卧式结构标识，避免误用于其他脚位的 5521／5525 座。具体器件符号名称不变，关联与筛选字段已同步更新。

DC 座封装按官方 `BarrelJack_CUI_PJ-079BH_Horizontal` 的命名格式调整：`3rd.connector:DC-044_5521_5525_Horizontal` → `3rd.connector:BarrelJack_DC-044_Horizontal`。5521／5525 兼容信息保留于描述；符号型号及焊盘几何不变。

新增 `3rd.module.sensor:VL53L0X_4Plus2`，关联 `VL53L0X_4Plus2_PinHeader_P2.54mm_13x10mm_Provisional`。未知板厂不冠以 ST 厂商名；传感器模块分类独立于裸芯片。排针列距按照片推算为 10.16 mm；安装孔仅作装配参考，不在底板自动钻孔。见 尺寸记录（历史记录见 Git）。

新增 `3rd.module.sensor:GY-SHT3x` 符号与对应 `_PinHeader_P2.54mm_13x10mm_Provisional` 封装；根据正反面照片核对 ALERT/ADDR，板形及列距为估算。详见 SHT3x 模块记录（历史记录见 Git）。

2026-10-09：新增 mikroBUS 底座与模块接口符号、底座封装及 S/M/L 模块板框，均位于 `3rd.connector`。尺寸、方向和使用方法见 mikroBUS 说明（历史记录见 Git）。当前共 42 个符号、44 个封装。

2026-10-09：mikroBUS 封装文字统一横向；底座拆为 S/M/L 三种占位尺寸。旧 `3rd.connector:mikroBUS_Socket_2x08_P2.54mm` → `3rd.connector:mikroBUS_Socket_S_2x08_P2.54mm`，另增 M/L；符号默认关联 S 型并允许筛选三种规格，已有设计需更新旧引用。当前共 42 个符号、46 个封装。

2026-10-10：mikroBUS 按官方 v2.00 手册修订丝印，加入从 PDF 提取的完整 Logo、开口底座轮廓及模块正面竖排／背面横排标注。S/M/L 底座统一接口丝印，模块投影及空间预留按尺寸区分；实际板名、NC 与多底座编号由具体设计填写，见 规范核对记录（历史记录见 Git）。

2026-10-10：`3rd.connector:XUNPU_TF-110` 按原厂 Rev A 手册重绘符号与推荐焊盘，修正检测开关未插卡闭合状态、右上内侧壳焊盘位置、SWA 宽度等尺寸，并补顶层禁布区。名称及功能电气标识不变；已有 PCB 更新后需检查走线与禁布区。见 TF-110 核对记录（历史记录见 Git）。

## 原始资料与数据

`docs/` 仅保留原始资料，文件名统一为 `[厂商_]<型号>_<资料类型>[_版本].扩展名`；整理时只改名称，保留原文件内容。生成预览、过程笔记、备份及重复 JSON 已移除，历史内容可从 Git 查阅。脚本必需的迁移表和 mikroBUS Logo 轮廓数据保留在 `scripts/data/`。

Adafruit PCB 原文件来源：[MCP2221](https://github.com/adafruit/Adafruit-MCP2221-PCB)、[FT232H](https://github.com/adafruit/Adafruit-FT232H-Breakout-PCB)。Designed by Limor Fried/Ladyada for Adafruit Industries. Adafruit invests time and resources providing this open source design; please support Adafruit and open-source hardware by purchasing products from Adafruit. 原始文件及派生几何遵循源仓库 Creative Commons Attribution/Share-Alike 条款。两块核心板当前 USB 朝上，安装孔圆仅作位置参考，载板需自行添加实际安装孔。

TF-110 3D 模型来源于 LCSC C266613 的 EasyEDA 配套模型，UUID `6f3af1915f434bde9fc3a32e8e3a97c0`；按用户要求去除独立标识实体。模型关联 Z 偏移 +0.05 mm，当前使用本机绝对路径，迁移库时需更新。TF-110 的历史电气编号 `GND/SWB` 仅代表 SWB 开关端，不能据此认定内部接地；规则域为用户指定的中央矩形简化范围。

`3rd.crystal` 按用户最新要求采用 YXC 厂商及具体型号命名，取代此前无厂商的通用名称。符号为 `YXC_YSO680PR`（有源，默认 3225，可选 2520）、`YXC_YSX321SL`（3225 无源）、`YXC_YSX221SL`（2520 无源）。有源 1=OE/ST/NC、2=GND、3=OUT、4=VDD；无源 1/3 为晶体端、2/4 接地。封装俯视编号均为左下 1、右下 2、右上 3、左上 4。

| 封装 | 本体尺寸 mm | 单个焊盘 mm | 焊盘中心距 X×Y mm |
| --- | --- | --- | --- |
| `YXC_YSO680PR_2520_2.5x2.0mm` | 2.5×2.0 | 0.90×0.80 | 1.85×1.45 |
| `YXC_YSO680PR_3225_3.2x2.5mm` | 3.2×2.5 | 1.30×1.10 | 2.30×1.90 |
| `YXC_YSX221SL_2520_2.5x2.05mm` | 2.5×2.05 | 1.00×0.90 | 1.85×1.55 |
| `YXC_YSX321SL_3225_3.2x2.5mm` | 3.2×2.5 | 1.40×1.20 | 2.20×1.70 |

尺寸来自原始手册：[YSO680PR](docs/YXC_YSO680PR_Datasheet.pdf)、[YSX221SL](docs/YXC_YSX221SL_Datasheet.pdf)、[YSX321SL](docs/YXC_YSX321SL_Datasheet.pdf)。YSX221SL 手册概要的 2.05×2.05 与尺寸图不一致，本库以详细尺寸图的 2.5±0.05×2.05±0.05 mm 为准。已修正旧 2520 无源版过小的焊盘及中心距；3225 有源和无源推荐焊盘确实不同，不能只按外壳尺寸混用。圆角矩形焊盘按项目规则处理，丝印、庭院为按间距规则生成的库图形，不属于厂家推荐铜皮尺寸。

名称迁移：`Oscillator_4Pin` → `YXC_YSO680PR`；`Crystal_4Pin` → `YXC_YSX321SL`，原来使用 2520 的设计应选 `YXC_YSX221SL`。旧 `Oscillator_SMD_2520/3225_4Pin_*` 分别迁至上表 YSO680PR 封装；旧 `Crystal_SMD_2520/3225_4Pin_*` 分别迁至 YSX221SL/YSX321SL。详细映射保存在 `scripts/data/library-classification.json`；已有原理图/PCB 的引用需另行更新，本次未改动已有设计。

### ZY-MAX485（2026-10-14）

新增 `3rd.module.interface` 有线接口模块分类，符号 `ZY-MAX485`，以及独立的
`ZY-MAX485_PinHeader_P2.54mm_15x12mm_Provisional` 与
`ZY-MAX485_Castellated_P2.54mm_15x12mm_Provisional` 封装。
来源：[用户提供的原理图和实物尺寸图](docs/ZY-MAX485_Dimensions.jpg)。
板尺寸 15×12mm；排针节距 2.54mm、列距 12.70mm、居中位置按照片估算，需实物核对。
排针孔径 1mm、焊盘直径 1.8mm 为底板设计值；贴片焊盘按项目半孔规则计算。
元件面朝上：左列从上到下 GND/TXD/RXD/VCC，右列 EN/B/A/GND。
引脚编号与焊盘名均采用功能名称，两处 GND 同网。TXD 是 RO（三态输出），
RXD 是 DI（输入），不要按主控 TX/RX 习惯反向定义。EN 同时控制 DE 与低有效 RE，
高电平发送、低电平接收，板载 10k 下拉；板载 A-B 120Ω 终端，A 上拉与 B 下拉各 4.7k。
模块厂商未核实，保留 ZY-MAX485 型号且不添加芯片厂商前缀。

### 通用降压电源模块（2026-10-14）

新增 `3rd.module.power:Buck_EN` 和 `Buck` 通用符号，使用 VIN/VOUT/GND/EN
功能编号；无使能符号仅有 VIN/VOUT/GND。两者默认封装留空，避免将无 EN
符号关联到含 EN 焊盘的实物；带 EN 符号过滤贴板封装，无 EN 符号过滤排针封装；均不绑定封装。
封装 `MP2225GJ-Z_PinHeader_18x13mm_Provisional` 与
`MP2225GJ-Z_Castellated_18x13mm_Provisional` 来自
[用户尺寸图](docs/MP2225GJ-Z_18x13mm_Dimensions.png)，用户确认芯片为 MP2225GJ-Z，模块厂商未确认。
板体 18×13mm，纵向孔距 9.2mm；以板中心为原点，功率孔 y=±4.6mm，
EN y=+0.1mm（比右下 GND 高 4.5mm）。纵向居中由照片估算；
列距暂估 13.4mm，板角 R0.8mm 暂估；底板排针焊盘直径 2.2mm、钻孔 1.2mm
为设计值，需要核实排针及模块孔径。排针版按用户要求不引出 EN，仅保留四个功率通孔，配合无 EN 的通用符号。
贴板版保留 EN 焊盘。两版板内丝印 EN DEFAULT: ON / EN H=ON L=OFF，
表示用户确认的默认使能、高使能和低失能状态。
贴板版四个功率焊盘统一为 4×2.4mm 圆角矩形，中心 x=±7.8mm、y=±4.6mm，
相对板边外伸 0.8mm、内伸 3.2mm，圆角半径 0.25mm。根据照片焊接区域估算，
不套用稀疏功率触点之间 9.2mm 的节距公式；保留 Provisional 待实物核对。
EN 焊盘保持原有尺寸、位置及网络标识，排针版保持不变。
模块底面结构未提供，贴板前应核实绝缘及底面元件间隙。

### 功能编号迁移（2026-10-14）

全部模块及非通用核心板采用功能作为符号引脚编号和封装焊盘名。本次转换
16 份符号及 19 份封装，已有功能编号条目保持不变。NUCLEO ST-MORPHO
属于跨板型共用接口，保留 CN7/CN10 编号；mikroBUS 标准接口不在此次专用板迁移范围。
GPIO 使用端口名；多功能说明保留在引脚名称中。低有效 EN/RST/SLP 的编号
采用 EN_N/RST_N/SLP_N，符号名称仍保留低有效上划线。NC 引脚使用独立标识，
如 NC_5，PDN 与 PDN_ALT 等未确认短接的触点保持分开；GND 同网触点共用编号。
E73 LP/LX 按 docs/Ebyte_E73-2G4M_UserManual_CN_V1.2.pdf 第 5–6 页共用引脚表同步转换。

按用户要求删除 `WeAct_STM32G431CBT6_Standard` 符号，只保留 CBU6。
封装 `WeAct_STM32G431CoreBoard_Standard_P2.54mm` →
`WeAct_STM32G431CBU6_Standard_P2.54mm`，焊盘形状、孔位、层和丝印位置不变。
本次只改变电气标识，并为较长编号延长必要的符号引线；未改变封装几何。

完整逐引脚旧→新映射在 `scripts/data/library-classification.json` 的
`pin_identifier_migration` 记录中。现有原理图/PCB 的缓存编号不会自动迁移：
更新库器件时须按映射同步更新两端并核对网络，不能仅替换封装。

命名迁移：`BMP280_8Pin` → `ZY-BMP280`（用户确认名称），符号及两种安装封装同步改名，功能编号与几何不变；已有设计需更新库引用。

命名迁移：`SHT3x-DIS_4Plus2` → `GY-SHT3x`（用户指定模块名称），符号、封装及过滤器同步更新，尺寸与功能编号不变；已有设计需更新库引用。

命名迁移：`ADS1115_8Pin` → `ZY-ADS1115`（用户指定模块名称），符号、排针与贴板封装、过滤器及原始资料文件名同步更新，尺寸与功能编号不变；已有设计需更新库引用。

命名迁移（2026-10-15）：按用户要求，`ST_NUCLEO-U545RE-Q_ST-MORPHO` → `ST_NUCLEO-U545RE_ST-MORPHO`，Value 同步去掉 `-Q`。官方板卡资料链接及型号描述保留；引脚和通用 NUCLEO 封装关联不变。已有原理图需更新符号库标识。
