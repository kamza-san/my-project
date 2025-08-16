import pygame
import sys
class Textbox:
    def __init__(self,x,y,si_x,si_y,image,text,font,red,green,blue,screen):
        self.x = x
        self.y = y
        self.si_x = si_x
        self.si_y = si_y
        self.screen = screen
        self.image = image
        self.text = text
        self.font = font
        self.red = red
        self.green = green
        self.blue = blue
    def draw(self):
        self.screen.blit(self.image,(self.x-20,self.y-25))
        return self.screen.blit(self.font.render(str(self.text), True, (self.red,self.green,self.blue)),(self.x,self.y))
    def click(self,mouse):
        if self.x <= mouse[0] and mouse[0] <= (self.x + self.si_x) :
            if self.y <= mouse[1] and mouse[1] <= (self.y + self.si_y) :
                return True
        return False
    def input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        return "del"
                    elif event.key == pygame.K_RETURN:
                        return "end"
                    else:
                        return event.unicode