from case import Case
from motif import Motif

class Grille: # Représente la grille complète du jeu Néonaure

    def __init__(self, largeur, hauteur, donnees_motifs):
        self.largeur = largeur
        self.hauteur = hauteur
        self.motifs = []
        
        # Initialisation du tableau 2D
        self.cases = []
        for x in range(largeur):
            colonne = []
            for y in range(hauteur):
                colonne.append(None)
            self.cases.append(colonne)
            
        # Construction des cases et motifs
        for nom_motif in donnees_motifs:
            liste_coords = donnees_motifs[nom_motif]
            cases_motif = []
            
            for triplet in liste_coords:
                x = triplet[0]
                y = triplet[1]
                val = triplet[2]
                
                # Vérification des bornes
                if x < 0 or x >= largeur or y < 0 or y >= hauteur:
                    raise ValueError("Case hors grille : (" + str(x) + ", " + str(y) + ")")
                
                # Vérification de doublon
                if self.cases[x][y] is not None:
                    raise ValueError("Doublon detecte aux coordonnees (" + str(x) + ", " + str(y) + ")")
                    
                nouvelle_case = Case(x, y, val)
                self.cases[x][y] = nouvelle_case
                cases_motif.append(nouvelle_case)
                
            nouveau_motif = Motif(cases_motif)
            self.motifs.append(nouveau_motif)

    def get_case(self, x, y): # reenvoyer les coordonne de la case ou rien

        if x < 0 or x >= self.largeur or y < 0 or y >= self.hauteur:
            return None
        return self.cases[x][y]

    def get_motifs(self): # revoie une copie des motifs
        
        copie = []
        for m in self.motifs:
            copie.append(m)
        return copie

    def get_motif_de_case(self, x, y): # renvoie le motif de la case
        for m in self.motifs:
            if m.contient_case(x, y):
                return m
        return None

    def get_voisins(self, x, y): # renvoie les cases voisines en 8 directions
        voisins = []
        # Boucle de -1 à 1 pour dx et dy
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                # Vérification des bornes
                if nx >= 0 and nx < self.largeur and ny >= 0 and ny < self.hauteur:
                    voisine = self.cases[nx][ny]
                    if voisine is not None:
                        voisins.append(voisine)
        return voisins

    def est_grille_valide(self): # revoie si la grille est valide
        for m in self.motifs:
            if not m.est_valide():
                return False
                
        # Vérification des voisinages
        for x in range(self.largeur):
            for y in range(self.hauteur):
                c = self.cases[x][y]
                if c is not None:
                    if not c.est_vide():
                        val_c = c.valeur
                        voisins = self.get_voisins(x, y)
                        for voisin in voisins:
                            if not voisin.est_vide() and voisin.valeur == val_c:
                                return False
        return True

    def get_cases_vides(self): # revoie les cases vides
        vides = []
        for y in range(self.hauteur):
            for x in range(self.largeur):
                c = self.cases[x][y]
                if c is not None:
                    if c.valeur == 0:
                        vides.append(c)
        return vides

    def __str__(self): # affiche la grille
        res = "Grille " + str(self.largeur) + "x" + str(self.hauteur) + " :\n"
        for y in range(self.hauteur):
            for x in range(self.largeur):
                c = self.cases[x][y]
                if c is None:
                    res += "?"
                else:
                    res += str(c.valeur)
                if x < self.largeur - 1:
                    res += " "
            res += "\n"
        return res
