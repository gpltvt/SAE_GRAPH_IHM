from modele.motif import Motif

class Grille: # Classe Grille représente la grille 8x8 composee de motifs 

    def __init__(self, donnees_json): # Initialise la grille a partir du dictionnaire
        self.largeur = 8
        self.hauteur = 8
        self.motifs = []
        for nom in donnees_json:
            liste_cases = donnees_json[nom]
            self.motifs.append(Motif(nom, liste_cases))

    def get_motifs(self): # Retourne la liste de tous les motifs de la grille
        return self.motifs

    def get_motif_de_case(self, x, y): # Retourne le motif contenant la case (x, y), ou None si aucun motif ne la contient
        for motif in self.motifs:
            for case in motif.get_cases():
                if case["x"] == x and case["y"] == y:
                    return motif
        return None

    def get_valeur(self, x, y): # Cherche dans tous les motifs la valeur de la case (x, y)
        for motif in self.motifs:
            valeur = motif.get_valeur(x, y)
            if valeur is not None:
                return valeur
        return None

    def set_valeur(self, x, y, v): # Trouve le motif contenant (x, y) et modifie la valeur de cette case
        motif = self.get_motif_de_case(x, y)
        if motif is not None:
            motif.set_valeur(x, y, v)

    def get_voisins(self, x, y): # Retourne la liste des dictionnaires cases voisins en 8 directions
        voisins = []
        for motif in self.motifs:
            for case in motif.get_cases():
                cx = case["x"]
                cy = case["y"]
                if max(abs(cx - x), abs(cy - y)) == 1:  # Reste dans les bornes de la grille
                    if cx >= 0 and cx < self.largeur and cy >= 0 and cy < self.hauteur:
                        voisins.append(case)
        return voisins

    def est_valide(self): # Retourne True si tous les motifs sont valides ET qu'aucune case voisine non vide n'a la même valeur
        for motif in self.motifs:
            if not motif.est_valide():
                return False
        for motif in self.motifs:
            for case in motif.get_cases():
                if case["valeur"] != 0:
                    voisins = self.get_voisins(case["x"], case["y"])
                    for voisin in voisins:
                        if voisin["valeur"] != 0 and voisin["valeur"] == case["valeur"]:
                            return False
        return True

    def cases_vides(self): # Retourne la liste de tous les dictionnaires cases dont la valeur est 0
        vides = []
        for motif in self.motifs:
            for case in motif.get_cases():
                if case["valeur"] == 0:
                    vides.append(case)
        return vides

    def __str__(self): # Affiche la grille 8x8 ligne par ligne, 0 pour les cases sans valeur
        resultat = ""
        for y in range(self.hauteur):
            ligne = ""
            for x in range(self.largeur):
                valeur = self.get_valeur(x, y)
                if valeur is None:
                    ligne = ligne + "0 "
                else:
                    ligne = ligne + str(valeur) + " "
            resultat = resultat + ligne.strip() + "\n"
        return resultat
