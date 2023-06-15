from game.components.enemies.ship import Ship
from game.components.enemies.ship2 import Ship2
from game.components.enemies.marcian1 import Marcian_sp
from game.components.enemies.meteor_image import Meteor
from game.components.enemies.ovni_white1 import Boos_
from game.components.enemies.boss import Boos
import random, pygame

class EnemyHandler:
    DIFICULT_TIME = 1000
    def __init__(self):
        self.dificult_time = 0
        self.enemies = []
        # self.enemies.append(Ship())
        # self.enemies.append(Ship2())
        self.enemies.append(Marcian_sp())
        # self.enemies.append(Meteor())
        
    def update(self,user_input, bullet_handler, player, player_two):
        self.dificult_time += 1
        self.enemy_cont = 4
        self.alien = Marcian_sp()
        self.enemy2 = Ship2()
        self.enemy = Ship()
        self.meteor = Meteor()
        self.white_ovni = Boos_()
        self.boos = Boos()       
        
        self.select_enemy =[self.alien, self.enemy, self.enemy2, self.meteor, self.white_ovni, self.boos]
        for enemy in range(len(self.enemies)):
            self.delete = self.enemies[enemy].update(bullet_handler, player, player_two)
            if user_input[pygame.K_p]:
                self.delete = True
                    
            if self.delete:
                del self.enemies[enemy]
                self.enemies.append(random.choice(self.select_enemy))
                pygame.time.delay(1)
        self.add_enemy()
    
    def add_enemy(self):
        if self.dificult_time >= self.DIFICULT_TIME:
            self.enemy_cont += 1
        if len(self.enemies) <self.enemy_cont:
            self.enemies.append(random.choice(self.select_enemy))
        self.dificult_time = 0
            
            
                
                
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)