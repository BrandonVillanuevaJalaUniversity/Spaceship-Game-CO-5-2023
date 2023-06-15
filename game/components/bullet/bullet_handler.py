from game.components.bullet.bullet_enemy import BulletEnemy
from game.utils.constants import BULLET_ENEMY_TYPE

class BulletHandler:
    def __init__(self):
        self.bullet = []
        
    def update(self,player):
        for bullet in self.bullet:
            bullet.update(player)
            
    def draw(self, screen):
        for bullet in self.bullet:
            bullet.draw(screen)
    
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullet.append(BulletEnemy(center))