from game.components.enemies.ship import Ship
from game.components.enemies.ship2 import Ship2
from game.components.enemies.marcian1 import Marcian_sp
from game.components.enemies.meteor_image import Meteor

import random, pygame

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        # self.enemies.append(Ship())
        # self.enemies.append(Ship2())
        self.enemies.append(Marcian_sp())
        # self.enemies.append(Meteor())
        
    def update(self,user_input, bullet_handler):
        self.a = Marcian_sp()
        self.b = Ship2()
        self.c = Ship()
        self.d = Meteor()
        self.select_enemy =[self.a,self.b,self.c,self.d]
        for enemy in range(len(self.enemies)):
            self.delete = self.enemies[enemy].update(bullet_handler)
            if user_input[pygame.K_p]:
                self.delete = True
                    
            if self.delete:
                del self.enemies[enemy]
                print (self.a)
                self.enemies.append(random.choice(self.select_enemy))
                pygame.time.delay(1)
        self.add_enemy()
    
    def add_enemy(self):
        if len(self.enemies) <4:
            self.enemies.append(random.choice(self.select_enemy))
            
            
                
                
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)