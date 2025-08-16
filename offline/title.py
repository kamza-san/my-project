import pygame
import sys
from offline.button import Button
from offline.textbox import Textbox
from image import button,title_photo
import threading

def title(clock,screen,FPS,MYFONT,level):
    gamestart = Button(200,300,200,80,button,"game start",MYFONT,0,0,0,screen)
    gameonline = Button(200,420,200,80,button,"game online",MYFONT,0,0,0,screen)
    setting = Button(200,540,200,80,button,"setting",MYFONT,0,0,0,screen)
    gamequit = Button(200,660,200,80,button,"game quit",MYFONT,0,0,0,screen)
    level_setting = Button(410,300,200,80,button,level,MYFONT,0,0,0,screen)
    rank = Button(410,420,200,80,button,"rank",MYFONT,0,0,0,screen)
    text = Textbox(410,540,200,80,button,"",MYFONT,0,0,0,screen)
    def drawing():
        text.draw()
        gamestart.draw()
        gameonline.draw()
        setting.draw()
        gamequit.draw()
        level_setting.draw()
        rank.draw()
        pygame.display.update()
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gamestart.click(pygame.mouse.get_pos()):
                    return "game"
                elif gameonline.click(pygame.mouse.get_pos()):
                    return "online"
                elif setting.click(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                elif gamequit.click(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                elif level_setting.click(pygame.mouse.get_pos()):
                    return "level_settting"
                elif rank.click(pygame.mouse.get_pos()):
                    return "ranking"
                elif text.click(pygame.mouse.get_pos()):
                    while True:
                        result = text.input()
                        if result == "end":
                            break
                        if result == "del":
                            text.text = text.text[:-1]
                        else:
                            text.text += result
                        drawing()
        drawing()
        #thread1 = threading.Thread(target=drawing())