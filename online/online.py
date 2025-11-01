import pygame
import sys
from offline.button import Button
from offline.textbox import Textbox
from image import button,title_photo,quit_button1,button2,quit_button2

def online(clock,screen,FPS,MYFONT):
    host = Textbox(200,300,200,80,button,"host",MYFONT,0,0,0,screen)
    port = Textbox(200,420,200,80,button,"port",MYFONT,0,0,0,screen)
    gameenter = Button(200,540,200,80,button,"enter",MYFONT,0,0,0,screen)
    quit = Button(500,20,80,80,quit_button1,"",MYFONT,0,0,0,screen)
    matching = Button(200,660,200,80,button,"matching",MYFONT,0,0,0,screen)
    writing = Button(200,100,200,80,button,"writing...",MYFONT,0,0,0,screen)
    while True:    
        clock.tick(FPS)
        screen.blit(title_photo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameenter.click(pygame.mouse.get_pos()):
                    return [host.text,int(port.text)]
                elif quit.click(pygame.mouse.get_pos()):
                    return "title"
                elif host.click(pygame.mouse.get_pos()):
                    while True:
                        writing.draw()
                        host.draw()
                        port.draw()
                        gameenter.draw()
                        quit.draw()
                        pygame.display.update()
                        result = host.input()
                        if result == "end":
                            break
                        if result == "del":
                            host.text = host.text[:-1]
                        else:
                            host.text += result
                elif port.click(pygame.mouse.get_pos()):
                    while True:
                        writing.draw()
                        host.draw()
                        port.draw()
                        gameenter.draw()
                        quit.draw()
                        pygame.display.update()
                        result = port.input()
                        if result == "end":
                            break
                        if result == "del":
                            port.text = port.text[:-1]
                        else:
                            port.text += result
                elif matching.click(pygame.mouse.get_pos()):
                    return "matching"
        host.image = button
        port.image = button
        gameenter.image = button
        quit.image = quit_button1
        matching.image = button
        if host.click(pygame.mouse.get_pos()):
            host.image = button2
        elif port.click(pygame.mouse.get_pos()):
            port.image = button2
        elif gameenter.click(pygame.mouse.get_pos()):
            gameenter.image = button2
        elif quit.click(pygame.mouse.get_pos()):
            quit.image = quit_button2
        elif matching.click(pygame.mouse.get_pos()):
            matching.image = button2        
        host.draw()
        port.draw()
        gameenter.draw()
        quit.draw()
        matching.draw()
        pygame.display.update()