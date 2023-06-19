import pygame, random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Power:
    POWER_WIDTH= 40
    POWER_HEIGTH = 40
    POWER_SPEED = 10
    
    def __init__(self, image, type,rect):
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.POWER_HEIGTH,self.POWER_WIDTH))
        self.rect = rect
        self.rect.x = random.randint(120, SCREEN_WIDTH-120) 
        self.type = type
        self.rect.y = 0
        self.position = 'down_rigth'
        
    def update(self):
        if self.position == 'down_left':
            self.down_left()
        elif self.position == 'down_rigth':
            self.down_rigth()
        elif self.position == 'up_rigth':
            self.up_rigth()
        elif self.position == 'up_left':
            self.up_left()
        
    def down_left(self):
        if self.rect.x > 0 and self.rect.bottom < SCREEN_HEIGHT: 
            self.rect.x -=10
            self.rect.y += self.POWER_SPEED
        elif self.rect.x > 0 and self.rect.bottom >= SCREEN_HEIGHT: 
            self.position = 'up_left'
        elif self.rect.x <= 0 and self.rect.bottom >= SCREEN_HEIGHT: 
            self.position = 'up_rigth'            
        elif self.rect.x < 0 and self.rect.bottom < SCREEN_HEIGHT: 
            self.position = 'down_rigth'            
            
                    
    def down_rigth(self):
        if self.rect.x < SCREEN_WIDTH and self.rect.y < SCREEN_HEIGHT: 
            self.rect.x +=10
            self.rect.y += self.POWER_SPEED
            
        elif self.rect.x < SCREEN_WIDTH and self.rect.y >= SCREEN_HEIGHT: 
            self.position = 'up_rigth'
            
        elif self.rect.x >= SCREEN_WIDTH and self.rect.y < SCREEN_HEIGHT: 
            self.position = 'down_left'  
            
        elif self.rect.x >= SCREEN_WIDTH and self.rect.y >= SCREEN_HEIGHT: 
            self.position = 'up_left'  
            
            
    def up_left(self):
        if self.rect.x > 0 and self.rect.y > 0: 
            self.rect.x -=10
            self.rect.y -= self.POWER_SPEED
            
        elif self.rect.x <= 0 and self.rect.y > 0: 
            self.position = 'up_rigth'
            
        elif self.rect.x > 0 and self.rect.top <= 0: 
            self.position = 'down_left'
            
        elif self.rect.x <= 0 and self.rect.y <= 0: 
            self.position = 'down_rigth'                        
        
    def up_rigth(self):
        if self.rect.x < SCREEN_WIDTH and self.rect.y > 0: 
            self.rect.x +=10
            self.rect.y -= self.POWER_SPEED
            
        elif self.rect.x >= SCREEN_WIDTH and self.rect.y > 0: 
            self.position = 'up_left'
            
        elif self.rect.x >= SCREEN_WIDTH and self.rect.y <= 0: 
            self.position = 'down_left'
            
        elif self.rect.x < SCREEN_WIDTH and self.rect.y <= 0: 
            self.position = 'down_rigth'   
        
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)