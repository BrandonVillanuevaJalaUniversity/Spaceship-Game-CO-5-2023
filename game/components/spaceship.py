import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP2

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    def __init__(self,player_number):
        self.player= player_number
        if player_number:
            self.image = SPACESHIP
        else:
            self.image = SPACESHIP2
            
        self.image = pygame.transform.scale(self.image,(40,60))            
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
    def update(self, user_input):
        if self.player:
            if user_input[pygame.K_LEFT]:
                self.move_left()
            elif user_input[pygame.K_RIGHT]:
                self.move_right()
            elif user_input[pygame.K_UP]:
                self.move_up()
            elif user_input[pygame.K_DOWN]:
                self.move_down()
        else:
            if user_input[pygame.K_a]:
                self.move_left()
            elif user_input[pygame.K_d]:
                self.move_right()
            elif user_input[pygame.K_w]:
                self.move_up()
            elif user_input[pygame.K_s]:
                self.move_down()
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        
    def move_left(self):
        if self.rect.left >0:
            self.rect.x -= 15
        else:
            self.rect.right = SCREEN_WIDTH
    
    def move_right(self):
        if self.rect.right <SCREEN_WIDTH:
            self.rect.x += 15
        else:
            self.rect.left = 0
            
    def move_up(self):
        if self.rect.top >(SCREEN_HEIGHT/2):
            self.rect.y -= 15
            
    def move_down(self):
        if self.rect.bottom <(SCREEN_HEIGHT):
            self.rect.y += 15