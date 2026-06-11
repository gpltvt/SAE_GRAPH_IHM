# -*- coding: utf-8 -*-
# Vue de la grille pour le jeu Néonaure
# Couche Vue - passe uniquement par le contrôleur, jamais par le modèle directement

from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

class VueGrille(QWidget):

    def __init__(self, controleur): # Initialise la vue avec le contrôleur et crée les 64 boutons
        super().__init__()
        self.controleur = controleur

        # Création du layout grille avec espacement 0 et marges 10px
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)
        self.setStyleSheet("background-color: #F0F0F0;")
        self.setFixedSize(8 * 60 + 20, 8 * 60 + 20)

        # Création des 64 boutons stockés dans un dictionnaire clé (x, y)
        self.boutons = {}
        for y in range(8):
            for x in range(8):
                btn = QPushButton("")
                btn.setFixedSize(60, 60)
                # Connexion du clic en capturant x et y dans une fonction lambda
                btn.clicked.connect(self._creer_callback_clic(x, y))
                self.boutons[(x, y)] = btn
                layout.addWidget(btn, y, x)

        # Premier affichage de la grille
        self.rafraichir_affichage()

    def _creer_callback_clic(self, x, y): # Crée une fonction de rappel pour le clic sur la case (x, y)
        # Nécessaire pour capturer correctement x et y dans la boucle
        def callback():
            self.clic_sur_case(x, y)
        return callback

    def clic_sur_case(self, x, y): # Gère le clic sur la case (x, y) : donne le focus et rafraîchit
        self.boutons[(x, y)].setFocus()
        self.rafraichir_affichage()

    def keyPressEvent(self, event): # Gère l'appui sur une touche clavier pour modifier la case ayant le focus
        # Recherche de la case qui a le focus
        x_focus = -1
        y_focus = -1
        for y in range(8):
            for x in range(8):
                if self.boutons[(x, y)].hasFocus():
                    x_focus = x
                    y_focus = y

        # Si aucune case n'a le focus, on ne fait rien
        if x_focus == -1:
            return

        # Lecture de la touche pressée
        touche = event.key()
        texte = event.text()

        # Backspace ou Delete ou "0" : efface la valeur
        if touche == Qt.Key.Key_Backspace or touche == Qt.Key.Key_Delete or texte == "0":
            self.controleur.set_valeur_case(x_focus, y_focus, 0)
            self.rafraichir_affichage()
        # Chiffre entre 1 et 8 : place la valeur
        elif texte == "1" or texte == "2" or texte == "3" or texte == "4" or texte == "5" or texte == "6" or texte == "7" or texte == "8":
            chiffre = int(texte)
            self.controleur.set_valeur_case(x_focus, y_focus, chiffre)
            self.rafraichir_affichage()

    def rafraichir_affichage(self): # Met à jour l'affichage de tous les boutons selon l'état du contrôleur
        for y in range(8):
            for x in range(8):
                btn = self.boutons[(x, y)]
                valeur = self.controleur.get_valeur_case(x, y)

                # Affichage du texte du bouton (vide si 0)
                if valeur == 0:
                    btn.setText("")
                else:
                    btn.setText(str(valeur))

                # Calcul des 4 bordures
                # Bordure haute
                if y == 0 or not self.controleur.memes_motifs(x, y, x, y - 1):
                    bordure_haut = "3px solid black"
                else:
                    bordure_haut = "1px solid #AAAAAA"

                # Bordure basse
                if y == 7 or not self.controleur.memes_motifs(x, y, x, y + 1):
                    bordure_bas = "3px solid black"
                else:
                    bordure_bas = "1px solid #AAAAAA"

                # Bordure gauche
                if x == 0 or not self.controleur.memes_motifs(x, y, x - 1, y):
                    bordure_gauche = "3px solid black"
                else:
                    bordure_gauche = "1px solid #AAAAAA"

                # Bordure droite
                if x == 7 or not self.controleur.memes_motifs(x, y, x + 1, y):
                    bordure_droite = "3px solid black"
                else:
                    bordure_droite = "1px solid #AAAAAA"

                # Détermination de la couleur de fond et du style de texte
                if self.controleur.case_est_fixe(x, y):
                    # Case fixe imposée par le puzzle
                    fond = "#D0D0D0"
                    style_texte = "color: black; font-weight: bold; font-size: 18px;"
                elif not self.controleur.case_est_valide(x, y) and valeur != 0:
                    # Case en erreur (contrainte de voisinage violée)
                    fond = "#FFAAAA"
                    style_texte = "color: black; font-weight: bold; font-size: 18px;"
                elif btn.hasFocus():
                    # Case sélectionnée
                    fond = "#E2EFFF"
                    style_texte = "color: black; font-weight: bold; font-size: 18px;"
                else:
                    # Case normale
                    fond = "white"
                    style_texte = "color: black; font-weight: bold; font-size: 18px;"

                # Construction du stylesheet en une seule chaîne par concaténation
                feuille = "QPushButton {"
                feuille = feuille + "background-color: " + fond + ";"
                feuille = feuille + style_texte
                feuille = feuille + "border-top: " + bordure_haut + ";"
                feuille = feuille + "border-bottom: " + bordure_bas + ";"
                feuille = feuille + "border-left: " + bordure_gauche + ";"
                feuille = feuille + "border-right: " + bordure_droite + ";"
                feuille = feuille + "}"

                btn.setStyleSheet(feuille)
