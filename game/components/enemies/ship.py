from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_TYPE_NORMAL
import pygame
class Ship(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 5
    SPEED_Y = 5
    Y_POS = -50
    LIVE = 1
    def __init__(self):
        self.enemy_type = ENEMY_TYPE_NORMAL
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image,self.SPEED_X, self.SPEED_Y,self.Y_POS,self.enemy_type,self.LIVE)