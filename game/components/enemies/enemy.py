import pygame 
import random
from game.utils.constants import SCREEN_WIDTH
class Enemy:
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    Y_POS = 20
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100
    def __init__(self,image,speed_x,speed_y):
        self.SPEED_X = speed_x
        self.SPEED_Y = speed_y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.MOV_X = random.choice(self.MOV_X)
        self.index = 0
        
    def update(self):
        self.rect.y += self.SPEED_Y
        if self.MOV_X == self.LEFT:
            self.rect.x -= self.SPEED_X
            if self.index >self.INTERVAL or self.rect.x <= 0:
                self.MOV_X = self.RIGHT
                self.index = 0
                
        else:
            self.rect.x += self.SPEED_X
            if self.index >self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.MOV_X = self.LEFT
                self.index = 0
        self.index += 1
        
            
    def draw(self,screen):
        screen.blit(self.image, self.rect)