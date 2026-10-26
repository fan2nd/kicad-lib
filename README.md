# 第三方 KiCad 符号与封装库

按器件实际形态和用途分类。符号采用 KiCad 10 的 `.kicad_symdir` 目录库，封装采用 `.pretty` 库；库昵称与目录名保持一致。

## 凯华机械轴热插拔封装

新增两个独立封装，均在 `3rd.switch`：`Kailh_PG1350_HotSwap`（Choc V1/PG1350，配 CPG135001S30 座）和 `Kailh_MX_HotSwap`（标准 MX，配 CPG151101S11-16 座）。不是双轴混合孔位，不适用于 PG1353。轴体在 PCB 正面、座子在背面；保持封装放在 F.Cu 即可，焊接焊盘已定义在 B.Cu/B.Mask/B.Paste，座子外形丝印在 B.SilkS，正面只画轴体角标。两版各有 5 个 NPTH：中心柱孔、两个定位柱孔、两个直径 3 mm 的触点穿孔。触点孔不镀铜，电气连接由背面两个圆角贴片焊盘完成；编号为 1/2，可配官方 `Switch:SW_Push`，PG1350 也可配现有 `Kailh_PG1350` 符号，原直接焊接封装不变。

坐标以轴心为原点，从正面看：

| 封装 | 中心孔 | 定位孔 | 触点穿孔中心 | 背面焊盘中心及尺寸 |
| --- | --- | --- | --- | --- |
| PG1350 | Ø3.4 mm | (±5.5, 0)，Ø1.9 mm | 1=(0, 5.95)，2=(-5, 3.75)，均 Ø3 mm | 1=(3.275, 5.95)，2=(-8.275, 3.75)，2.6×2.6 mm |
| MX | Ø4 mm | (±5.08, 0)，Ø1.7 mm | 1=(2.54, -5.08)，2=(-3.81, -2.54)，均 Ø3 mm | 1=(6.29, -5.08)，2=(-7.56, -2.54)，2.55×2.5 mm |

MX 版保留五脚轴的两侧塑料定位孔，三脚轴也可安装。PG1350 座接触孔纵向差为 2.20 mm，采用 3.75/5.95 mm 的安装位置，对应轴体 3.8/5.9 mm 触点各偏移 0.05 mm，利用 Ø3 mm 座孔容差，不直接复用焊接版 Ø1.2 mm 孔。矩形电气焊盘统一 R0.25 mm；铜皮到 NPTH 边缘检查不小于 0.2 mm。F.Fab 是轴体占位，B.Fab/B.SilkS 是简化座体轮廓，未标注的小圆角只作装配示意；封装不生成定位板切口或 Edge.Cuts，也不自带 LED 焊盘。

