# ObjPad-NVDA对象管理导航插件 #

* 作者: Joseph Lee, Cleverson Uliana and others
* 下载 [稳定版][1]
* 下载 [开发板][2]

此插件提供快捷键来管理屏幕上的对象，包括导航和其他可能性。

## 快捷键

* Control + NVDA + TAB：逐步执行光标键模式（详见下文）。

## 光标键模式

插件提供了四种使用光标键的模式：

* 经典（或普通模式）：使用光标键移动光标。
* 对象导航：使用光标键移动到下一个/上一个/父/第一个子对象。
* Web：使用光标键循环元素并在元素之间移动。
* 扫描模式：使用光标键在屏幕上移动对象，而不管层次结构如何。

光标键设置为对象nav时，以下命令可用：

* 右光标：下一个对象。
* 左光标：上一个对象。
* 上光标：父对象。
* 下光标：第一个子对象。
* 空格：激活。

在Web模式处于活动状态（元素正常或按对象，链接，表单字段，标题，框架，表格，列表，地标移动）：

* 右光标：下一个元素。
* 左光标：上一个元素。
* 上光标：上一个元素类型。
* 下光标：下一个元素类型。
* 空格：激活。

扫描模式激活时：

* Down arrow: next object.
* Up arrow: previous object.
* Right arrow: review next character.
* Left arrow: previous character.
* 空格：激活。

## Version 18.03

* Better compatibility with NVDA 2018.1.

## 版本16.12

* 添加了网络模式。

## 版本16.10

* 发布初始版本

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=objPad

[2]: https://addons.nvda-project.org/files/get.php?file=objPad-dev
