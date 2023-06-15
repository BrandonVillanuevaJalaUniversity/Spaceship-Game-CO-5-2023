from game.components.bullet.bullet_enemy import BulletEnemy
from game.components.bullet.bullet_player import BulletPlayer
from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE

class BulletHandler:
    def __init__(self):
        self.bullets = []
        
    def update(self,player, player_two,enemy):
        for bullet in range(len(self.bullets)):
            self.valid = self.bullets[bullet].update(player, player_two,enemy)
            
    def draw(self, screen):
        for bullet in range(len(self.bullets)):
            self.bullets[bullet].draw(screen)
    
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        if type == BULLET_PLAYER_TYPE:
            self.bullets.append(BulletPlayer(center))