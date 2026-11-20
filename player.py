# player.py
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
      
        image_originale = pygame.image.load("assets/images/messi.jpg").convert_alpha()
        self.image = pygame.transform.scale(image_originale, (50, 50))
        
        self.rect = self.image.get_rect()
        
        self.rect = self.image.get_rect()
        # Positionnement initial de l'agent en bas au centre
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        # Gestion des événements clavier pour les déplacements (Q/D ou Flèches)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.speed_x = -7
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed_x = 7
        
        self.rect.x += self.speed_x
        
        # Empêcher l'agent de sortir de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self, all_sprites, bullets):
        # Création d'un projectile à la position actuelle du joueur
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Le projectile est un petit rectangle blanc
        self.image = pygame.Surface((5, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -10 # Vitesse du projectile vers le haut

    def update(self):
        self.rect.y += self.speed_y
        # Détruire le projectile s'il sort de l'écran pour libérer la mémoire
        if self.rect.bottom < 0:
            self.kill()