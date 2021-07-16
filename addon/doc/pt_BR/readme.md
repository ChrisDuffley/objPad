# ObjPad #

* Autor: Joseph Lee, Cleverson Uliana e outros
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]
* Compatibilidade com NVDA: 2020.1 a 2020.4

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

[1]: https://addons.nvda-project.org/files/get.php?file=objPad

[2]: https://addons.nvda-project.org/files/get.php?file=objPad-dev