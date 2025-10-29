import pygame
from pygame import Surface

class TextLabel:
    '''
    '''
    def __init__(self,text,wight,height,position):
        self.pressed = False
        self.text = text 
        self.wight = wight
        self.height = height
        self.position = position

        #top reg
        self.top_rect = pygame.Rect(position,(wight,height))
        self.top_color = "#2C6699" 
        #button reg
        self.button_rect = pygame.Rect(position,(wight,height))
        self.bottom_color = "#274661" 

        self.font = pygame.font.Font(None,42)
        self.text_surf = self.font.render(self.text,True,(230,230,230))
        self.text_reg = self.text_surf.get_rect(center=self.top_rect.center)
        #text 
        pass

    def _draw(self,surface:Surface):
        bottom_offset = self.button_rect.move(3, 3) 
        pygame.draw.rect(surface, self.bottom_color, bottom_offset)
        pygame.draw.rect(surface, self.top_color,self.top_rect)
        surface.blit(self.text_surf, self.text_reg)
        
#HOW TO MAKE IT MORE FLEXIBLE? 
    def set_text(self,new_text):
        print("receive")
        self.text = new_text
        self.text_surf = self.font.render(self.text, True, (230, 230, 230))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        pass





        