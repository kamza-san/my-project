import pygame
import sys
from offline.button import Button
from image import button,title_photo

def level_set(clock,screen,FPS,MYFONT):
    hard = Button(200,300,200,80,button,"hard",MYFONT,0,0,0,screen)
    normal = Button(200,420,200,80,button,"normal",MYFONT,0,0,0,screen)
    easy = Button(200,540,200,80,button,"easy",MYFONT,0,0,0,screen)
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hard.click(pygame.mouse.get_pos()):
                    return "hard"
                elif normal.click(pygame.mouse.get_pos()):
                    return "normal"
                elif easy.click(pygame.mouse.get_pos()):
                    return "easy"
        hard.draw()
        normal.draw()
        easy.draw()
        pygame.display.update()