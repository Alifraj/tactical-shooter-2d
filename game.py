# game.py
import pygame
import sys
from settings import *
from player import Player
from enemy import Enemy
class Game:
    def __init__(self):
        pygame.init()
        # Fenêtre de jeu de taille fixe définie au lancement[cite: 1]
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Titre de la fenêtre correspondant au nom du jeu[cite: 1]
        pygame.display.set_caption("Tactical Shooter 2D")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = STATE_MENU
        
        # Initialisation de la police
        self.font = pygame.font.SysFont(None, 48)

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        # Instanciation de l'agent
        self.player = Player()
        self.all_sprites.add(self.player)
        
        self.score = 0
        # Meilleur score (high score) sauvegardé dans un fichier texte[cite: 1]
        self.high_score = self.load_high_score()
        self.spawn_enemies(8) # Fait apparaître 8 ennemis
        
        # --- AUDIO (Effets sonores)[cite: 1] ---
        pygame.mixer.init()
        
        # 1. Chargement du son de tir
        try:
            self.shoot_sound = pygame.mixer.Sound("assets/sounds/messi-to-weghorst.mp3")
            self.shoot_sound.set_volume(0.8) 
        except:
            print("Attention: Fichier son 'assets/sounds/shoot.wav' introuvable.")
            self.shoot_sound = None
            
        # 2. Chargement de la musique de fond
        try:
            pygame.mixer.music.load("assets/sounds/cr_suuu.mp3")
            pygame.mixer.music.set_volume(0.15)
            # Le paramètre -1 permet de jouer la musique en boucle infinie
            pygame.mixer.music.play(-1)
        except:
            print("Attention: Fichier musique 'assets/sounds/background.ogg' introuvable.")
    def spawn_enemies(self, count):
        for _ in range(count):
            enemy = Enemy(self.score)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def events(self):
        # Gestion des événements clavier et souris[cite: 1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if self.state == STATE_MENU:
                    # Écran d'accueil: touche pour démarrer[cite: 1]
                    if event.key == pygame.K_SPACE:
                        self.state = STATE_PLAYING
                
                elif self.state == STATE_PLAYING:
                    # Écran de pause (touche P ou Échap pour suspendre le jeu)[cite: 1]
                    if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                        self.state = STATE_PAUSE
                        # On met la musique en pause
                        pygame.mixer.music.pause() 
                        
                    # Tirer un projectile avec la barre Espace lorsque le jeu est en cours
                    elif event.key == pygame.K_SPACE:
                        self.player.shoot(self.all_sprites, self.bullets)
                        # Jouer le son lors du tir[cite: 1]
                        if self.shoot_sound:
                            self.shoot_sound.play()
                            
                elif self.state == STATE_PAUSE:
                    # On sort de la pause avec les mêmes touches
                    if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                        self.state = STATE_PLAYING
                        # On relance la musique là où elle s'était arrêtée
                        pygame.mixer.music.unpause() 
                
                elif self.state == STATE_GAME_OVER:
                    # Écran Game Over: option pour rejouer ou quitter[cite: 1]
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.state = STATE_PLAYING
                    elif event.key == pygame.K_q:
                        self.running = False
    def update(self):
        # Mise à jour de la logique selon l'état
        if self.state == STATE_PLAYING:
            self.all_sprites.update()
            
            # --- NOUVEAU CODE : COLLISIONS ---
            
            # 1. Collision Balles / Ennemis (Détruit les deux)
            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
            for hit in hits:
                self.score += 1
                # À chaque fois qu'un ennemi est détruit, on en recrée un nouveau
                # pour que le jeu continue à l'infini
                self.spawn_enemies(1)
                
            # 2. Collision Ennemis / Joueur (Game Over)
            # Le paramètre False signifie qu'on ne détruit pas le joueur immédiatement
            if pygame.sprite.spritecollide(self.player, self.enemies, False):
                # --- NOUVEAU CODE : Vérification du meilleur score ---
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.save_high_score()
                # -----------------------------------------------------
                self.state = STATE_GAME_OVER
        

    def draw(self):
        self.screen.fill(BLACK)

        if self.state == STATE_MENU:
            self.draw_text("Tactical Shooter - Appuyez sur ESPACE", self.font, WHITE, 80, 250)
        
        elif self.state == STATE_PLAYING:
            # --- NOUVEAU CODE ---
            # Dessine tous les sprites (joueur + balles) à l'écran
            self.all_sprites.draw(self.screen)
            self.draw_text(f"Score: {self.score}", self.font, WHITE, 10, 10)
            # On peut aussi afficher le "Niveau" (qui augmente tous les 10 points)
            niveau = (self.score // 10) + 1
            self.draw_text(f"Niveau: {niveau}", self.font, GREEN, 10, 50)
        elif self.state == STATE_PAUSE:
            # On dessine les sprites en fond pour voir le jeu figé
            self.all_sprites.draw(self.screen)
            self.draw_text("PAUSE", self.font, BLUE, 330, 250)
            self.draw_text("Appuyez sur P ou Echap pour reprendre", self.font, WHITE, 100, 320)
            # --------------------
            
        elif self.state == STATE_GAME_OVER:
           
           self.draw_text("GAME OVER", self.font, RED, 280, 200)
           self.draw_text(f"Score Final : {self.score}", self.font, WHITE, 280, 260)
            # --- NOUVEAU CODE : Affichage du meilleur score ---
           self.draw_text(f"Meilleur Score : {self.high_score}", self.font, GREEN, 260, 310)
           self.draw_text("Appuyez sur 'R' pour Rejouer ou 'Q' pour Quitter", self.font, WHITE, 50, 380)
        pygame.display.flip()

    def draw_text(self, text, font, color, x, y):
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def reset_game(self):
        # On vide les groupes d'ennemis et de balles
        for enemy in self.enemies:
            enemy.kill()
        for bullet in self.bullets:
            bullet.kill()
            
        # On replace le joueur au centre
        self.player.rect.centerx = WIDTH // 2
        self.player.rect.bottom = HEIGHT - 20
        self.score = 0
        
        # On fait réapparaître une nouvelle vague
        self.spawn_enemies(8)
    # --- NOUVELLES MÉTHODES ---
    def load_high_score(self):
        try:
            # Essaie de lire le fichier texte
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except:
            # Si le fichier n'existe pas encore, le high score est 0
            return 0

    def save_high_score(self):
        # Écrit le nouveau record dans le fichier texte[cite: 1]
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def run(self):
        # Boucle de jeu (game loop)[cite: 1]
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()