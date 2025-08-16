import pygame
from pathlib import Path

BASE_DIR = Path(__file__).parent
IMG_PATH1 = BASE_DIR / "image" / "background.png"
IMG_PATH2 = BASE_DIR / "image" / "title.png"
IMG_PATH3 = BASE_DIR / "image" / "wait_ground.png"
IMG_PATH4 = BASE_DIR / "image" / "button.png"
IMG_PATH5 = BASE_DIR / "image" / "player_right.png"
IMG_PATH6 = BASE_DIR / "image" / "player_left.png"
IMG_PATH7 = BASE_DIR / "image" / "score.png"
background = pygame.image.load(str(IMG_PATH1))
background = pygame.transform.scale(background,(600,1600))
title_photo = pygame.image.load(str(IMG_PATH2))
title_photo = pygame.transform.scale(title_photo,(600,800))
wait_ground = pygame.image.load(str(IMG_PATH3))
wait_ground = pygame.transform.scale(wait_ground,(600,800))
button = pygame.image.load(str(IMG_PATH4))
button = pygame.transform.scale(button,(200,80))
player_right = pygame.image.load(str(IMG_PATH5))
player_right = pygame.transform.scale(player_right,(60,60))
player_left = pygame.image.load(str(IMG_PATH6))
player_left = pygame.transform.scale(player_left,(60,60))
scoreimage = pygame.image.load(str(IMG_PATH7))
scoreimage = pygame.transform.scale(scoreimage,(200,80))