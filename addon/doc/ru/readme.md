# ObjPad #

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph
  Lee, Cleverson Uliana and others
* Загрузить [стабильную версию][1]
* NVDA compatibility: 2022.4 and later

Данное дополнение обеспечивает горячие клавиши для управления объектами на
экране, включая навигацию и другие возможности.

## Команды

* Control+NVDA+TAB: переключение между режимами управления стрелками
  (см. ниже).

## Режимы управления стрелками

Дополнение предоставляет четыре способа использования клавиш со стрелками:

* Классический (или обычный режим): клавиши стрелок взаимодействуют с
  системным курсором.
* ОБъектный навигатор: клавиши стрелок позволяют перемещаться по следующему,
  предыдущему, родительскому и первому дочернему элементам.
* Веб: Используйте клавиши со стрелками для перебора элементов и перемещения
  между ними.
* Режим сканирования: клавиши стрелок позволяют перемещаться по элементам на
  экране независимо от их иерархии.

В режиме объектного навигатора, клавиши со стрелками выполняют следующие
команды:

* Стрелка вправо: следующий объект.
* Стрелка влево: предыдущий объект.
* Стрелка вверх: родительский объект.
* Стрелка вниз: первый дочерний объект.
* SPACE or ENTER: activate.

При активном веб-режиме (элементы нормальные или передвижение по объектам,
ссылка, форма, поле, заголовок, фрейм, таблица, список, ориентир):

* Стрелка вправо: следующий элемент.
* Стрелка влево: предыдущий элемент.
* Стрелка вверх: предыдущий тип элемента.
* Стрелка вниз: следующий тип элемента.
* SPACE or ENTER: activate.

В режиме сканирования:

* Down arrow: next object or the next line.
* Up arrow: previous object or previous line.
* Стрелка вправо: перейти к следующему символу на объекте.
* Стрелка влево: перейти к предыдущему символу на объекте.
* Control+right arrow: next word.
* Control+left arrow: previous word.
* SPACE or ENTER: activate.

## Version 23.05

* To reflect the maintainer change, the manifest has been updated to
  indicate as such.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## Version 22.06

* Requires NVDA 2021.3 or later.

## Version 21.04

* Requires NVDA 2020.1 or later.

## Version 20.01

* Requires NVDA 2019.3 or later.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.09

* Added localizations.
* Enter key (regular and Numpad) can be used to activate objects.

## Версия 18.03

* Улучшена Совместимость с NVDA 2018.1.

## Версия 16.12

* Добавлен веб-режим.

## Версия 16.10

* Первая стабильная версия.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
