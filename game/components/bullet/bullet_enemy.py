from game.components.bullet.bullet import Bullet
from game.utils.constants import BULLET_ENEMY, SCREEN_WIDTH
import pygame

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    
    def __init__(self,center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        super().__init__(self.image, center)
        
    def update(self, player, player_two, enemy):
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect):
            if not player.shiel_activate:
                self.rect.top = 600
                pygame.time.delay(10)
                player.lives -= 1
                self.is_available = False
            else:
                player.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
                
            
        elif self.rect.colliderect(player_two.rect):
            if not player_two.shiel_activate:
                self.rect.top = 600
                player_two.lives -= 1
                self.is_available = False
            else:
                player_two.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
        if self.rect.top >= SCREEN_WIDTH:
            self.is_available = False