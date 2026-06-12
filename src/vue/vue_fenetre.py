from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
from vue.vue_grille import VueGrille

class FenetrePrincipale(QMainWindow): #la classe fenetre principale herite de la classe QMainWindow
    def __init__(self, controleur): #initialise la fenetre principale
        super().__init__()
        self.controleur = controleur
         
        self.setWindowTitle("Néonaure - Jeu de Grille") # titre de la fenetre

        self.setStyleSheet(         # rajoute de la patte graphique un peu neon
            "QMainWindow { background-color: #0d0b1e; }"
            "QWidget#central { background-color: #0d0b1e; }"
            "QMenuBar { background-color: #0a0818; color: #c084fc; font-size: 14px; font-weight: bold; padding: 2px; border-bottom: 1px solid #2d1b4e; }"
            "QMenuBar::item { padding: 4px 12px; }"
            "QMenuBar::item:selected { background-color: #2d1b4e; color: #c084fc; }"
            "QMenu { background-color: #1a1635; color: #e2e8f0; border: 1px solid #a855f7; }"
            "QMenu::item:selected { background-color: #2d1b4e; color: #c084fc; }"
        )
        
        # la barre des menus 
        barre_menu = self.menuBar()
        menu_fichier = barre_menu.addMenu("Menu du jeu")
        
        action_charger = menu_fichier.addAction("Charger une grille")
        action_charger.triggered.connect(self.controleur.charger_partie)

        action_sauvegarder = menu_fichier.addAction("Sauvegarder")
        action_sauvegarder.triggered.connect(self.controleur.sauvegarder_partie)
        
        action_resoudre = menu_fichier.addAction("Résoudre la grille")
        action_resoudre.triggered.connect(self.controleur.resoudre_partie)

        action_reinitialiser = menu_fichier.addAction("Réinitialiser la grille")
        action_reinitialiser.triggered.connect(self.controleur.reinitialiser_grille)
        
        zone_centrale = QWidget()
        # zone autour du jeu pour faire beaux et que le jeu ressorte
        zone_centrale.setObjectName("central")
        layout_principal = QVBoxLayout()
        layout_principal.setSpacing(15)  
        
        #Création un conteneur largeur fixe pareille à la grille (500px)
        widget_haut = QWidget()
        widget_haut.setFixedWidth(500) # Aligné sur les 8 * 60 + 20 pixels de VueGrille
        
        layout_haut = QHBoxLayout(widget_haut)
        layout_haut.setContentsMargins(0, 0, 0, 0) # Supprime les marges internes pour coller aux bords de la grille
        
        self.label_statut = QLabel("Veuillez charger une grille pour commencer")
        self.label_statut.setStyleSheet("font-size: 16px; font-weight: bold; color: #a855f7;") #couleur violet

        self.label_timer = QLabel("Temps : 00:00")
        self.label_timer.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label_timer.setStyleSheet("font-size: 16px; font-weight: bold; color: #22d3ee;") #couleur cyan
        
        # Assemblage de la ligne du haut
        layout_haut.addWidget(self.label_statut)
        layout_haut.addWidget(self.label_timer)
        
        self.vue_grille = VueGrille(self.controleur)

      
        cadre_grille = QFrame()
        cadre_grille.setStyleSheet(
            "QFrame { border: 2px solid #a855f7; border-radius: 6px;"
            " background-color: #0a0818; padding: 6px; }"
        )
        # Layout interne du cadre pour y placer la grille
        layout_cadre = QVBoxLayout(cadre_grille)
        layout_cadre.setContentsMargins(0, 0, 0, 0)
        layout_cadre.addWidget(self.vue_grille)
        
        # Label de crédits
        self.label_credits = QLabel("Projet Néonaure (R2-02, R2-07) - réalisé par PLAETEVOET Gaëlle, LANIEZ Gabriel, ROBA Ethan")
        self.label_credits.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Crédits : violet moyen, plus lisible sur fond sombre
        self.label_credits.setStyleSheet("font-size: 12px; color: #7c3aed; font-style: italic; margin-top: 5px;")
        
        # Ajout des widgets dans le layout principal en les centrant explicitement
        layout_principal.addWidget(widget_haut, alignment=Qt.AlignmentFlag.AlignCenter)
        # On ajoute le cadre terminal (qui contient la grille) au lieu de la grille directement
        layout_principal.addWidget(cadre_grille, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_credits, alignment=Qt.AlignmentFlag.AlignCenter)
        
        #Application du layout à la zone centrale
        zone_centrale.setLayout(layout_principal)
        self.setCentralWidget(zone_centrale)

    # Partie IA
    def changer_message_statut(self, texte, couleur="#c084fc"):
        # Couleur par défaut : violet néon ; #4ade80 pour victoire, #67e8f9 pour info
        if hasattr(self, 'label_statut') and self.label_statut:
            self.label_statut.setText(texte)
            # Applique la nouvelle taille de texte statut (16px) avec la couleur reçue
            self.label_statut.setStyleSheet("font-size: 16px; font-weight: bold; color: " + couleur + ";")

    def changer_affichage_timer(self, texte):
        if hasattr(self, 'label_timer') and self.label_timer:
            self.label_timer.setText(texte)