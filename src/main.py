# Point d'entrée du jeu Néonaure
import sys
from PyQt6.QtWidgets import QApplication
from controleur import Controleur
from vue.vue_fenetre import FenetrePrincipale

# Création et lancement de l'application PyQt6
app = QApplication(sys.argv)
controleur = Controleur()
fenetre = FenetrePrincipale(controleur)
controleur.set_vue(fenetre)
fenetre.show()
sys.exit(app.exec())