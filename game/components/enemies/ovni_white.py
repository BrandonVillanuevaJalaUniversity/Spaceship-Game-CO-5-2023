import pygame
from game.utils.constants import SCREEN_WIDTH, BULLET_ENEMY_TYPE

class Boos(pygame.sprite.Sprite):
    SHOOTING_TIME = 30
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load("game\components\enemies\sprites\Boos.png")
        self.sheet.set_clip(pygame.Rect(335, 80, 48, 45))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.bottomright = (0, 100)
        self.frame = 0
        self.shooting_time = 0
        self.alives = False
        self.direction = "left"
        self.lives= 1
        self.clock = pygame.time.Clock()
        self.right_states = { 0: (0, 0, 160, 100), 1:(160, 0, 160, 100), 2:(320, 0, 160, 100), 3:(480, 0, 160, 100), 4:(640, 0, 160, 100), 5:(800, 0, 160, 100), 6: (0, 100, 160, 100), 7:(160, 100, 160, 100), 8:(320, 100, 160, 100), 9:(480, 100, 160, 100), 10:(640, 100, 160, 100), 11:(800, 100, 160, 100)}
        
    def update(self,bullet_handler, player, player_two):
        if self.lives <= 0:
            return True
        self.shooting_time +=1
        self.shoot(bullet_handler)
        if self.direction == "left":
            self.clip(self.right_states)
            self.rect.x +=10
            if self.rect.right >= SCREEN_WIDTH:
                self.direction = "rigth"
            if self.alives:
                self.direction = "dead"
        elif self.direction == "rigth":
            self.clip(self.right_states)
            self.rect.x -=10
            if self.rect.left <= 0:
                self.direction = "left"
            if self.alives:
                self.direction = "dead"
        elif self.direction == "dead":
                return self.alives
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.shooting_time +=1
        self.shoot(bullet_handler)
        
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
        
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        
    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE ,self.rect.center)