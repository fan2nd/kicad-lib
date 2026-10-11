# Adafruit USB 核心板封装重绘

2026-10-10。来源为 Adafruit 官方 USB-C 版本 Eagle PCB：
- https://github.com/adafruit/Adafruit-MCP2221-PCB （本地 Adafruit_MCP2221.brd）
- https://github.com/adafruit/Adafruit-FT232H-Breakout-PCB （本地 Adafruit_FT232H.brd）

原设计：Designed by Limor Fried/Ladyada for Adafruit Industries. Adafruit invests time and resources providing this open source design; please support Adafruit and open-source hardware by purchasing products from Adafruit. 原始文件及本次派生几何按原项目 Creative Commons Attribution/Share-Alike 条款使用，详见上述仓库 license.txt。

生成器：scripts/build_adafruit_usb_coreboards.py。保留原公共名称、原点及功能焊盘编号。最终 Eagle 坐标转换为 x'=y−板高/2、y'=x，顶视图 USB 朝上、Qwiic 朝下，原点在板顶边中心。相对旧版 USB 朝左的封装为整体顺时针旋转并重设原点，已有 PCB 实例更新后需核对位置和角度。通过官方 signals/contactref 核对每个排针的网络及旋转位置。

| 封装 | 板尺寸 | 排针 | 排距 | 圆角 |
|---|---|---|---|---|
| Adafruit_MCP2221A | 25.40×17.78 mm | 两排各 6，间距 2.54 mm | 12.70 mm | R2.54 mm |
| Adafruit_FT232H | 38.10×22.86 mm | 两排各 11，间距 2.54 mm | 20.32 mm | R2.54 mm |

模块在载板上方：板外形在 F.SilkS/F.Fab，无 Edge.Cuts；四角孔仅以丝印/装配圆表示模块孔位置，不强制在载板钻孔。MCP 左侧孔直径 2.54 mm、右侧 2.50 mm；FT232H 四孔为 2.50 mm，均来自原板。需要螺丝固定时在载板另放安装孔。

引脚孔径 1.00 mm；MCP 焊盘直径 1.778 mm，FT232H 为 1.6764 mm，保持原封装。引脚丝印全部水平且位于板内；复位脚标为 RST，电气编号仍为 ~{R}，与符号兼容。USB-C 和 Qwiic 接口机械轮廓仅保留在 F.Fab；按用户要求撤销接口外框丝印。F.CrtYd 包括 USB-C 的突出部分。

两块封装均已 KiCad CLI 导出并目视检查。全库检查中无关的 A4988/TMC2209 基线差异需另行处理，未以本次重绘覆盖它们。

用户确认的显示名称：QT 改 Qwiic，3V 改 3V3，G0…G3 改 GP0…GP3，5V 及其余引脚名称保持；仅修改丝印，电气焊盘编号不变。

后续用户修正：GPIO 保留原简写，MCP2221A 使用 G0…G3，FT232H 使用 D0…D7/C0…C9；Qwiic 和 3V3 保留。
