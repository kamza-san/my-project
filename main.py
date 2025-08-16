import pygame
import sys
from pygame.locals import *
from offline.game import game
from offline.title import title
from online.online import online
from offline.level_setting import level_set
from online.make import make
from offline.ranking import ranking
from online.host import server
from online.onlinegame import enter

pygame.init()
#Object 만들때 무조건 가로와 가로위치를 5의 배수로 만들어야함
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
        elif answer == "level_settting":
            level = level_set(clock,screen,FPS,MYFONT)
            answer = "title"
        elif answer == "make":
            answer = make(clock,screen,FPS,MYFONT)
        elif answer == "ranking":
            answer = ranking(clock,screen,FPS,MYFONT)
        elif answer == "enter":
            answer == enter(clock,screen,FPS,MAX_WIDTH,MAX_HEIGHT,MYFONT)