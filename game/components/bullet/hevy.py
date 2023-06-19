from game.utils.constants import BULLET, SCREEN_WIDTH, DRAGON_DOWN
import pygame

class HeavyLeft:
    WIDTH = 9
    HEIGTH = 32
    SPEED = 40
    def __init__(self,player, top):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        self.rect = self.image.get_rect()
        self.rect.left = player
        self.rect.bottom = top
        
    def update(self,player, player_two,enemies):
        self.rect.y -= self.SPEED
        for enemy in range(len(enemies)):
            if self.rect.colliderect(enemies[enemy].rect):
                enemies[enemy].lives -= 1
                self.rect.bottom = -50
                self.is_available = False
        if self.rect.top >= SCREEN_WIDTH:
            self.is_available = False
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
#---------------------------------------------------------------------------------
class HeavyRigth:
    WIDTH = 9
    HEIGTH = 32
    SPEED = 40
    def __init__(self,right, top):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.is_available = True
        self.rect = self.image.get_rect()
        self.rect.right = right
        self.rect.bottom = top
        
    def update(self,player, player_two,enemies):
        self.rect.y -= self.SPEED
        for enemy in range(len(enemies)):
            if self.rect.colliderect(enemies[enemy].rect):
                enemies[enemy].lives -= 1
                self.rect.bottom = -50
                self.is_available = False
        if self.rect.top >= SCREEN_WIDTH:
            self.is_available = False
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
#---------------------------------------------------------------------------------