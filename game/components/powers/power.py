import pygame, random
from game.utils.constants import SCREEN_WIDTH

class Power:
    POWER_WIDTH= 30
    POWER_HEIGTH = 30
    POWER_SPEED = 10
    
    def __init__(self, image, type,rect):
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.POWER_HEIGTH,self.POWER_WIDTH))
        self.rect = rect
        self.rect.x = random.randint(120, SCREEN_WIDTH-120) 
        self.type = type
        self.rect.y = 0
        
    def update(self):
        self.rect.y += self.POWER_SPEED
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)

        