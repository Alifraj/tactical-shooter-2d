# enemy.py
import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, score=0):
        super().__init__()
        image_originale = pygame.image.load("assets/images/ronaldo.jpg").convert_alpha()
        self.image = pygame.transform.scale(image_originale, (50, 50))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        
        # --- NOUVEAU CODE : DIFFICULTÉ ---
        # La vitesse augmente de 1 tous les 10 points marqués
        bonus_speed = score // 10 
        self.speed_y = random.randrange(2 + bonus_speed, 6 + bonus_speed)

    def update(self):
        self.rect.y += self.speed_y
        
        # Si l'ennemi sort de l'écran en bas, il réapparaît en haut
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(2, 6)