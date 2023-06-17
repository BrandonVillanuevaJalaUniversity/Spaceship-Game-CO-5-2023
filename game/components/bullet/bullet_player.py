from game.components.bullet.bullet import Bullet
from game.utils.constants import BULLET
import pygame

class BulletPlayer(Bullet):
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    
    def __init__(self,center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        super().__init__(self.image, center)
        
    def update(self,player, player_two, enemies):
        self.rect.y -= self.SPEED
        for enemy in range(len(enemies)):
            if self.rect.colliderect(enemies[enemy].rect):
                enemies[enemy].lives -= 1
                self.rect.bottom = -50
                self.is_available = False
                return True