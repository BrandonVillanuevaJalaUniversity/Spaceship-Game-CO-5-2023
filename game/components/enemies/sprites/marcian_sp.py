import pygame

class Marcian_sp(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sheet = pygame.image.load("sprites\metal.png")
        self.sheet.set_clip(pygame.Rect(335, 80, 48, 45))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.bottomleft = position
        self.frame = 0
        self.right_states = {0: (0, 30, 55, 40), 1: (55, 30, 48, 40), 2: (100, 30, 48, 40), 3:(148, 30, 48, 40), 4:(195, 30, 48, 40), 5: (240, 30, 48, 45), 6:(287, 30, 48, 45), 7: (335, 30, 48, 45), 8: (0, 80, 55, 45), 9: (55, 80, 48, 45), 10:(101, 80, 48, 45), 11:(149, 80, 48, 45), 12:(195, 80, 48, 45), 13:(240, 80, 48, 45), 14:(287, 80, 48, 45), 15:(335, 80, 48, 45)}
        
    def update(self):
        self.clip(self.right_states)
        
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