from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from vue.vue_grille import VueGrille

class FenetrePrincipale(QMainWindow):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        
        # Configuration du titre de la fenêtre
        self.setWindowTitle("Néonaure - Jeu de Grille")
        
        #Barre d'outils
        barre_menu = self.menuBar()
        
        menu_fichier = barre_menu.addMenu("Fichier")
        
        action_charger = menu_fichier.addAction("Charger une grille")
        action_charger.triggered.connect(self.controleur.charger_partie)

        action_sauvegarder = menu_fichier.addAction("Sauvegarder")
        action_sauvegarder.triggered.connect(self.controleur.sauvegarder_partie)
        
        menu_jeu = barre_menu.addMenu("Grille")
        
        action_resoudre = menu_jeu.addAction("Résoudre la grille")
        action_resoudre.triggered.connect(self.controleur.resoudre_partie)

        action_reinitialiser = menu_jeu.addAction("Réinitialiser la grille")
        action_reinitialiser.triggered.connect(self.controleur.reinitialiser_grille)
        
        zone_centrale = QWidget()
        layout_principal = QVBoxLayout()
        layout_principal.setSpacing(15)  
        
        self.label_statut = QLabel("Veuillez charger une grille pour commencer")
        self.label_statut.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_statut.setStyleSheet("font-size: 13px; font-weight: bold; color: #555555;")
        
        self.vue_grille = VueGrille(self.controleur)
        
        # Label de crédits
        self.label_credits = QLabel("Projet Néonaure (R2-02, R2-07) - réalisé par PLAETEVOET Gaëlle, LANIEZ Gabriel, ROBA Ethan")
        self.label_credits.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_credits.setStyleSheet("font-size: 10px; color: #888888; font-style: italic; margin-top: 5px;")
        
        # Assemblage des composants du haut vers le bas
        layout_principal.addWidget(self.label_statut)
        layout_principal.addWidget(self.vue_grille)
        layout_principal.addWidget(self.label_credits)
        
        # Application du layout à la zone centrale
        zone_centrale.setLayout(layout_principal)
        self.setCentralWidget(zone_centrale)

    # Partie IA
    def changer_message_statut(self, texte, couleur="#555555"):
        if hasattr(self, 'label_statut') and self.label_statut:
            self.label_statut.setText(texte)
            self.label_statut.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {couleur};")