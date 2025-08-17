import pygame
import sys
from offline.button import Button
from image import button,title_photo,quit_button1,button2,quit_button2
from offline.textbox import Textbox
import json


def ranking(clock,screen,FPS,MYFONT):
    MYFONT1 = pygame.font.SysFont(None, 30)
    name = Textbox(200,300,200,80,button,"",MYFONT,0,0,0,screen)
    hard = Button(200,420,200,80,button,"hard:0",MYFONT1,0,0,0,screen)
    normal = Button(200,540,200,80,button,"normal:0",MYFONT1,0,0,0,screen)
    easy = Button(200,660,200,80,button,"easy:0",MYFONT1,0,0,0,screen)
    quit = Button(500,20,80,80,quit_button1,"",MYFONT,0,0,0,screen)
    writing = Button(200,100,200,80,button,"writing...",MYFONT,0,0,0,screen)
    def drawing():
        name.draw()
        hard.draw()
        normal.draw()
        easy.draw()
        quit.draw()
        pygame.display.update()
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if name.click(pygame.mouse.get_pos()):
                    while True:
                        writing.draw()
                        drawing()
                        result = name.input()
                        if result == "end":
                            break
                        if result == "del":
                            name.text = name.text[:-1]
                        else:
                            name.text += result
                    user_name = name.text
                    with open("./data.json","r",encoding="utf-8")as f:
                        dict = json.load(f)
                    find = True
                    for i in dict:
                        if user_name == i:
                            name.text = user_name
                            hard.text = "hard:"+str(dict[i]["hard"])
                            normal.text = "normal:"+str(dict[i]["normal"])
                            easy.text = "easy:"+str(dict[i]["easy"])
                            find = False
                            break
                    if find:
                        hard.text = "hard:None"
                        normal.text = "normal:None"
                        easy.text = "easy:None"
                elif quit.click(pygame.mouse.get_pos()):
                    return "title"
        name.image = button
        quit.image = quit_button1
        if name.click(pygame.mouse.get_pos()):
            name.image = button2
        elif quit.click(pygame.mouse.get_pos()):
            quit.image = quit_button2
        drawing()