from game.components.enemies.ship import Ship
from game.components.enemies.ship2 import Ship2
from game.components.enemies.marcian import Marcian_sp
class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(Ship2())
        self.enemies.append(Marcian_sp())
        
    def update(self):
        for enemy in self.enemies:
            enemy.update()
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)