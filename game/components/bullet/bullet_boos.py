from game.components.bullet.boos_controller import BulletCenter, BulletLeft, BulletRigth
from game.utils.constants import BULLET_ENEMY, SCREEN_WIDTH
import pygame

class BoosRigth(BulletRigth):
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    
    def __init__(self,rigth):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        super().__init__(self.image, rigth)
        
    def update(self, player, player_two, enemy):
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect):
            if not player.shiel_activate:
                self.rect.top = 600
                player.is_available = False
                self.is_available = False
            else:
                player.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
                
            
        elif self.rect.colliderect(player_two.rect):
            if not player_two.shiel_activate:
                self.rect.top = 600
                player_two.is_available = False
                self.is_available = False
            else:
                player_two.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
        if self.rect.top >= SCREEN_WIDTH:
            self.is_available = False
            
#-------------------------------------------------------------------------------------------------------------------

class BoosLeft(BulletLeft):
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    
    def __init__(self,left):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        super().__init__(self.image, left)
        
    def update(self, player, player_two, enemy):
        self.rect.y += self.SPEED
        if self.rect.colliderect(player.rect):
            if not player.shiel_activate:
                self.rect.top = 600
                player.is_available = False
                self.is_available = False
            else:
                player.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
                
            
        elif self.rect.colliderect(player_two.rect):
            if not player_two.shiel_activate:
                self.rect.top = 600
                player_two.is_available = False
                self.is_available = False
            else:
                player_two.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
        if self.rect.top >= SCREEN_WIDTH:
            self.is_available = False
            
#-------------------------------------------------------------------------------------------------------------------

class BoosCenter(BulletCenter):
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
                player.is_available = False
                self.is_available = False
            else:
                player.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
                
            
        elif self.rect.colliderect(player_two.rect):
            if not player_two.shiel_activate:
                self.rect.top = 600
                player_two.is_available = False
                self.is_available = False
            else:
                player_two.shiel_activate = False
                self.rect.top = 600
                self.is_available = False
        if self.rect.top >= SCREEN_WIDTH:
            self.is_available = False