来源：[凯华 PG1350 座原始手册](docs/Kailh_CPG135001S30_Datasheet_RevB.pdf)、[凯华 MX 座原始尺寸及手册](docs/Kailh_CPG151101S11-16_Dimensions_Datasheet.pdf)。座孔直径、触点孔相对间距和焊盘尺寸依原厂图；轴心到孔位及焊盘中心位置与 [daprice/keyswitches.pretty](https://github.com/daprice/keyswitches.pretty) 的 PG1350/MX 安装坐标交叉核对；未复制该库图形。MX 中心及定位柱孔另与已安装 KiCad 官方 `SW_Cherry_MX_1.00u_PCB` 核对。正式选用时须匹配上述座子型号，PG1350 推荐板厚按座子手册为 1.6 mm。

## W5500 Lite 以太网模块

新增 `3rd.module.interface:W5500_Lite`，关联 `W5500_Lite_PinHeader_P2.54mm_23x25mm_Provisional`。按用户提供的 [尺寸图](docs/W5500_Lite_Dimensions.jpg)、[元件面照片](docs/W5500_Lite_Pinout.png) 及最新 [尺寸和引脚图](docs/W5500_Lite_Dimensions_Pinout.png) 绘制；未知板厂不添加 WIZnet、USR 等厂商前缀。模块位于底板上方，RJ45 插口朝上，J1 左列从上至下为 GND/GND/MOSI/SCLK/CS/INT，J2 右列为 GND/3V3/3V3/NC/RST/MISO。照片 MO/MI 对应 MOSI/MISO；J2-4 按照片 NC 标识保留独立 `NC`，不套用其他版本的 PWDN。CS、INT、RST 低有效。符号和焊盘均使用功能编号，重复 GND/3V3 分别共网。

PCB 为 23×25 mm，排针列距 20.32 mm、纵向针距 2.54 mm；板中心为原点，列中心 x=±10.16 mm。最新图首针距底边 18.50 mm、末针距底边 5.80 mm，因此首针 y=-6.00 mm、末针 y=6.70 mm，距顶边为 6.50 mm；以此覆盖首张表中不闭合的 I=6.40 mm。底板焊盘 1.8 mm、钻孔 1.0 mm 为排针适配尺寸；两列首针用圆角矩形，其余圆形。RJ45 宽度 16.10 mm、前端伸出 PCB 3.50 mm 按首张尺寸表绘制；后端暂估至 y=11.30 mm，仅在 F.Fab 标识。F.SilkS 保留模块板框、RJ45 前端轮廓及板内水平功能文字，不在底板生成 RJ45 固定孔或 Edge.Cuts。RJ45 后端等机械细节未全部标注，保留 `_Provisional`。供电为 3.3 V，电源供电能力按用户资料大于 200 mA。

## 待检查清单

- [x] `Trinamic_TMC4361A-BOB`：2026-10-15 按官方 BOB 手册 Rev1.0 第 1 页模块顶视图／接口表、第 2 页原理图核对。两侧 30 个接点和顶部 3 个接点的名称、功能编号及位置顺序均匹配，无需改名或对调焊盘。
- [ ] `Trinamic_TMC2160-BOB`：核对模块实际引脚顺序、功能与当前符号引脚编号／封装焊盘名的对应关系，复核数字编号迁移为功能编号的映射。

未勾选项目尚未完成核实；符号与封装的编号集合一致性检查不代表物理引脚映射已经确认。

TMC4361A-BOB 核对依据：[官方模块原理图及顶视图](docs/Trinamic_TMC4361A-BOB_Datasheet_Rev1.0.pdf)。文档版本为 Rev1.0，照片中的板版为 1.1。模块功能名与裸芯片定义的关键差异如下：

| BOB 功能编号 | 芯片脚号／名称 | 说明 |
| --- | --- | --- |
| CLK / NRST / CSN / SCK | 38 CLK_EXT / 39 RST / 2 SCSIN / 3 SCKIN | 使用模块网络名称 |
| SDI / SDO | 4 SDIIN / 7 SDOIN | 控制端 SPI 输入／输出 |
| CSN_DRV / SCK_DRV | 30 SCSDRV / 29 SCKDRV | 驱动端片选／时钟 |
| SDO_DRV | 28 SDIDRV | 来自外接驱动器 SDO；对本模块是输入 |
| SDI_DRV | 27 SDODRV | 送往外接驱动器 SDI；对本模块是输出 |
| TARGET_R / NFREEZE | 31 TARGET_REACHED / 19 FREEZE | 保留板上网络名称 |
| ANEG / BNEG / NNEG | 1（反相 A）/ 11（反相 B）/ 22（反相 N） | 与 A/B/N 分别独立，不能合并 |
| DCSTEP_STALL / DC_OUT / STDBY_CLK | 8 MP1 / 9 MP2 / 32 STDBY_CLK | 顶部从左至右三个接点 |

顶视方向以左上 VCC、右上 INTR 为准。左列从上至下为 VCC/GND/CLK/NRST/CSN/SCK/SDI/SDO/HOME_REF/STOPR/STOPL/NFREEZE/START/STPIN/DIRIN；右列为 INTR/TARGET_R/CSN_DRV/SCK_DRV/SDO_DRV/SDI_DRV/STPOUT/DIROUT/ANEG/A/BNEG/B/NNEG/N/GND。两个 GND 经原理图确认共网。符号引脚编号与封装焊盘名继续使用模块功能名，不能套用裸芯片数字脚号。本次核对未更改电气标识或封装几何。

按用户最终选择，保留 BOB 板上丝印名称。下一级驱动器统一标为 `NEXT`，不限定具体型号；以下按兼容的 SPI 与 STEP/DIR 接口说明连接，信号方向以 TMC4361A-BOB 为参照。NEXT 的实际端口名称及接口兼容性须按所选器件手册确认：

| TMC4361A-BOB | 方向 | NEXT |
| --- | --- | --- |
| CSN_DRV | → | CSN |
| SCK_DRV | → | SCK |
| SDI_DRV（芯片 SDODRV） | → | SDI |
| SDO_DRV（芯片 SDIDRV） | ← | SDO |
| STPOUT | → | STEP |
| DIROUT | → | DIR |
| GND | 共地 | GND |

SPI 用于配置／读取 NEXT，STEP/DIR 用于运动脉冲控制；需配置相应接口工作模式，不能仅接 SPI 就假定已完成运动控制。TMC4361A-BOB 与 NEXT 的逻辑电平须兼容；NEXT 的逻辑电源、电机电源范围及使能极性按所选器件手册确定，不沿用某一具体驱动器的参数。NEXT 的使能由主控控制，初始化前保持禁能。dcStep 等可选接口不包含在上述基本连接中，按需另行核对与配置。

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


### ZJY096T-IG11 背折排线 3D 模型

`3rd.display:Zhongjingyuan_ZJY096T-IG11_Solder_Folded` 已关联
`3dmodels/3rd.display.3dshapes/Zhongjingyuan_ZJY096T-IG11_Solder_Folded.step`，
同目录的 `.FCStd` 为可编辑源工程。屏体最大包络 13.5×27.95×1.5 mm，
显示区 10.8×21.7 mm；依据 `docs/Zhongjingyuan_ZJY096T-IG11_Datasheet_RevB.pdf`。
内部层厚、FPC 未标注轮廓和弯折为外观简化，不作为制造尺寸。
模型原点为屏体背面中心，正 Z 朝显示面；按 KiCad 3D 坐标，屏顶为正 Y，
引脚 1 位于 X=+4.2 mm。关联偏移 (0,0,+0.32) mm、缩放 1、旋转 0，
使金手指最低面位于 PCB 顶面。触点位于对应 0.4×3 mm 焊盘范围内。
沿用现有模型的本机绝对路径方式；迁移库时需修改关联路径。
此模型仅适用于背折版，不关联 `Solder_ThroughPCB_1.6mm` 穿板背焊版。

### C455282 / C2681476 轻触开关

新增 `3rd.switch:XUNPU_TS-1089S-02526`（C455282）和
`3rd.switch:Shouhan_TS3425BA`（C2681476）。原始资料分别保存为
`docs/XUNPU_TS-1089S-02526_Datasheet.pdf`（装配图第 2 页）及
`docs/Shouhan_TS3425BA_Datasheet.pdf`（第 1 页）。

| 封装 | 本体/mm | 端子总宽/mm | 焊盘尺寸/mm | 焊盘中心 X/mm | 焊盘中心 Y/mm |
| --- | --- | --- | --- | --- | --- |
| XUNPU_TS-1089S-02526 | 4.2×3.25 | 5.10 | 1.20×0.65 | ±2.15 | ±1.075 |
| Shouhan_TS3425BA | 4.2×3.20 | 4.60 | 1.05×0.65 | ±2.075 | ±1.075 |

均按原厂推荐焊盘的内外边缘计算，矩形焊盘依项目规则作圆角处理。
俯视图：上排两个焊盘均为 1，下排两个焊盘均为 2；同排内部相通，
按下后两排接通，可配合官方 `Switch:SW_Push` 两脚符号使用。
按用户要求将旧编号 1/2 合并为 1，旧编号 3/4 合并为 2；焊盘几何和模型不变。
已有 PCB 如使用旧四脚编号，应同步更新符号及焊盘网络。

配套模型位于 `3dmodels/3rd.switch.3dshapes/`，每款提供 `.step`、`.wrl`
及可编辑 `.FCStd`。两款均已改用立创原始 STEP，取消先前自建的简化几何。
封装关联 WRL；同名 STEP 用于 KiCad 的 STEP 导出替代。
原始模型保存于 `docs/XUNPU_TS-1089S-02526_Model_LCSC.step` 和
`docs/Shouhan_TS3425BA_Model_LCSC.step`，保持下载字节不变。
来源模型 UUID 分别为 `ccf428d0f05443699e8e5d7213d16527`、
`2b59e85a5ed544cb9a7fbd649d351ea1`（通过 EasyEDA 的对应 LCSC 料号接口获取）。

只清除 logo 几何并对齐贴板面：XUNPU 填平底面刻字、削除右侧凸字，模型 Z 平移
+1.7 mm；Shouhan 削除底面凸字，模型 Z 平移 +0.01 mm，保留原始向上包脚。
处理后原点位于主体中心投影、端子最低面 Z=0，封装关联无额外偏移或旋转。
立创原模型包络分别为 5.20×3.25×2.50 mm 和 4.65×3.30×2.51 mm；
与原厂图纸存在细微差异，保持模型原几何，焊盘仍以原厂图纸为准。
WRL 按 KiCad 的 0.1 英寸单位导出，STEP/FCStd 采用毫米；模型关联沿用本库绝对路径。
可用 FreeCAD Python 运行 `scripts/build_tact_switch_models.py` 重建并校验 STEP 包络。


### HRO U-A-24DS-W-1（C530628）

新增 `3rd.connector:HRO_U-A-24DS-W-1`，使用安装库已有的
`Connector:USB_A` 通用符号，不重复创建符号。焊盘 1=VBUS、2=D-、3=D+、4=GND，
四个屏蔽壳焊脚均为 `SH`，与当前官方符号逐项匹配。
来源：`docs/HRO_U-A-24DS-W-1_Datasheet.pdf`，HRO（韩荣）2021-06-21 图纸。
信号焊盘 1.15×2.45 mm，X=-3.5/-1/+1/+3.5 mm、Y=-1.825 mm；
屏蔽壳焊盘 1.3×2.3 mm、镀铜长圆孔 0.8×1.8 mm，X=±7.775 mm、Y=0/5.5 mm。

封装包含三边开放的 U 形 `Edge.Cuts` 沉板槽：X=±6.6 mm、后边 Y=0，
两端到 Y=9.5 mm 的主板边缘。必须将两端与主板板框连接，删除横跨槽口的原板边线；
不能把该封装直接放在完整闭合主板内部。`Dwgs.User` 虚线为主板边缘参考，
`F.Fab` 为插座实体轮廓；丝印避开开槽和壳脚，前端悬空区域不印丝印。
手册没有标注槽宽，13.2 mm 采用立创对应料号参考封装；制板前核对实物间隙和板厚。
参考封装来源 [嘉立创EDA](https://lceda.cn/) / [EasyEDA](https://easyeda.com/) 官方库，
原始器件接口 `https://easyeda.com/api/products/C530628/components?version=6.4.19.5`。
可通过 `scripts/build_hro_usb_a.py` 重建封装。

C530628 已关联去标识立创 3D 模型（UUID `56bfa40334ac452f8b0ea67224a29821`）。
原始 STEP 保存在 `docs/HRO_U-A-24DS-W-1_Model_LCSC.step`；处理后 STEP/WRL/FCStd
位于 `3dmodels/3rd.connector.3dshapes/`。只清除壳体侧面与底面 logo，
原始模型平移 (0,-10.25,+1.24) mm，信号脚底面落于 Z=0；外壳下沉保留。
使用原模型几何，不据其修改手册焊盘；原模型外壳深度与手册略有差异。
生成脚本为 `scripts/build_hro_usb_a_model.py`，模型关联采用既有绝对路径惯例。
封装 1 脚丝印改为小圆点，电气编号不变。

### HongCheng recessed USB 3.0 Type-A (C7501852 / C7501855 / C7501863)

Added `HongCheng_HC-USB3.0-C34-P`, `HongCheng_HC-USB3.0-C225-P`, and
`HongCheng_HC-USB3.0-C345-P` in `3rd.connector`, with original LCSC STEP sources
and manufacturer datasheets in `docs/`. STEP / WRL / editable FCStd models are
in `3dmodels/3rd.connector.3dshapes/`; raised LCSC lettering/logo is removed,
while shell springs, windows, contacts and mounting tabs are preserved.
Generators: `scripts/build_hongcheng_usb3.py` and `scripts/build_hongcheng_usb3_models.py`.

Signal lands follow the respective recommended PCB drawings (C34/C225: 9 lands,
0.70 x 1.60 mm; C345: four 1.00 x 2.20 mm plus four 0.45 x 2.20 mm).
All shell contacts use `SH`; pin 1 is identified by a silk dot.
C345 has **no independent external pad 7** in the supplied PCB drawing or model;
do not invent a land or assume GND_DRAIN is electrically bonded to the shell.
A generic nine-contact USB3 symbol therefore requires explicit treatment of pin 7.

Open U-shaped `Edge.Cuts` must be joined to the carrier outline, with the USB
opening facing +Y. C345 notch width 13.60 mm and rear edge y=1.70 mm follow its
PCB drawing. C34/C225 drawings do not fully dimension the carrier notch: rear
edges use LCSC CAD (2.05 / 1.435 mm); width is 13.20 mm, clearing the nominal
13.10 mm housing and leaving the specified shell lands intact. C34's wider
LCSC cutout was narrowed because it intersected the datasheet shell lands.
These two notch fits need physical verification; shell-land-to-notch clearance
is only 0.05 mm, so confirm the board fabricator's edge-copper process.
Nominal body depths below PCB are 3.40 / 2.25 / 3.45 mm respectively.
The original C225 model differs by 0.01 mm in body height and C345 by 0.05 mm
in a mounting-tab location; the original geometry is retained.

### 按键轴 3D 模型（2026-10-23）

为 `Kailh_PG1350_Solder`、`Kailh_PG1350_HotSwap`、
`Kailh_MX_HotSwap` 关联本地 3D 模型；两种热插拔封装同时显示正面轴体和背面座子。
PG1350 模型转 Z 轴 180°，匹配本库 LED 朝北方向。背面座模型按约 1.6 mm
PCB 安装位置提供，其他板厚需调整模型高度。焊盘、钻孔、丝印均未修改。
MX 轴体为通用 Cherry MX 装配示意，非特定凯华轴款。
KiSwitch 模型为 WRL。来源、许可和限制见
[模型来源说明](3dmodels/3rd.switch.3dshapes/SOURCES.md)。

2026-10-23：按用户要求删除 `Kailh_PG1353` 符号、`Kailh_PG1353_Solder` 封装及专用 STEP/WRL 模型。原始手册保留归档；历史条目不代表当前可用器件。已有设计中的该符号／封装需另行替换。

### ESPC2-01-N2 / E01C-ML01D 排母（2026-10-24）

`DOIT_ESPC2-01-N2` 和 `Ebyte_E01C-ML01D` 增加正面 2×4、2.54 mm
直立排母装配轮廓与 3D 模型。排母塑壳为 10.16×5.08×8.5 mm，脚伸出
PCB 顶面以下 3.1 mm；属于通用排母示意，具体采购高度需匹配。
模型由本机 KiCad 官方 `Connector_PinSocket_2.54mm.3dshapes/PinSocket_2x04_P2.54mm_Vertical.step`
旋转并居中，保留原始几何；放在本项目 `3dmodels/3rd.connector.3dshapes/`
供两封装共用。原官方库文件未修改。上游来源为
https://gitlab.com/kicad/libraries/kicad-packages3D ，遵循上游模型许可。
排母安装在底板正面，丝印为 F.SilkS；焊盘、钻孔和功能编号保持不变。
ESPC2 移除了指向本机不存在文件的旧 ESP-01 模型引用，当前显示排母而非模块轴测外形。

### Raspberry Pi CSI / DSI 接口符号（2026-10-27）

新增到 `3rd.connector`，仅定义接口，不绑定具体 FPC 座封装：

| 符号 | 接口 |
| --- | --- |
| `RaspberryPi_CSI_15Pin` | 旧版 15P、1.0 mm、双数据通道 CSI |
| `RaspberryPi_DSI_15Pin` | 旧版 15P、1.0 mm、双数据通道 DSI |
| `RaspberryPi_MIPI_22Pin` | Pi 5 CAM/DISP0 或 CAM/DISP1，22P、0.5 mm、CSI/DSI 共用 |

这些是标准接口，pin number 保留 1–15 / 1–22，pin name 显示功能，所有接点采用 passive 类型；GND 和 3V3 的多个接点分别保留各自编号。旧版 CSI 与 DSI 不兼容：CSI 的 D0/D1/CLK 分别在 2–3/5–6/8–9，DSI 则是 D1/CLK/D0；电源和 I2C 位置也不同。Pi 5 使用一个共用符号和物理引脚表，17/18 保留 CAM_IO0/CAM_IO1，不擅自接地。符号不代表显示端一定使用这些辅助 GPIO。

来源：[官方 CSI 15P/22P 引脚表](https://www.raspberrypi.com/documentation/accessories/camera.html)、[Pi 4B 官方原理图 DISPLAY J4](docs/RaspberryPi_4B_Schematic_Reduced.pdf)、[官方 Pi 5 共用 CSI/DSI 接口说明](https://www.raspberrypi.com/documentation/computers/sbcs.html)。这里只定义旧版树莓派接口与 Pi 5，不声称适配 Compute Module 底板。连接器的观察方向、触点面及排线翻转需按实际座子核对，不能由符号左右布局判断。生成脚本：`scripts/build_raspberrypi5_mipi_symbols.py`。

### Raspberry Pi PCIe FPC 接口（2026-10-27）

`3rd.connector:RaspberryPi_PCIe_FPC_16Pin` 按[官方 PCIe 规范 v1.1](docs/RaspberryPi_PCIe_StandardSpecification_1.1.pdf)图 1 定义 16 个数字接点，0.5 mm 间距，PCIe x1；无封装绑定，机械固定脚不属于排线接口，未加入符号。引脚类型为 passive。RX/TX 以树莓派主机为参照：RX 接外设发送端，TX 接外设接收端。

1/2=5V，3/6/9/12=GND，4/5=PCIE_CLK_P/N，7/8=PCIE_RX_P/N，10/11=PCIE_TX_P/N，13=PCIE_PWR_EN，14=PCIE_DET_WAKE，15=PCIE_CLKREQ_N，16=PCIE_RST_B。控制信号为 3.3 V；PCIE_PWR_EN 是主机输出，DET_WAKE 用于外设检测/唤醒。不得将 5V 电源和 3.3V 控制信号混淆。生成脚本：`scripts/build_raspberrypi_pcie_symbol.py`。

### Qwiic 接口符号（2026-10-27）

新增 `3rd.connector:Qwiic`，按 [SparkFun Qwiic 标准](https://www.sparkfun.com/qwiic)及[官方参考原理图](https://cdn.sparkfun.com/assets/0/0/3/5/4/Qwiic-OpenLog.pdf)定义：1=GND、2=3V3、3=SDA、4=SCL。采用数字接点编号及 passive 类型，JST SH 4P、1.0 mm 接口；未绑定封装，可按卧贴/立贴等实际连接器选择。符号不包含机械固定焊脚。生成脚本为 `scripts/build_qwiic_symbol.py`。

### Grove-IIC 与接口符号布局更新（2026-10-27）

新增 `3rd.connector:Grove_IIC`，依据 [Seeed Grove 官方定义](https://wiki.seeedstudio.com/Grove_System/)：1=SCL、2=SDA、3=VCC、4=GND。VCC 根据实际系统为 3.3V 或 5V，不固定为 3V3；数字接点编号、passive 类型、不绑定封装。生成脚本为 `scripts/build_grove_iic_symbol.py`。

本次新增的旧版 CSI/DSI、Pi 5 MIPI、PCIe、Qwiic、Grove-IIC 共六个接口符号均改为右侧出线，编号自上而下保持不变。`RaspberryPi_5_CSI_22Pin` 和 `RaspberryPi_5_DSI_22Pin` 合并为 `RaspberryPi_MIPI_22Pin`，没有保留旧名副本；已放置的符号若使用旧名需重新指定库符号。

命名修正：临时名 `mipi_22pin` 已更正为 `RaspberryPi_MIPI_22Pin`，保留树莓派接口前缀及 MIPI 标准大写；引脚定义和右出线布局不变。

### Raspberry Pi SH 1.0 mm 三针调试接口（2026-10-27）

依据[官方三针调试接口规范 rev 4](docs/RaspberryPi_DebugConnector_StandardSpecification_4.pdf)，新增以下 `3rd.connector` 符号，均右出线、数字接点编号、passive 类型，不绑定封装：

| 符号 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| `RaspberryPi_SWD_3Pin` | SWCLK | GND | SWDIO |
| `RaspberryPi_UART_Host_3Pin` | TX | GND | RX |
| `RaspberryPi_UART_Target_3Pin` | RX | GND | TX |

UART 名称以符号所代表的本地设备为参照：Host 是调试探针，Target 是被调试设备（包括 Pi 5 的调试串口）。规范表格采用 Target 视角，所以不能把表格中的 RX/TX 原样标到 Host。使用 1→1、2→2、3→3 的直通线，Host TX 即连接 Target RX。SWD 两端接点功能相同，无需拆分 Host/Target；时钟由 Host 驱动。接口没有 VCC/VTref/复位接点。标准连接器为 JST SH 1.0 mm 3P，顶插 BM03B-SRSS-TB 或侧插 SM03B-SRSS-TB，具体封装另选。规范建议信号源端串联 100Ω，Host 为 3.3V IO；这些电路要求没有嵌入连接器符号。生成脚本：`scripts/build_raspberrypi_debug_symbols.py`。
