# ObjPad #

* Author: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph
  Lee, Cleverson Uliana and others
* Baixe a [versão estável][1]
* NVDA compatibility: 2022.4 and later

Esse complemento fornece comandos rápidos para gerenciar objetos na tela,
incluindo navegação e outras possibilidades.

## Comandos

* Control+NVDA+TAB: Percorre os modos de teclas de seta (veja abaixo para
  detalhes).

## Modos das teclas de seta

O complemento apresenta quatro maneiras para usar as teclas de seta:

* Clássico (ou modo normal): usa as setas para mover o cursor.
* Navegação por objeto: usa as teclas de seta para ir para os objetos
  próximo/anterior/pai/primeiro filho.
* Web: usa as setas para percorrer os elementos e mover-se entre eles.
* Modo de esquadrinhamento: usa as teclas de seta para percorrer os objetos
  na tela, independentemente da hierarquia.

Os seguintes comandos estão disponíveis com as teclas de seta configuradas
para navegação por objeto:

* Seta para direita: próximo objeto.
* Seta para esquerda: objeto anterior.
* Seta para cima: objeto pai.
* Seta para baixo: primeiro objeto filho.
* ESPAÇO ou ENTER: ativar.

Com o modo Web ativo (os elementos são normais ou movendo-se por objeto,
link, campo de formulário, título, frame, tabela, lista, marco):

* Seta para direita: próximo elemento.
* Seta para esquerda: elemento anterior.
* Seta para cima: tipo de elemento anterior.
* Seta para baixo: próximo tipo de elemento.
* ESPAÇO ou ENTER: ativar.

Com o modo de esquadrinhamento ativo:

* Seta para baixo: próximo objeto ou próxima linha.
* Seta para cima: objeto anterior ou linha anterior.
* Seta para direita: explora próximo caractere.
* Seta para esquerda: caractere anterior.
* CTRL+seta para direita: próxima palavra.
* CTRL+seta para esquerda: palavra anterior.
* ESPAÇO ou ENTER: ativar.

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

## Versão 21.04

* Requer NVDA 2020.1 ou posterior.

## Versão 20.01

* Requer NVDA 2019.3 ou posterior.

## Versão 18.12

* Alterações internas para dar suporte a versões futuras do NVDA.

## Versão 18.09

* Adicionado localizações.
* A tecla Enter (regular e bloco numérico) pode ser usada para ativar
  objetos.

## Versão 18.03

* Melhor compatibilidade com o NVDA 2018.1.

## Versão 16.12

* Adicionado modo web.

## Versão 16.10

* Versão inicial estável.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
