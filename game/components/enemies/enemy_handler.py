from game.components.enemies.ship import Ship
from game.components.enemies.ship2 import Ship2
from game.components.enemies.marcian1 import Marcian_sp
from game.components.enemies.meteor_image import Meteor
from game.components.enemies.boss import Boos
from game.utils.constants import ENEMY_TYPE_BOOS, ENEMY_TYPE_NORMAL
import random, pygame

class EnemyHandler:
    def __init__(self):
        self.boos_activate = False
        self.dificult_time = 500
        self.enemie_destroy = 0
        self.enemies = []
        # self.enemies.append(Ship())
        # self.enemies.append(Ship2())
        self.enemies.append(Marcian_sp())
        # self.enemies.append(Meteor())
        
    def update(self,user_input, bullet_handler, player, player_two):
        self.enemy_cont = 3
        self.alien = Marcian_sp()
        self.enemy2 = Ship2()
        self.enemy = Ship()
        self.meteor = Meteor()
        self.boos = Boos()       
        
        self.select_enemy =[self.alien, self.enemy, self.enemy2, self.meteor]
        for enemy in range(len(self.enemies)):
            self.delete = self.enemies[enemy].update(bullet_handler, player, player_two)
            if user_input[pygame.K_p]:
                self.delete = True
                    
            if self.delete:
                if self.enemies[enemy].enemy_type == ENEMY_TYPE_NORMAL:
                    self.enemie_destroy += 10
                elif self.enemies[enemy].enemy_type == ENEMY_TYPE_BOOS:
                    self.enemie_destroy += 1000
                    self.dificult_time += 1000
                    self.boos_activate = False
                del self.enemies[enemy]
                self.enemies.append(random.choice(self.select_enemy))
                pygame.time.delay(1)
        self.add_enemy()
    
    def add_enemy(self):
        if self.enemie_destroy >= self.dificult_time:
            self.enemy_cont += 1
            if not self.boos_activate:
                self.enemies.append(Boos())
                self.boos_activate = True
        if len(self.enemies) <self.enemy_cont:
            self.enemies.append(random.choice(self.select_enemy))
        
    def reset(self):
        self.enemies = []
        self.enemie_destroy = 0
        self.enemy_cont = 3
        self.boos_activate = False
            
                
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)