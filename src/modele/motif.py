class Motif: # Classe Motif représentant un groupe de cases devant contenir les valeurs 1 à N sans répétition
    def __init__(self, nom, liste_cases): # Initialise le motif avec son nom et la liste de ses cases
        self.nom = nom
        self.cases = []
        for case in liste_cases:
            self.cases.append({"x": case[0], "y": case[1], "valeur": case[2]})
        self.n = len(self.cases)

    def get_cases(self): # Retourne la liste des dictionnaires cases du motif
        return self.cases

    def get_n(self): # Retourne le nombre de cases du motif
        return self.n

    def get_valeur(self, x, y):# Retourne la valeur de la case (x, y) dans ce motif, ou None si absente
        for case in self.cases:
            if case["x"] == x and case["y"] == y:
                return case["valeur"]
        return None

    def set_valeur(self, x, y, v): # Modifie la valeur de la case (x, y) dans ce motif
        for case in self.cases:
            if case["x"] == x and case["y"] == y:
                case["valeur"] = v

    def est_valide(self): # Retourne True si toutes les cases sont non vides et contiennent exactement les valeurs 1 à N sans répétition
        vus = [False] * (self.n + 1)
        for case in self.cases:
            valeur = case["valeur"]
            if valeur == 0:
                return False
            if valeur < 1 or valeur > self.n:
                return False
            if vus[valeur]:
                return False
            vus[valeur] = True
        return True

    def __str__(self): # Affichage simple du motif pour le débogage
        resultat = "Motif " + self.nom + " (n=" + str(self.n) + ") :\n"
        for case in self.cases:
            resultat = resultat + "  (" + str(case["x"]) + ", " + str(case["y"]) + ") = " + str(case["valeur"]) + "\n"
        return resultat
