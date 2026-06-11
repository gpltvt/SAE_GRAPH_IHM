import json
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QCoreApplication
from modele.grille import Grille

# Classe représentant le contrôleur de l'application (Architecture MVC)
# Elle fait le lien entre le modèle et la vue 
class Controleur:
    def __init__(self):
        # Initialisation des attributs essentiels du contrôleur
        self.grille = None                      
        self.cases_fixes = set()                
        self.vue_principale = None              
        self.en_cours_de_resolution = False

    def set_vue(self, vue):
        # Permet d'associer la vue principale au contrôleur après son instanciation
        self.vue_principale = vue

    def sauvegarder_partie(self):
        # Si aucune grille n'est chargée, on annule l'action
        if not self.grille:
            return
            
        # Ouverture de l'explorateur pour choisir l'emplacement et le nom du fichier de sauvegarde
        fichier, _ = QFileDialog.getSaveFileName(
            self.vue_principale, "Sauvegarder la grille", "", "Fichiers JSON (*.json)"
        )
        
        if fichier:
            donnees = {}
            # Parcours de tous les motifs pour extraire l'état actuel de la grille
            for motif in self.grille.get_motifs():
                liste_cases = []
                for case in motif.get_cases():
                    x, y = case["x"], case["y"]
                    # Détermination si la case fait partie des indices fixés du départ
                    est_fixe = (x, y) in self.cases_fixes
                    # Stockage des coordonnées, de la valeur actuelle et de la nature de la case
                    liste_cases.append([x, y, case["valeur"], est_fixe])
                donnees[motif.nom] = liste_cases
            
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=4)
                
            # Mise à jour du message de statut dans l'IHM
            if self.vue_principale:
                self.vue_principale.changer_message_statut("Grille sauvegardée.", "#555555")

    def charger_partie(self):
        # Ouverture de l'explorateur pour sélectionner un fichier de grille JSON valide
        fichier, _ = QFileDialog.getOpenFileName(
            self.vue_principale, "Charger une grille", "", "Fichiers JSON (*.json)"
        )
        if fichier:
            # Lecture et décodage du fichier JSON
            with open(fichier, 'r', encoding='utf-8') as f:
                donnees = json.load(f)
            
            # Instanciation d'une nouvelle grille dans le modèle avec les données lues
            self.grille = Grille(donnees)
            # Réinitialisation de l'ensemble des cases verrouillées
            self.cases_fixes.clear() 
            
            # Identification des cases de départ  pour bloquer leur saisie par le joueur
            for nom_motif, liste_cases in donnees.items():
                for case in liste_cases:
                    x, y, valeur = case[0], case[1], case[2]
                    # Si le booléen indiquant la nature fixe de la case est fourni dans le fichier
                    if len(case) > 3:
                        est_fixe = case[3]
                        if est_fixe:
                            self.cases_fixes.add((x, y))
                    else:
                        # Par défaut toute case initialisée avec un chiffre non nul est fixe
                        if valeur != 0:
                            self.cases_fixes.add((x, y))
            
            # Actualisation des éléments de l'interface utilisateur
            if self.vue_principale:
                self.vue_principale.changer_message_statut("Partie en cours...", "#555555")
                if self.vue_principale.vue_grille:
                    self.vue_principale.vue_grille.rafraichir_affichage()

    def get_valeur_case(self, x, y):
        # Récupère la valeur numérique d'une case
        if self.grille:
            val = self.grille.get_valeur(x, y)
            return val if val is not None else 0
        return 0

    def set_valeur_case(self, x, y, v):
        # Bloque l'action si aucune grille n'est en mémoire
        if not self.grille:
            return
        # Empêche la modification si la case fait partie des indices fixes du départ
        if (x, y) in self.cases_fixes:
            return
        # Vérifie la contrainte du motif pour rejeter une valeur supérieure à sa taille N
        motif = self.grille.get_motif_de_case(x, y)
        if motif and v > motif.get_n():
            return
        
        # Enregistrement de la nouvelle valeur dans le modèle de données
        self.grille.set_valeur(x, y, v)
        
        # Déclenchement de la victoire si la grille est totalement remplie et valide
        if len(self.grille.cases_vides()) == 0 and self.grille.est_valide():
            if self.vue_principale:
                self.vue_principale.changer_message_statut("Victoire!", "green")

    def memes_motifs(self, x1, y1, x2, y2):
        # Vérifie si deux coordonnées distinctes partagent le même motif de la grille
        if not self.grille:
            return False
        m1 = self.grille.get_motif_de_case(x1, y1)
        m2 = self.grille.get_motif_de_case(x2, y2)
        return m1 == m2 and m1 is not None

    def case_est_fixe(self, x, y):
        # Renvoie vrai si la case est protégée contre l'écriture
        return (x, y) in self.cases_fixes

    def case_est_valide(self, x, y):
        # Par défaut, une case est valide s'il n'y a pas de modèle chargé
        if not self.grille:
            return True
        valeur = self.grille.get_valeur(x, y)
        # Une case vide est considérée valide
        if valeur == 0 or valeur is None:
            return True
        
        # Vérification des cases adjacentes directes et diagonales
        voisins = self.grille.get_voisins(x, y)
        for voisin in voisins:
            if voisin["valeur"] == valeur:
                return False 
        
        #  Vérification du motif
        motif = self.grille.get_motif_de_case(x, y)
        if motif:
            compte = 0
            for case in motif.get_cases():
                if case["valeur"] == valeur:
                    compte += 1
            if compte > 1:
                return False 
                
        return True

    def resoudre_partie(self):
        # Sécurité pour ne pas lancer plusieurs calculs ou agir sans données
        if not self.grille or self.en_cours_de_resolution:
            return
            
        self.en_cours_de_resolution = True
        # Désactivation de la fenêtre principale pendant la recherche pour bloquer les entrées clavier/souris
        if self.vue_principale:
            self.vue_principale.setEnabled(False)
            self.vue_principale.changer_message_statut("Résolution automatique en cours...", "orange")
        
        # Nettoyage préalable de toutes les cases remplies par le joueur (on conserve uniquement les fixes)
        for motif in self.grille.get_motifs():
            for case in motif.get_cases():
                x, y = case["x"], case["y"]
                if (x, y) not in self.cases_fixes:
                    self.grille.set_valeur(x, y, 0)
        
        # Collecte et tri des cases vides par taille de motif (optimisation heuristique)
        liste_cases_vides = self.grille.cases_vides()
        liste_cases_vides.sort(key=lambda c: self.grille.get_motif_de_case(c["x"], c["y"]).get_n())
        
        self._compteur_iterations = 0
        # Démarrage de l'algorithme de backtracking
        succes = self._backtracking_opt(liste_cases_vides, 0)
        
        # Exploitation du résultat renvoyé par le solveur
        if succes:
            if self.vue_principale:
                self.vue_principale.changer_message_statut("Grille résolue par le solveur.", "blue")
                if self.vue_principale.vue_grille:
                    self.vue_principale.vue_grille.rafraichir_affichage()
        else:
            if self.vue_principale:
                self.vue_principale.changer_message_statut("Aucune solution trouvée pour cette configuration.", "red")
                
        # Réactivation complète de l'IHM
        if self.vue_principale:
            self.vue_principale.setEnabled(True)
        self.en_cours_de_resolution = False

    def _backtracking_opt(self, cases_vides, index):
        # Condition d'arrêt réussie : toutes les cases vides ont reçu une valeur valide
        if index >= len(cases_vides):
            return True
        
        # Incrémentation du compteur
        self._compteur_iterations += 1
        if self._compteur_iterations % 50000 == 0:
            QCoreApplication.processEvents()
            
        # Sélection de la case courante à traiter
        case = cases_vides[index]
        x, y = case["x"], case["y"]
        motif = self.grille.get_motif_de_case(x, y)
        n = motif.get_n()
        
        # Boucle itérative testant les candidats possibles pour cette case
        for v in range(1, n + 1):
            self.grille.set_valeur(x, y, v)
            # Si le candidat respecte les règles, on explore récursivement la case suivante
            if self.case_est_valide(x, y):
                if self._backtracking_opt(cases_vides, index + 1):
                    return True 
                    
        # Retour en arrière: restauration de l'état vide si aucun choix n'a réussi
        self.grille.set_valeur(x, y, 0)
        return False
    
    def reinitialiser_grille(self):
        # Annulation si aucune grille n'est chargée
        if not self.grille:
            return
            
        # Parcours et réinitialisation à 0 uniquement pour les cases modifiables par l'utilisateur
        for motif in self.grille.get_motifs():
            for case in motif.get_cases():
                x, y = case["x"], case["y"]
                if (x, y) not in self.cases_fixes:
                    self.grille.set_valeur(x, y, 0)
        
        # Rafraîchissement visuel et mise à jour du texte de statut de la fenêtre principale
        if self.vue_principale:
            self.vue_principale.changer_message_statut("Grille réinitialisée.", "#555555")
            if self.vue_principale.vue_grille:
                self.vue_principale.vue_grille.rafraichir_affichage()