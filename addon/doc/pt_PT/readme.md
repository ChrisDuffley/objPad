# ObjPad

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others

Este extra fornece comandos rápidos para gerir objetos no ecrã, incluindo navegação e outras possibilidades.

## Comandos:

* Control+NVDA+TAB: deslocamentos através dos modos de tecla de seta (veja abaixo detalhes).

## Modos das teclas de setas:

O extra apresenta quatro maneiras para usar as teclas de setas:

* Clássico (ou modo normal): usa as teclas de seta para mover o cursor.
* Navegação por objectos: usa as teclas de seta para mover para os objetos seguintes / anteriores / pai / primeiro filho.
* Web: use as setas para percorrer os elementos e mover-se entre eles.
* Modo de varredura: use as setas para se mover entre os objetos no ecrã, independentemente da hierarquia.

Os seguintes comandos estão disponíveis com as teclas de seta definidas para a navegação por objectos:

* Seta para a direita: próximo objecto.
* Seta para a esquerda: objecto anterior.
* Seta para cima: objecto pai.
* Seta para baixo: primeiro objecto filho.
* ESPAÇO ou enter: activar.

Com o modo web activo (os elementos são normais ou em movimento por objecto, link, campo do formulário, título, quadro, tabela, lista, marcador):

* Seta para a direita: próximo elemento.
* Seta para a esquerda: elemento anterior.
* Seta para cima: tipo de elemento anterior.
* Seta para baixo: próximo tipo de elemento.
* ESPAÇO ou enter: activar.

Com o modo de varredura activo:

* Seta para baixo: próximo objecto ou próxima linha.
* Seta para cima: objecto anterior ou linha anterior.
* Seta para a direita: ver o próximo caracter.
* Left arrow: caracter anterior.
* CTRL+seta para a direita: próxima palavra.
* CTRL+seta para a esquerda: palavra anterior.
* ESPAÇO ou enter: activar.

## ObjPad settings

In NVDA 2026.2, a dedicated setting is introduced to configure available browse mode navigation elements for use in touch browse mode. With NVDA installed on a touch capable computer, this setting can be found in browse mode settings. On non-touch devices or portable NVDA versions, ObjPad offers this same setting via ObjPad settings interface (part of NVDA settings screen).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
