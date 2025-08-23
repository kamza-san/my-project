import pygame
import sys
from offline.button import Button
from offline.textbox import Textbox
from image import button,title_photo,button2,setting_button1,setting_button2,quit_button1,quit_button2
import threading

def title(clock,screen,FPS,MYFONT,level):
    right = Button(200,300,200,80,button,"d",MYFONT,0,0,0,screen)
    left = Button(200,420,200,80,button,"a",MYFONT,0,0,0,screen)
    jump = Button(200,540,200,80,button,"k",MYFONT,0,0,0,screen)
    down = Button(200,660,200,80,button,"s",MYFONT,0,0,0,screen)
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN: