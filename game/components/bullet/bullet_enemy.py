from game.components.bullet.bullet import Bullet
from game.utils.constants import BULLET_ENEMY
import pygame

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    
    def __init__(self,center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image, center)
        
    def update(self, player, player_two, enemy):
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect):
            player.is_available = False
            
        elif self.rect.colliderect(player_two.rect):
            player_two.is_available = False