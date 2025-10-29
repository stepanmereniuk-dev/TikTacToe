import pygame
from pygame import Surface


class Button:
    '''
    tutorial: https://pythonprogramming.altervista.org/button-widget-in-pygame-updated/
    TODO: Make call-back function on parameter
    '''
    def __init__(self,text,wight,height,position, passed_value,callback_func=None):
        self.pressed = False
        self.text = text 
        self.wight = wight
        self.height = height
        self.position = position
        self.passed_value = passed_value
        self.call_back_func = callback_func

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

    def void():
        pass

    def _draw(self,surface:Surface):
        bottom_offset = self.button_rect.move(3, 3) 
        pygame.draw.rect(surface, self.bottom_color, bottom_offset)
        pygame.draw.rect(surface, self.top_color,self.top_rect)
        surface.blit(self.text_surf, self.text_reg)
        

    def _check_hover(self,surface:Surface):
        pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(pos):
            bottom_offset = self.button_rect.move(3, 3)
            pygame.draw.rect(surface, self.bottom_color, bottom_offset)
            surface.blit(self.text_surf, self.text_reg)
        else:
            bottom_offset = self.button_rect.move(3, 3)
            pygame.draw.rect(surface, self.top_color, bottom_offset)
            surface.blit(self.text_surf, self.text_reg)
        pass

    def _check_click(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos()
                if self.top_rect.collidepoint(pos):
                    if self.call_back_func is not None:  
                        self.call_back_func(self.passed_value)
    
    def set_text(self,new_text):
        print("receive")
        self.text = new_text
        self.text_surf = self.font.render(self.text, True, (230, 230, 230))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        pass

    def _pressed(self):
        pass

    def update(self,surface,event):
        self._check_click(event)
        self._check_hover(surface)
        pass 



        