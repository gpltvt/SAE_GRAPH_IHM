# -*- coding: utf-8 -*-
# Point d'entrée du jeu Néonaure

import sys
import os

from PyQt6.QtWidgets import QApplication

from controleur import Controleur

from vue.vue_fenetre import FenetrePrincipale

# Création et lancement de l'application PyQt6
app = QApplication(sys.argv)
controleur = Controleur()
fenetre = FenetrePrincipale(controleur)
fenetre.show()
app.exec()
