# SAE_GRAPH_IHM

Projet en cours dans le cadre de la SAÉ R2-02 et R2-07 (année 2025-2026).

Objectif: Concevoir et développer une application complète en Python pour jouer au jeu du **Néonaure**, une variante du Sudoku.

## Membres de l'équipe:
* **Roba Ethan**
* **Laniez Gabriel**
* **Plaetevoet Gaëlle**

## Cloner le dépôt:
git clone https://github.com/gpltvt/SAE_GRAPH_IHM.git

## Construction des fichiers JSON
**Motifs :** identifiant unique pour un motif de la grille. Chaque valeur associée est une liste de coordonnées qui représente les cases composants le motif.

**Case :** X, c'est l'index de la colonne. Y, c'est l'index de la ligne. Valeur, c'est l'indice de départ de la case. Si au début du jeu le troisième chiffre est 0, alors la case est vide. Si le troisième chiffre est autre que 0, alors c'est un chiffre fixe.

**Dimensions de la grille :** La grille est carée, avec 64 cases (donc 8x8).

**Valeurs d'un motif :** un motif de N cases doit comporter tous les chiffres de 1 à N. 
