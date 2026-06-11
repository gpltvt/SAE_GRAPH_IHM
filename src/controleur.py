# -*- coding: utf-8 -*-
# Contrôleur du jeu Néonaure - fait le lien entre la Vue et le Modèle

import json
import os

from modele.grille import Grille

class Controleur:

    def __init__(self): # Charge grille1.json et crée l'objet Grille
        # Chemin vers grille1.json situé dans le même dossier que ce script
        chemin = os.path.join(os.path.dirname(__file__), "grille1.json")
        fichier = open(chemin)
        donnees_json = json.load(fichier)
        fichier.close()
        self.grille = Grille(donnees_json)

    def get_valeur_case(self, x, y): # Retourne la valeur de la case (x, y), 0 si vide ou absente
        valeur = self.grille.get_valeur(x, y)
        if valeur is None:
            return 0
        return valeur

    def set_valeur_case(self, x, y, v): # Modifie la valeur de la case (x, y)
        self.grille.set_valeur(x, y, v)

    def memes_motifs(self, x1, y1, x2, y2): # Retourne True si les deux cases appartiennent au même motif
        motif1 = self.grille.get_motif_de_case(x1, y1)
        motif2 = self.grille.get_motif_de_case(x2, y2)
        return motif1 is motif2

    def case_est_fixe(self, x, y): # Retourne True si la case est imposée par le puzzle - à compléter plus tard
        return False

    def case_est_valide(self, x, y): # Retourne True si la case ne viole pas les contraintes - à compléter plus tard
        return True

    def charger_partie(self): # Charge une nouvelle partie depuis un fichier JSON - à compléter plus tard
        pass
