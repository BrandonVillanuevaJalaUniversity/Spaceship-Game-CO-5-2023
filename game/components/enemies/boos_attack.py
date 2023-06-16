import pygame 
import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE, ENEMY_TYPE_BOOS

class Boos:
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    SHOOTING_TIME = 30
    
    def __init__(self,image,speed_x,speed_y,Y_POS):
        self.SPEED_X = speed_x
        self.SPEED_Y = speed_y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = Y_POS
        self.MOV_X = random.choice(self.MOV_X)
        self.direction = "left"
        self.shooting_time = 0
        self.alives = False
        self.lives= 10
        self.enemy_type = ENEMY_TYPE_BOOS
        
    def update(self, bullet_handler,player,player_two):
        if self.lives <= 0:
            return True
        self.shooting_time +=1
        if self.rect.top >= SCREEN_HEIGHT:
            self.alives = True
            return self.alives 
        self.move()
        self.shoot(bullet_handler)
        
        if self.rect.colliderect(player.rect):
            player.is_available = False
            
        if self.rect.colliderect(player_two.rect):
            player_two.is_available = False
            
        return self.alives
            
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        
    def move(self):
        if self.direction == "left":
            self.rect.x +=10
            if self.rect.right >= SCREEN_WIDTH:
                self.direction = "rigth"
            if self.alives:
                self.direction = "dead"
        elif self.direction == "rigth":
            self.rect.x -=10
            if self.rect.left <= 0:
                self.direction = "left"
            if self.alives:
                self.direction = "dead"
                
    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE ,self.rect.center)