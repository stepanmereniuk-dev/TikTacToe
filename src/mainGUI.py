import pygame
import sys

from script import Button, TextLabel

pygame.init()
screenProperty = (1200,680)
screen = pygame.display.set_mode(screenProperty)

all_button = []
all_labels = []
pre_build_complited = False

def pre_build():

    text_label = TextLabel("Unknown choice",250,50,(500,20))
    all_labels.append(text_label)
    
    button = Button("Player vs Player",240,40,(900,200),passed_value="Player vs Player",callback_func = text_label.set_text)
    button._draw(screen)
    all_button.append(button)
    button = Button("Player vs AI",240,40,(900,250),passed_value="Player vs AI",callback_func = text_label.set_text)
    button._draw(screen)
    all_button.append(button)

def desk_build():
    
    for i in range(3):
        for b in range(3):
            x = 100 +(100 * b + 100)
            y = 100 + (100 * i + 100)
            button = Button(" - ",100,100,(x,y),passed_value="X")
            button._draw(screen)
            all_button.append(button)
    pass

pre_build()
desk_build()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((230,230,230))

    for but in all_button:
        but.update(screen,event)
    for lb in all_labels:
        lb._draw(screen)
    
    pygame.display.flip()

