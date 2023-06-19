import pygame

from game.components import text_utils
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, PLAYER_ONE, PLAYER_TWO, WHITE, GAME_OVER, BLACK, PINK, PLAYER_TWO_CONTROLLERS, PLAYER_ONE_CONTROLLERS, SPACESHIP
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullet.bullet_handler import BulletHandler
from game.components.powers.power_handler import PowerHandler
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_over = GAME_OVER
        self.game_over = pygame.transform.scale(self.game_over ,(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.player_two_controllers = pygame.transform.scale(PLAYER_TWO_CONTROLLERS, (280, 148))
        self.player_one_controllers = pygame.transform.scale(PLAYER_ONE_CONTROLLERS, (280, 148))
        self.spaceship = pygame.transform.scale(SPACESHIP, (50, 60))
        self.text_size = 30
        self.dificult_time = 500
        self.running = True
        self.game_speed = 10
        self.hig_score= 0
        self.x_pos_bg = 0
        self.margin = True
        self.enemy_cont= 4
        self.back = True
        self.y_pos_bg = 0
        self.number_death = 0
        self.player_one = Spaceship(PLAYER_ONE)
        self.player_two = Spaceship(PLAYER_TWO)
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.power_handler = PowerHandler()
        

    def run(self):
        # Game loop: events - update - draw
        pygame.mixer.music.load("game/assets/soundtracks/neo-geo-intro.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.0)
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    self.playing = True
                    self.enemy_cont = 4
                    pygame.mixer.music.load("game/assets/soundtracks/into-the-cosmos.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(1.0)
                    self.back = True
                    self.reset(event)

    def update(self):
        if self.playing:
            self.score= self.enemy_handler.enemie_destroy
            self.enemy_destroyer = self.enemy_handler.enemy_destroyer
            if self.score > self.hig_score:
                self.hig_score = self.score
            self.user_input = pygame.key.get_pressed()
            self.player_one.update(self.user_input, self.bullet_handler)
            self.player_two.update(self.user_input, self.bullet_handler)
            self.enemy_handler.update(self.user_input,self.bullet_handler, self.player_one, self.player_two,self.power_handler,self.back,self.enemy_cont)
            self.bullet_handler.update(self.player_one,self.player_two, self.enemy_handler.enemies)
            self.power_handler.update(self.player_one,self.player_two)
            if not self.player_two.is_available and not self.player_one.is_available:
                self.playing = False
                self.number_death +=1
                pygame.mixer.music.load("game/assets/soundtracks/metal-slug-3-music-hq.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(1.0)
            if self.score >= self.enemy_handler.dificult_time:
                self.enemy_cont += 1

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            if self.player_one.is_available:
                self.player_one.draw(self.screen)
            if self.player_two.is_available:
                self.player_two.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.draw_score()
            self.power_handler.draw(self.screen)
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
        
    def draw_menu(self):
        if self.number_death == 0:
            if self.margin:
                self.text_size += 3
                if self.text_size >= 100:
                    self.margin = False
            elif self.margin == False:
                self.text_size -= 3
                if self.text_size <= 30:
                    self.margin = True
            title, title_rect = text_utils.get_message('THE NEO-SPACESHIP', self.text_size, WHITE, SCREEN_WIDTH/2, 100)
            text, text_rect = text_utils.get_message('press the number of players', 50, WHITE)
            self.screen.blit(text, text_rect)
            self.screen.blit(self.player_two_controllers,(50, 400))
            self.screen.blit(self.player_one_controllers,(770, 400))
            self.screen.blit(self.spaceship,(540, 400))
            self.screen.blit(title, title_rect)
                
        else:
            # text, text_rect = text_utils.get_message('prees any key to start', 30, WHITE)
            score, score_rect = text_utils.get_message('your score is:', 40, WHITE, 394, 440)
            score0, score_rect0 = text_utils.get_message(f' {self.score} ', 40, WHITE, 800, 440)
            hig_score, hig_score_rect = text_utils.get_message('your hig score is:', 40, WHITE, 430, 490)
            hig_score0, hig_score_rect0 = text_utils.get_message(f' {self.hig_score} ', 40, WHITE, 800, 490)
            enemy, enemy_rect = text_utils.get_message('your destroy score is:', 40, WHITE, 472, 540)
            enemy0, enemy_rect0 = text_utils.get_message(f' {self.enemy_destroyer} ', 40, WHITE, 800, 540)
            self.screen.blit(self.game_over ,(0,0))
            if self.back:
                self.enemy_handler.reset()
                self.enemy_cont = 1
                self.enemy_handler.add_enemie_background()  
                self.back = False
            self.enemy_handler.update(self.user_input,self.bullet_handler, self.player_one, self.player_two,self.power_handler,self.back,self.enemy_cont)
            self.enemy_handler.draw(self.screen)
            # self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(hig_score, hig_score_rect)
            self.screen.blit(hig_score0, hig_score_rect0)
            self.screen.blit(enemy, enemy_rect)
            self.screen.blit(enemy0, enemy_rect0)
            self.screen.blit(score0, score_rect0)
            


    def draw_score(self):
        score, score_rect = text_utils.get_message(f'score: {self.score}', 30, WHITE, 100, 40)
        arm, arm_rect = text_utils.get_message('Arm:', 30, WHITE, 60, 80)
        arm1, arm_rect1 = text_utils.get_message(f' {self.player_one.heavym} ', 30, WHITE, 150, 80)
        arm2, arm_rect2 = text_utils.get_message('Arm:', 30, WHITE, 60, 120)
        arm3, arm_rect3 = text_utils.get_message(f' {self.player_two.heavym} ', 30, WHITE, 150, 120)
        self.screen.blit(arm, arm_rect)
        self.screen.blit(arm1, arm_rect1)
        self.screen.blit(arm2, arm_rect2)
        self.screen.blit(arm3, arm_rect3)
        self.screen.blit(score, score_rect)
        
    def reset(self, event):
        if event.key == pygame.K_1:
            self.player_one.reset()
        if event.key == pygame.K_2:
            self.player_one.reset()
            self.player_two.reset()
            
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_handler.reset()
        