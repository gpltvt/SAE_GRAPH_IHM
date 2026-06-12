from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

class VueGrille(QWidget): #la class vue grille

    def __init__(self, controleur): # Initialise la vue avec le contrôleur et cree les 64 case
        super().__init__()
        self.controleur = controleur

        # Creation du layout grille avec espacement tout coller 
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)
        self.setStyleSheet("background-color: #0d0b1e;")
        self.setFixedSize(8 * 60 + 20, 8 * 60 + 20)

        # Creation des 64 boutons stockes dans un dictionnaire cle (x, y)
        self.boutons = {}
        for y in range(8):
            for x in range(8):
                btn = QPushButton("")
                btn.setFixedSize(60, 60)
                btn.clicked.connect(self._creer_callback_clic(x, y))# Connexion du clic en capturant x et y dans une fonction lambda
                self.boutons[(x, y)] = btn
                layout.addWidget(btn, y, x)

        # Premier affichage de la grille
        self.rafraichir_affichage()

    def _creer_callback_clic(self, x, y): # Cree une fonction de rappel pour le clic sur la case (x, y)
        # Pour capturer correctement x et y dans la boucle
        def callback():
            self.clic_sur_case(x, y)
        return callback

    def clic_sur_case(self, x, y): # Gere le clic sur la case (x, y) 
        self.boutons[(x, y)].setFocus()
        self.rafraichir_affichage()

    def keyPressEvent(self, event): # Gere l'appui sur une touche clavier pour modifier la case 
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

        # Lecture de la touche appuyer
        touche = event.key()
        texte = event.text()

        # efface la valeur
        if touche == Qt.Key.Key_Backspace or touche == Qt.Key.Key_Delete or texte == "0":
            self.controleur.set_valeur_case(x_focus, y_focus, 0)
            self.rafraichir_affichage()
        # Chiffre entre 1 et 5 : place la valeur
        elif texte == "1" or texte == "2" or texte == "3" or texte == "4" or texte == "5": 
            chiffre = int(texte)
            self.controleur.set_valeur_case(x_focus, y_focus, chiffre)
            self.rafraichir_affichage()

    def rafraichir_affichage(self): # Met à jour l'affichage de tous les boutons selon l'etat du contrôleur
        for y in range(8):
            for x in range(8):
                btn = self.boutons[(x, y)]
                valeur = self.controleur.get_valeur_case(x, y)

                # Affichage du texte du bouton (vide si 0)
                if valeur == 0:
                    btn.setText("")
                else:
                    btn.setText(str(valeur))

                # Bordure haute epaisse si bord de grille ou changement de motif
                if y == 0 or not self.controleur.memes_motifs(x, y, x, y - 1):
                    bordure_haut = "3px solid #a855f7"
                else:
                    bordure_haut = "1px solid #2d2b52"

                # Bordure basse epaisse si bord de grille ou changement de motif
                if y == 7 or not self.controleur.memes_motifs(x, y, x, y + 1):
                    bordure_bas = "3px solid #a855f7"
                else:
                    bordure_bas = "1px solid #2d2b52"

                # Bordure gauche epaisse si bord de grille ou changement de motif
                if x == 0 or not self.controleur.memes_motifs(x, y, x - 1, y):
                    bordure_gauche = "3px solid #a855f7"
                else:
                    bordure_gauche = "1px solid #2d2b52"

                # Bordure droite epaisse si bord de grille ou changement de motif
                if x == 7 or not self.controleur.memes_motifs(x, y, x + 1, y):
                    bordure_droite = "3px solid #a855f7"
                else:
                    bordure_droite = "1px solid #2d2b52"

                # Priorite 1 case fixe
                if self.controleur.case_est_fixe(x, y):
                    fond = "#120a2e"
                    couleur_texte = "#e879f9"
                    poids = "bold"
                    taille_police = "20px"
                # Priorite 2 valeur saisie mais invalide
                elif valeur != 0 and not self.controleur.case_est_valide(x, y):
                    fond = "#4a0f0f"
                    couleur_texte = "#ff2d78"
                    poids = "bold"
                    taille_police = "18px"
                # Priorite 3 : case selectionnee
                elif btn.hasFocus():
                    fond = "#3b1f6b"
                    couleur_texte = "#67e8f9"
                    poids = "bold"
                    taille_police = "18px"
                # Priorite 4 : case saisie valide
                elif valeur != 0:
                    fond = "#1a1635"
                    couleur_texte = "#22d3ee"
                    poids = "normal"
                    taille_police = "18px"
                # Priorite 5 : case vide editable
                else:
                    fond = "#1a1635"
                    couleur_texte = "#e2e8f0"
                    poids = "normal"
                    taille_police = "18px"

                # Construction de la feuille de style 
                feuille = "QPushButton {"
                feuille = feuille + "background-color: " + fond + ";"
                feuille = feuille + "color: " + couleur_texte + ";"
                feuille = feuille + "font-weight: " + poids + ";"
                feuille = feuille + "font-size: " + taille_police + ";"
                feuille = feuille + "font-family: Consolas, Courier New, monospace;"
                feuille = feuille + "border-top: " + bordure_haut + ";"
                feuille = feuille + "border-bottom: " + bordure_bas + ";"
                feuille = feuille + "border-left: " + bordure_gauche + ";"
                feuille = feuille + "border-right: " + bordure_droite + ";"
                feuille = feuille + "}"

                btn.setStyleSheet(feuille)

