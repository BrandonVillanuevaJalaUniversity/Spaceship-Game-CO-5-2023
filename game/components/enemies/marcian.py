import pygame
from game.utils.constants import SCREEN_WIDTH, BULLET_ENEMY_TYPE,ENEMY_TYPE_NORMAL

class Marcian_sp(pygame.sprite.Sprite):
    SHOOTING_TIME = 30
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load("game\components\enemies\sprites\metal1.png")
        self.sheet.set_clip(pygame.Rect(335, 80, 48, 45))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.bottomright = (0, 100)
        self.frame = 0
        self.shooting_time = 0
        self.alives = False
        self.direction = "left"
        self.enemy_type = ENEMY_TYPE_NORMAL
        self.clock = pygame.time.Clock()
        self.right_states = {0: (6, 40, 75, 70), 1: (82, 40, 75, 70), 2: (152, 40, 75, 70), 3:(222, 40, 75, 70), 4:(292, 40, 75, 70), 5: (362, 40, 75, 70), 6:(432, 40, 75, 70), 7: (502, 40, 75, 70), 8: (6, 110, 75, 70), 9: (82, 110, 75, 70), 10:(152, 110, 75, 70), 11:(222, 110, 75, 70), 12:(292, 110, 75, 70), 13:(362, 110, 75, 70), 14:(432, 110, 75, 70), 15:(502, 110, 75, 70)}
        self.left_states = { 0:(6, 430, 75, 80), 1:(81, 430, 75, 80), 2:(160, 430, 85, 80), 3:(245, 430, 85, 80),4 :(340, 420, 85, 80), 5:(440, 420, 85, 80), 6:(6, 510, 105, 80), 7: (105, 510, 95, 80), 8: (200, 510, 95, 80), 9: (290, 510, 75, 80), 10: (360, 510, 75, 80), 11:(435, 510, 75, 80), 12:(510, 510, 75, 80), 13:(6, 600, 75, 90), 14:(81, 600, 75, 90), 15:(150, 600, 75, 90), 16:(215, 600, 75, 90), 17:(280, 600, 75, 90), 18:(345, 600, 70, 90)}
        self.lives= 1
        
        
    def update(self,bullet_handler, player, player_two):
        self.shooting_time +=1
        self.shoot(bullet_handler)
        if self.lives <= 0:
            self.direction = "dead"
            self.alives = True
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
        elif self.direction == "dead":
            self.clip(self.left_states)
            if self.frame >= (len(self.left_states) -3):
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