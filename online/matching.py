import pygame
import sys
from offline.button import Button
from offline.textbox import Textbox
from image import button,title_photo,quit_button1,button2,quit_button2
import socket
import socket
from pygame.locals import *
from offline.map import generate_map,touch,touch_side,touch_near

def matching(clock,screen,FPS,MYFONT):
    host = "54.180.80.228"
    port = 20000
    
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
    except TimeoutError:
        print("서버에 연결할 수 없습니다. (TimeoutError 발생)")
        pygame.quit()
        sys.exit()
    except Exception as e:
        print(f"서버 연결 중 오류가 발생했습니다: {e}")
        pygame.quit()
        sys.exit()

    quit = Textbox(200,300,200,80,button,"quit",MYFONT,0,0,0,screen)
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit.click(pygame.mouse.get_pos()):
                    return "online"
        