# ObjPad-NVDA简易导航器 #

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph
  Lee, Cleverson Uliana and others
* 下载 [稳定版][1]
* NVDA 兼容性：2022.4 及更高版本

此插件提供了一组快捷键来处理屏幕上的对象，包括导航和其他可能性。

## 快捷键

* Control + NVDA + TAB 切换以下模式（详见下文）。

## 光标键模式

插件提供了四种使用光标键的方式：

* 经典（或普通模式）：使用光标键移动光标。
* 对象导航：使用光标键移动到下一个/上一个/父/第一个子对象。
* 网页模式：使用光标键循环切换元素类型并在相应元素之间移动。
* 扫描模式：使用光标键在屏幕上移动对象，而忽略层次结构。

光标键设置为对象导航模式时，有以下快捷键可用：

* 右光标：下一个对象。
* 左光标：上一个对象。
* 上光标：父对象。
* 下光标：第一个子对象。
* 空格或回车：激活。

光标键设置为网页模式时（元素正常或按对象，链接，表单字段，标题，框架，表格，列表，地标移动）：

* 右光标：下一个元素。
* 左光标：上一个元素。
* 上光标：上一个元素类型。
* 下光标：下一个元素类型。
* 空格或回车：激活。

方向键设置为扫描模式时：

* 下光标：下一个对象或下一行。
* 上光标：上一个对象或上一行。
* 右光标：查看下一个字符。
* 左光标：查看上一个字符。
* Ctrl + 右光标: 下一个单词。
* Ctrl+左光标: 上一个单词。
* 空格或回车：激活。

## Version 23.05

* To reflect the maintainer change, the manifest has been updated to
  indicate as such.

## 版本 23.02

* 需要 NVDA 2022.4 或更高版本。
* 需要 Windows 10 21H2（2021 年 11 月更新/内部版本 19044）或更高版本。

## 版本 23.01

* 需要 NVDA 2022.3 或更高版本。
* 需要 Windows 10 或更高版本，因为自 2023 年 1 月起，Microsoft 不再支持 Windows 7、8 和 8.1。

## 版本 22.06

* 需要 NVDA 2021.3 或更高版本。

## 版本21.04

* 需要 NVDA 2020.1 或更高版本。

## 版本20.01

* 需要NVDA 2019.3或更高版本。

## 版本18.12

* 内部更改以支持 NVDA 后续的新版本。

## 版本18.09

* 添加本地化。
* 回车键（大键盘和小键盘上的两个回车键）都可用于激活对象。

## 版本18.03

* 更好地兼容 NVDA 2018.1。

## 版本16.12

* 添加了网页模式。

## 版本16.10

* 发布初始版本。

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
