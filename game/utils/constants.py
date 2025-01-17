import pygame
import os

# Global Constants
TITLE = "The neo-spaceship"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
PLAYER_ONE = True
PLAYER_TWO = False
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEAVY_TYPE = 'heavy'

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "background/game_over.png"))
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/metal1.png"))
SPACESHIP2 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/metal2.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_SHIELD2 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield2.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_3.png"))
DRAGON_DOWN = pygame.image.load(os.path.join(IMG_DIR, "Bullet/dragon down.png"))
BOOS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/BOOS.png"))
HEAVY = pygame.image.load(os.path.join(IMG_DIR, 'Other/HEAVY.png'))
HEAVY1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/HEAVY2.png'))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
METEOR_WHITE = pygame.image.load(os.path.join(IMG_DIR, "Enemy/meteoroBlanco.png"))
METEOR_RED = pygame.image.load(os.path.join(IMG_DIR, "Enemy/meteoroRojo.png"))
PLAYER_ONE_HEART1 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/heart1,1.png"))
PLAYER_ONE_HEART2 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/heart1,2.png"))
PLAYER_ONE_HEART3 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/heart1,3.png"))
HEAVI_IMG = pygame.image.load(os.path.join(IMG_DIR, 'Other/HEAVY_IMG.png'))

WHITE = (255,255,255)
RED = (255, 0, 0)
PINK = (255, 120, 122)
BLACK = (0, 0, 0)
GREEN = (1, 198 ,82)

PLAYER_TWO_CONTROLLERS = pygame.image.load(os.path.join(IMG_DIR, "background/player2.png"))
PLAYER_ONE_CONTROLLERS = pygame.image.load(os.path.join(IMG_DIR, "background/player1.png"))
FONT_STYLE = 'freesansbold.ttf'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'

ENEMY_TYPE_NORMAL = 'normal'
ENEMY_TYPE_BOOS = 'boos'
