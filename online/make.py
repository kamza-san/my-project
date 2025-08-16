import pygame
import sys
from offline.button import Button
from image import button,title_photo,scoreimage
from online.host import server

def make(clock,screen,FPS,MYFONT):
    enter_port = Button(200,300,200,80,button,"enter port",MYFONT,0,0,0,screen)
    show_port = Button(200,420,200,80,scoreimage,0,MYFONT,0,0,0,screen)
    make_port = Button(200,540,200,80,button,"make",MYFONT,0,0,0,screen)
    quit = Button(200,660,200,80,button,"quit",MYFONT,0,0,0,screen)
    port = 0
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if enter_port.click(pygame.mouse.get_pos()):
                    port = input()
                    show_port.text = port
                    server(port)
                elif make_port.click(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                elif quit.click(pygame.mouse.get_pos()):
                    return "online"
        enter_port.draw()
        show_port.draw()
        make_port.draw()
        quit.draw()
        pygame.display.update()