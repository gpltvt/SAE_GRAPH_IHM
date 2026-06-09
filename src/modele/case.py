class Case:
    def __init__(self, x, y, valeur):    # une case individuelle de la grille.

        self.x = x
        self.y = y
        self.valeur = valeur
        if valeur != 0:
            self.fixe = True
        else:
            self.fixe = False

    def est_vide(self): # reenvoyer true si la case n'a pas de valeur
        if self.valeur == 0:
            return True
        else:
            return False

    def set_valeur(self, v):# modifie la valeur de la case
        if self.fixe:
            raise ValueError("Impossible de modifier une case fixe.")
        self.valeur = v

    def effacer(self):# remet la valeur de la case à 0
        if self.fixe:
            raise ValueError("Impossible d'effacer une case fixe.")
        self.valeur = 0

    def est_voisine(self, autre):# revoie true si deux cases sont voisines
        if max(abs(self.x - autre.x), abs(self.y - autre.y)) == 1:
            return True
        else:
            return False

    def __str__(self):  # affichage de la case

        etat = ""
        if self.fixe:
            etat = "[FIXE]"
        elif self.valeur == 0:
            etat = "[vide]"
        else:
            etat = "[edite]"
            
        return "Case(" + str(self.x) + "," + str(self.y) + ")=" + str(self.valeur) + etat
