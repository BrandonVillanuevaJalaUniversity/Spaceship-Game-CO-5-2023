from game.utils.constants import BULLET, SCREEN_WIDTH
import pygame

class BulletLeft:
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    def __init__(self,left):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        self.rect = self.image.get_rect()
        self.rect.left = left
        
    def update(self,player, player_two,enemy):
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
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
#---------------------------------------------------------------------------------
class BulletRigth:
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    def __init__(self,right):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        self.rect = self.image.get_rect()
        self.rect.right = right
        
    def update(self,player, player_two,enemy):
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
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
#---------------------------------------------------------------------------------
class BulletCenter:
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20
    def __init__(self,center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def update(self,player, player_two,enemy):
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
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)