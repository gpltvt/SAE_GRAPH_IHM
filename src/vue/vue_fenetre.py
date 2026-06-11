from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from vue.vue_grille import VueGrille

class FenetrePrincipale(QMainWindow):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        
        # Configuration du titre de la fenêtre
        self.setWindowTitle("Néonaure - Jeu de Grille")
        
        # Barre d'outils
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
        
        #Création un conteneur d'une largeur fixe identique à la grille (500px)
        widget_haut = QWidget()
        widget_haut.setFixedWidth(500) # Aligné sur les 8 * 60 + 20 pixels de VueGrille
        
        layout_haut = QHBoxLayout(widget_haut)
        layout_haut.setContentsMargins(0, 0, 0, 0) # Supprime les marges internes pour coller aux bords de la grille
        
        self.label_statut = QLabel("Veuillez charger une grille pour commencer")
        self.label_statut.setStyleSheet("font-size: 13px; font-weight: bold; color: #555555;")
        
        self.label_timer = QLabel("Temps : 00:00")
        self.label_timer.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label_timer.setStyleSheet("font-size: 13px; font-weight: bold; color: #007BFF;")
        
        # Assemblage de la ligne du haut
        layout_haut.addWidget(self.label_statut)
        layout_haut.addWidget(self.label_timer)
        
        self.vue_grille = VueGrille(self.controleur)
        
        # Label de crédits
        self.label_credits = QLabel("Projet Néonaure (R2-02, R2-07) - réalisé par PLAETEVOET Gaëlle, LANIEZ Gabriel, ROBA Ethan")
        self.label_credits.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_credits.setStyleSheet("font-size: 10px; color: #888888; font-style: italic; margin-top: 5px;")
        
        #Ajout des widgets dans le layout principal en les centrant explicitement
        layout_principal.addWidget(widget_haut, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.vue_grille, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_credits, alignment=Qt.AlignmentFlag.AlignCenter)
        
        #Application du layout à la zone centrale
        zone_centrale.setLayout(layout_principal)
        self.setCentralWidget(zone_centrale)

    # Partie IA
    def changer_message_statut(self, texte, couleur="#555555"):
        if hasattr(self, 'label_statut') and self.label_statut:
            self.label_statut.setText(texte)
            self.label_statut.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {couleur};")

    def changer_affichage_timer(self, texte):
        if hasattr(self, 'label_timer') and self.label_timer:
            self.label_timer.setText(texte)