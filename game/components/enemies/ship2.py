from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2
import pygame
class Ship2(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 15
    SPEED_Y = 5
    Y_POS = -50
    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image,self.SPEED_X, self.SPEED_Y,self.Y_POS)
        