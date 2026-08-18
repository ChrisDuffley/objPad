# ObjPad

* Auteur : Christopher Duffley <nvda@chrisduffley.com>, à l'origine par Joseph Lee, Cleverson Uliana et autres

Cette extension fournit des commandes rapides pour gérer les objets sur l'écran, incluant la navigation et d'autres possibilités.

## Commandes

* Contrôle+NVDA+TAB : Parcourt les modes touche fléchée (voir ci-dessous pour plus de détails).

## Modes touche fléchée

L'extension offre quatre façons d’utiliser les touches fléchées :

* Classique (ou mode normal) : utiliser les touches fléchées pour déplacer le curseur.
* Navigation par objet : utiliser les touches fléchées pour se déplacer aux objets suivant/précédent/parent/premier enfant.
* Web : utilisez les touches fléchées pour parcourir les éléments et vous déplacer entre eux.
* Mode balayage : utiliser les touches fléchées pour naviguer parmi les objets à l’écran indépendamment de la hiérarchie.

Les commandes suivantes sont disponibles avec les touches fléchées définie pour navigation par objet :

* Flèche droite : objet suivant.
* Flèche gauche : objet précédent.
* Flèche haut : objet parent.
* Flèche bas : premier objet enfant.
* ESPACE ou entrer : activer.

Avec le mode Web actif (les éléments sont normal ou se déplacent par objet, lien, champ de formulaire, titre, cadre, tableau, liste, région) :

* Flèche droite : élément suivant.
* Flèche gauche : élément précédent.
* Flèche haut : type d'élément précédent.
* Flèche bas : type d'élément suivant.
* ESPACE ou entrer : activer.

Avec le mode balayage actif :

* Flèche bas : objet suivant ou ligne suivante.
* Flèche haut : objet précédent ou ligne précédente.
* Flèche droite : visualiser le caractère suivant.
* Flèche gauche : caractère précédent.
* Contrôle + flèche droite : mot suivant.
* Contrôle + flèche gauche : mot précédent.
* ESPACE ou entrer : activer.

## ObjPad settings

In NVDA 2026.2, a dedicated setting is introduced to configure available browse mode navigation elements for use in touch browse mode. With NVDA installed on a touch capable computer, this setting can be found in browse mode settings. On non-touch devices or portable NVDA versions, ObjPad offers this same setting via ObjPad settings interface (part of NVDA settings screen).

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
