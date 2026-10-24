# KiCad 官方连接器封装名称对照表

核对日期：2026-10-23。依据本机安装的 KiCad 官方封装库。
搜索关键词可直接用于封装选择器；俗称对应系列仅用于查找，国产兼容件仍需核对焊盘、定位柱和固定脚，不能只按间距替用。

| 常见名称／俗称 | 间距 | 官方库 | 搜索关键词 |
|---|---:|---|---|
| MX1.25 | 1.25 mm | `Connector_Molex` | `Molex_PicoBlade` |
| GH1.25 | 1.25 mm | `Connector_JST` | `JST_GH` |
| SH1.0 | 1.00 mm | `Connector_JST` | `JST_SH_` |
| ZH1.5 | 1.50 mm | `Connector_JST` | `JST_ZH` |
| PH2.0 | 2.00 mm | `Connector_JST` | `JST_PH_` |
| XH2.5 | **2.50 mm** | `Connector_JST` | `JST_XH` |
| EH2.5 | 2.50 mm | `Connector_JST` | `JST_EH` |
| VH3.96 | 3.96 mm | `Connector_JST` | `JST_VH` |
| 双排 PHD2.0 | 2.00 mm | `Connector_JST` | `JST_PHD` |
| 双排 SHD1.0 | 1.00 mm | `Connector_JST` | `JST_SHD` |
| ZE1.5 | 1.50 mm | `Connector_JST` | `JST_ZE` |
| SUR0.8 | 0.80 mm | `Connector_JST` | `JST_SUR` |
| DF13 | 1.25 mm | `Connector_Hirose` | `Hirose_DF13` |
| 双排 DF11 | 2.00 mm | `Connector_Hirose` | `Hirose_DF11` |
| KK2.54 | 2.54 mm | `Connector_Molex` | `Molex_KK-254` |
| KK3.96 | 3.96 mm | `Connector_Molex` | `Molex_KK-396` |
| Micro-Fit 3.0 | 3.00 mm | `Connector_Molex` | `Molex_Micro-Fit_3.0` |
| Mini-Fit Jr，常见 ATX 电源连接器系列 | 4.20 mm | `Connector_Molex` | `Molex_Mini-Fit_Jr` |
| 普通排针／杜邦板端公针 | 2.54 mm | `Connector_PinHeader_2.54mm` | `PinHeader_1x`、`PinHeader_2x` |
| 普通排母／杜邦板端母座 | 2.54 mm | `Connector_PinSocket_2.54mm` | `PinSocket_1x`、`PinSocket_2x` |
| 简易牛角座／IDC 座 | 常用 2.54 mm | `Connector_IDC` | `IDC-Header` |
| 带锁扣牛角座 | 常用 2.54 mm | `Connector_IDC` | `IDC-Header` + `Latch` |
| XT30／XT60 | 按型号 | `Connector_AMASS` | `AMASS_XT30`、`AMASS_XT60` |
| DC 圆孔电源座 | 按型号 | `Connector_BarrelJack` | `BarrelJack` |
| USB 接口 | 按型号 | `Connector_USB` | `USB_A`、`USB_C`、`USB_Micro` |
| RJ45 网口 | 按型号 | `Connector_RJ` | `RJ45` |

## MX1.25 / PicoBlade 安装形式

| 安装方式 | 官方搜索关键词 | 本机库已有针数 |
|---|---|---|
| 卧贴 | `Molex_PicoBlade_53261` | 2～15P、17P |
| 立贴 | `Molex_PicoBlade_53398` | 2～15P |
| 直插 | `Molex_PicoBlade_53047` | 2～15P |
| 弯插 | `Molex_PicoBlade_53048` | 2～15P |

## 选型与命名说明

- **MX1.25、GH1.25、DF13 都是 1.25 mm，但不是同一种连接器。**
- 商家常写“XH2.54”，而官方 JST XH 是 **2.50 mm**，应按实际尺寸选。
- `Horizontal` 表示水平插接，`Vertical` 表示垂直插接；不代表贴片或通孔，还要看具体型号及焊盘类型。
- `1x04` 表示单排 4 针，`P1.25mm` 表示针距；`MP` 表示机械固定焊盘。
- USB、DC、RJ45 等同类接口的定位孔、外壳脚和电气引脚排列可能不同，应选完整型号对应的封装。

## 核对来源

本机官方封装目录：
`/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints/`。
本表记录的是上述安装版本，不代表未来官方库的全部内容，也不声明讯普等兼容件与 Molex/JST 型号可直接互换。
