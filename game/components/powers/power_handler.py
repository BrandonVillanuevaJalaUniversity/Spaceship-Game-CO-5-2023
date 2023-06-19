from game.components.powers.shield import Shiel
from game.components.powers.heavy import Heavy
from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP_SHIELD2, HEAVY, HEAVY_TYPE, SHIELD_TYPE, HEAVY1
import pygame,random
class PowerHandler:
    def __init__(self) -> None:
        self.powers = []
        self.HEAVY = pygame.mixer.Sound("game/assets/soundtracks/H.mp3") 
        self.ok = pygame.mixer.Sound("game/assets/soundtracks/audio_metal_slug_ok.mp3") 
        self.wen_appears = random.randint(3000,7000)
        # power = Shiel()
        # self.powers.append(power)
        
    def update(self,player,player_two):
        self.current_time = pygame.time.get_ticks()
        if len(self.powers) > 0:
            for power in range(len(self.powers)):
                self.powers[power].update()
                if self.powers[power].rect.colliderect(player.rect):
                    if self.powers[power].type == HEAVY_TYPE:
                        player.image = HEAVY
                        player.image = pygame.transform.scale(player.image,(50,60))
                        player.shiel_activate = True
                        self.powers[power].rect.top = 1000
                        self.powers[power].position = "STOP"
                        self.powers[power].is_available = False          
                        player.heavym += 70   
                        self.HEAVY.play()
                    elif self.powers[power].type == SHIELD_TYPE:
                        self.powers[power].rect.top = 1000
                        self.powers[power].position = "STOP"
                        if player.lives <3 and player.lives > 0:
                            player.lives += 1
                        self.powers[power].is_available = False                        
                        self.ok.play()
                    
                elif self.powers[power].rect.colliderect(player_two.rect):
                    if self.powers[power].type == HEAVY_TYPE:
                        player_two.image = HEAVY1
                        player_two.image = pygame.transform.scale(player_two.image,(40,60))
                        player_two.shiel_activate = True
                        self.powers[power].rect.top = 1000
                        self.powers[power].position = "STOP"
                        self.HEAVY.play()
                        self.powers[power].is_available = False                        
                        player_two.heavym += 70       
                        
                    elif self.powers[power].type == SHIELD_TYPE:
                        self.powers[power].rect.top = 1000
                        self.powers[power].position = "STOP"
                        if player_two.lives <3 and player_two.lives > 0:
                            player_two.lives += 1
                        self.powers[power].is_available = False                        
                        self.ok.play()
                    
    def draw(self, screen):
        for power in range(len(self.powers)):
            if self.powers[power].is_available:
                self.powers[power].draw(screen)
            
    def add_power(self,rect,type):
        if type == HEAVY_TYPE:
            self.powers.append(Heavy(rect))
            
        if type == SHIELD_TYPE:
            self.powers.append(Shiel(rect))
            
    def reset(self):
        self.powers = []
        