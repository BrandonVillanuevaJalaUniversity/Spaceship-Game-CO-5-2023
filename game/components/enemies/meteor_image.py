from game.components.enemies.enemy import Enemy
from game.utils.constants import METEOR_WHITE, METEOR_RED,ENEMY_TYPE_NORMAL
import pygame,random
class Meteor(Enemy):
    WIDTH = 60
    HEIGHT = 60
    SPEED_X = 5
    SPEED_Y = 20
    Y_POS = -30
    def __init__(self):
        self.enemy_type = ENEMY_TYPE_NORMAL
        self.image_white = METEOR_WHITE
        self.image_red = METEOR_RED
        self.image_grup= [self.image_red, self.image_white]
        self.image = random.choice(self.image_grup)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image,self.SPEED_X, self.SPEED_Y,self.Y_POS,self.enemy_type)
        