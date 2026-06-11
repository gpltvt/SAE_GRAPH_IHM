# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from vue.vue_grille import VueGrille

class FenetrePrincipale(QMainWindow): #la class fenetre principale
    def __init__(self, controleur): #Initialise la fenetre principale avec le contrôleur
        super().__init__()
        self.controleur = controleur
        
        self.setWindowTitle("NÃ©onaure - Jeu de Grille")
        self.resize(520, 580)
        
        barre_menu = self.menuBar()
        menu_fichier = barre_menu.addMenu("Fichier")
        
        action_charger = menu_fichier.addAction("Charger une grille")
        action_sauvegarder = menu_fichier.addAction("Sauvegarder")
        action_quitter = menu_fichier.addAction("Quitter")
        
        action_charger.triggered.connect(self.controleur.charger_partie)
        action_quitter.triggered.connect(self.close)
        
        self.vue_grille = VueGrille(self.controleur)
        self.setCentralWidget(self.vue_grille)