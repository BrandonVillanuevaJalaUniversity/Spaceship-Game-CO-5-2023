from game.components.bullet.bullet_enemy import BulletEnemy
from game.components.bullet.bullet_player import BulletPlayer
from game.components.bullet.boos_controller import BulletCenter, BulletLeft, BulletRigth
from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE, ENEMY_TYPE_BOOS

class BulletHandler:
    def __init__(self):
        self.bullets = []
        
    def update(self, player, player_two,enemy):
        for bullet in range(len(self.bullets)):
            self.bullets[bullet].update(player, player_two,enemy)
            
    def draw(self, screen):
        for bullet in range(len(self.bullets)):
            if self.bullets[bullet].is_available:
                self.bullets[bullet].draw(screen)
    
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_PLAYER_TYPE:
            self.bullets.append(BulletPlayer(center))
            
    def add_boos_bullet(self, type, left, center, rigth):
        if type == ENEMY_TYPE_BOOS:
            self.bullets.append(BulletLeft(left))
            self.bullets.append(BulletCenter(center))
            self.bullets.append(BulletRigth(rigth))
    def reset(self):
        self.bullets = []