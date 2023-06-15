from game.components.enemies.boos_attack import Boos
from game.utils.constants import BOOS
import pygame
class Boos(Boos):
    WIDTH = 400
    HEIGHT = 312
    SPEED_X = 15
    SPEED_Y = 5
    Y_POS = -50
    def __init__(self):
        self.image = BOOS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image,self.SPEED_X, self.SPEED_Y,self.Y_POS)
        