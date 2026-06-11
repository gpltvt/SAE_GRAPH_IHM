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

## Avancées du projet:
* **Architecture MVC:** séparation entre le modèle de données et les vues.
* **Détection de la victoire:** validation dès que la grille est complète et correcte.

## Interface graphique:
* **Grille:** rendu visuel en mettant en évidence les contours et bordures.
* **Assistance visuelle:** les cases de départ sont fixées et légèrement plus sombres. Les cases incorrectes passent en rouge. La case sélectionnée est mise en valeur.
* **Barre des menus:** intégration des actions de fichiers et de grille

## Gestion des données:
* **Chargement et sauvegarde:** importation et exportation possibles au format JSON.

## Partie IA & algorithmique:
* **Solveur automatique:** algorithme de Backtracking récursif qui analyse/trie les cases vides par taille de motif pour accélérer la résolution.
* **Contrôle de flux:** intégration de processEvents() pour éviter le plantage.
* **Réinitialisation de la grille:** permet de vider la grille sans effacer les cases fixées du départ.
