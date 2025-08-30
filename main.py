import pygame
import sys
from pygame.locals import *
from offline.game import game
from offline.title import title
from online.online import online
from offline.level_setting import level_set
from online.enter import enter
from offline.ranking import ranking
from offline.set import setting

pygame.init()
pygame.mixer.init()
#Object 만들때 무조건 가로와 가로위치를 5의 배수로 만들어야함
bgm = pygame.mixer.Sound("./eximage/bgm2.mp3")
bgm.set_volume(0.5)
bgm.play(-1)
FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 800
MYFONT = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
answer = "title"
if __name__ == "__main__":
    level = "normal"
    while True:
        if answer == "title":
            answer = title(clock,screen,FPS,MYFONT,level)
        elif answer == "game":
            answer = game(clock,screen,FPS,MAX_WIDTH,MAX_HEIGHT,MYFONT,level)
        elif answer == "online":
            answer = online(clock,screen,FPS,MYFONT)
        elif answer == "level_setting":
            level = level_set(clock,screen,FPS,MYFONT,level)
            answer = "title"
        elif answer == "enter":
            answer = enter(clock,screen,FPS,MAX_WIDTH,MAX_HEIGHT,MYFONT)
        elif answer == "ranking":
            answer = ranking(clock,screen,FPS,MYFONT)
        elif answer == "setting":
            answer = setting(clock,screen,FPS,MYFONT)