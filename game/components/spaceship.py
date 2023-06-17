import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP2, BULLET_PLAYER_TYPE

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SHOOTING_TIME = 2
    def __init__(self,player_number):
        self.player= player_number
        self.player_number = player_number
        self.shooting_time = 0
        if player_number:
            self.image = SPACESHIP
        else:
            self.image = SPACESHIP2
            
        self.image = pygame.transform.scale(self.image,(40,60))            
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_available = False
        self.shiel_activate= False
        
    def update(self, user_input, bullet_handler):
        if self.is_available:
            if not self.shiel_activate:
                if self.player_number:
                    self.image = SPACESHIP  
                else:
                    self.image = SPACESHIP2
            self.image = pygame.transform.scale(self.image,(40,60)) 
            self.shooting_time += 1
            if self.player:
                if user_input[pygame.K_LEFT]:
                    self.move_left()
                elif user_input[pygame.K_RIGHT]:
                    self.move_right()
                elif user_input[pygame.K_UP]:
                    self.move_up()
                elif user_input[pygame.K_DOWN]:
                    self.move_down()
                elif user_input[pygame.K_SPACE]:
                    self.shoot(bullet_handler)
            else:
                if user_input[pygame.K_a]:
                    self.move_left()
                elif user_input[pygame.K_d]:
                    self.move_right()
                elif user_input[pygame.K_w]:
                    self.move_up()
                elif user_input[pygame.K_s]:
                    self.move_down()
                elif user_input[pygame.K_f]:
                    self.shoot(bullet_handler)
        else:
            self.rect.x = -50
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
            
    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_PLAYER_TYPE ,self.rect.center)
            
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_available = True
        self.shiel_activate = False