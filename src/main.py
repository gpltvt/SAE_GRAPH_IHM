# Jeu Néonaure
import sys
from PyQt6.QtWidgets import QApplication
from controleur import Controleur
from vue.vue_fenetre import FenetrePrincipale

# Création et lancement de l'application PyQt6
app = QApplication(sys.argv)

# Thème néon
app.setStyleSheet(
    "QMainWindow { background-color: #0d0b1e; } "
    "QMenuBar { background-color: #0d0b1e; color: #c084fc; font-size: 13px; } "
    "QMenuBar::item:selected { background-color: #2d1b4e; } "
    "QMenu { background-color: #1a1635; color: #e2e8f0; border: 1px solid #a855f7; } "
    "QMenu::item:selected { background-color: #2d1b4e; }"
)

controleur = Controleur()
fenetre = FenetrePrincipale(controleur)
controleur.set_vue(fenetre)
fenetre.show()
sys.exit(app.exec())