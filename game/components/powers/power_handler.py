from game.components.powers.shield import Shiel
from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP_SHIELD2
import pygame,random
class PowerHandler:
    def __init__(self) -> None:
        self.powers = []
        self.HEAVY = pygame.mixer.Sound("game/assets/soundtracks/H.mp3") 
        self.wen_appears = random.randint(3000,7000)
        # power = Shiel()
        # self.powers.append(power)
        
    def update(self,player,player_two):
        self.current_time = pygame.time.get_ticks()
        if len(self.powers) > 0:
            for power in range(len(self.powers)):
                self.powers[power].update()
                if self.powers[power].rect.colliderect(player.rect):
                    player.image = SPACESHIP_SHIELD
                    player.image = pygame.transform.scale(player.image,(40,60))
                    player.shiel_activate = True
                    self.powers[power].rect.y = 600
                    self.HEAVY.play()
                    
                elif self.powers[power].rect.colliderect(player_two.rect):
                    player_two.image = SPACESHIP_SHIELD2
                    player_two.image = pygame.transform.scale(player_two.image,(40,60))
                    player_two.shiel_activate = True
                    self.powers[power].rect.y = 600
                    self.HEAVY.play()
                    
    def draw(self, screen):
        for power in self.powers:
            power.draw(screen)
            
    def add_power(self,rect):
        self.powers.append(Shiel(rect))
            
    def reset(self):
        self.powers = []
        