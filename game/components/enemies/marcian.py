import pygame
from game.utils.constants import SCREEN_WIDTH

class Marcian_sp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load("game\components\enemies\sprites\metal.png")
        self.sheet.set_clip(pygame.Rect(335, 80, 48, 45))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.bottomright = (0, 100)
        self.frame = 0
        self.direction = "left"
        self.clock = pygame.time.Clock()
        self.right_states = {0: (0, 30, 55, 40), 1: (55, 30, 48, 40), 2: (100, 30, 48, 40), 3:(148, 30, 48, 40), 4:(195, 30, 48, 40), 5: (240, 30, 48, 45), 6:(287, 30, 48, 45), 7: (335, 30, 48, 45), 8: (0, 80, 55, 45), 9: (55, 80, 48, 45), 10:(101, 80, 48, 45), 11:(149, 80, 48, 45), 12:(195, 80, 48, 45), 13:(240, 80, 48, 45), 14:(287, 80, 48, 45), 15:(335, 80, 48, 45)}
        self.left_states = {  0: (0, 270, 55, 60), 1: (54, 270, 55, 60), 2: (106, 270, 55, 60), 3: (163, 270, 55, 60), 4: (224, 270, 55, 60), 5:(294, 270, 60, 60), 6:(0, 335, 70, 60), 7:(70, 335, 70, 60), 8:(140, 335, 55, 60), 9:(188, 335, 55, 60), 10:(237, 335, 53, 60), 11:(286, 335, 53, 60), 12:(333, 335, 53, 60), 13:(0, 395, 55, 70), 14:(52, 395, 50, 70), 15:(98, 395, 50, 65), 16:(143, 395, 50, 65), 17:(187, 395, 45, 65), 18:(228, 395, 45, 65), 19:(268, 395, 45, 65), 20:(308, 395, 45, 65), 21:(345, 395, 45, 65)}
        
        
    def update(self):
        if self.direction == "left":
            self.clip(self.right_states)
            self.rect.x +=10
            if self.rect.right >= SCREEN_WIDTH:
                self.direction = "rigth"
        elif self.direction == "rigth":
            self.clip(self.right_states)
            self.rect.x -=10
            if self.rect.left <= 0:
                self.direction = "dead"
        elif self.direction == "dead":
            self.clip(self.left_states)
        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        pygame.time.delay(30)
        
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
        self.update()
        screen.blit(self.image, self.rect)
        