import pygame
import sys
from offline.button import Button
from image import button,title_photo,quit_button1

def online(clock,screen,FPS,MYFONT):
    gamemake = Button(200,300,200,80,button,"make",MYFONT,0,0,0,screen)
    gameenter = Button(200,420,200,80,button,"enter",MYFONT,0,0,0,screen)
    quit = Button(500,20,80,80,quit_button1,"",MYFONT,0,0,0,screen)
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gamemake.click(pygame.mouse.get_pos()):
                    return "make"
                elif gameenter.click(pygame.mouse.get_pos()):
                    return "enter"
                elif quit.click(pygame.mouse.get_pos()):
                    return "title"
        gamemake.draw()
        gameenter.draw()
        quit.draw()
        pygame.display.update()