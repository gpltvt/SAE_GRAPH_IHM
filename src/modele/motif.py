class Motif: # Représente un motif de la grille, ces genre un groupe de N cases qui doit contenir les valeurs de 1 à N sans répétition

    def __init__(self, cases):
        self.cases = []
        for c in cases:
            self.cases.append(c)
        self.n = len(self.cases)

    def get_cases(self): # revoie une copie de la liste des cases du motif
        
        copie = []
        for c in self.cases:
            copie.append(c)
        return copie

    def get_n(self):# revoie la taille du motif
        
        return self.n

    def contient_case(self, x, y): # revoie true si le motif contient une case aux coordonnees (x,y)
        for c in self.cases:
            if c.x == x and c.y == y:
                return True
        return False

    def get_cases_vides(self): # revoie les cases vides
        vides = []
        for c in self.cases:
            if c.valeur == 0:
                vides.append(c)
        return vides

    def est_valide(self): # revoie true si le motif est valide, c'est-à-dire si toutes les cases sont pas vides et que les valeurs forment exactement {1..N} sans répétition.
        
        vus = [False] * (self.n + 1) 
        for c in self.cases:
            if c.est_vide():
                return False
            val = c.valeur
            if val < 1 or val > self.n:
                return False
            if vus[val]:
                return False # si doublons
            vus[val] = True
        return True

    def __str__(self): # affiche le motif
        
        res = "Motif(n=" + str(self.n) + ") ["
        for i in range(len(self.cases)):
            c = self.cases[i]
            res += "(" + str(c.x) + "," + str(c.y) + ")=" + str(c.valeur)
            if i < len(self.cases) - 1:
                res += ", "
        res += "]"
        return res
