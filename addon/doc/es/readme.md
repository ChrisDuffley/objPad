# ObjPad #

* Autores: Christopher Duffley <nvda@chrisduffley.com>, originalmente Joseph
  Lee, Cleverson Uliana y otros
* Descargar [versión estable][1]
* Compatibilidad con NVDA: de 2022.4 en adelante

Este complemento proporciona órdenes rápidas para gestionar objetos en
pantalla, incluyendo la navegación y otras posibilidades.

## Órdenes

* Control+NVDA+TAB: pasos a través de los modos de teclas de flechas
  (consulta abajo para detalles).

## Modos de teclas de flechas

El complemento proporciona cuatro formas de utilizar las flechas:

* Clássico (o modo normal): utiliza las flechas para mover el cursor.
* Navegación de objetos: utiliza las flechas para mover a los objetos
  siguiente/anterior/padre/primer hijo.
* Web: utiliza las teclas de flechas para recorrer los elementos y moverte
  entre ellos.
* Modo escanear: utiliza las flechas para moverte a través de los objetos en
  pantalla independientemente de la jerarquía.

Las siguientes órdenes están disponibles con las flechas puestas en
Navegación de objetos:

* Flecha derecha: objeto siguiente.
* Flecha izquierda: objeto anterior.
* Flecha arriba: objeto padre.
* Flecha abajo: primer objeto hijo.
* Espacio o intro: activar.

Con el modo web activo (los elementos son normal o se mueven por objeto,
enlace, campo de formulario, encabezado, marco, tabla, lista, punto de
referencia):

* Flecha derecha: elemento siguiente.
* Flecha izquierda: elemento anterior.
* Flecha arriba: tipo de elemento anterior.
* Flecha abajo: tipo de elemento siguiente.
* Espacio o intro: activar.

Con el modo escanear activo:

* Flecha abajo: objeto o línea siguiente.
* Flecha arriba: objeto o línea anterior.
* Flecha derecha: revisar carácter siguiente.
* Flecha izquierda: revisar carácter anterior.
* Control+Flecha derecha: palabra siguiente.
* Control+Flecha izquierda: palabra anterior.
* Espacio o intro: activar.

## Versión 23.05

* Para reflejar el cambio de responsable de mantenimiento, se ha actualizado
  el manifiesto indicando tal situación.

## Versión 23.02

* Se requiere NVDA 2022.4 o posterior.
* Se requiere Windows 10 21H2 (actualización de noviembre de 2021 /
  compilación 19044) o posterior.

## Versión 23.01

* Se requiere NVDA 2022.3 o posterior.
* Se requiere Windows 10 o posterior, ya que Microsoft no soporta Windows 7,
  8 y 8.1 a partir de enero de 2023.

## Versión 22.06

* Se requiere NVDA 2021.3 o posterior.

## Versión 21.04

* Se requiere NVDA 2020.1 o posterior.

## Versión 20.01

* Se requiere NVDA 2019.3 o posterior.

## Versión 18.12

* Cambios internos para dar soporte a versiones futuras de NVDA.

## Versión 18.09

* Añadidas traducciones.
* La tecla intro (normal y numérica) puede utilizarse para activar objetos.

## Versión 18.03

* Mejor compatibilidad con NVDA 2018.1.

## Versión 16.12

* Añadido el modo web.

## Versión 16.10

* Versión estable inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=objPad
