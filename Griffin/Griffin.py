import pygame

import Counter
from Button import Button
import Controls
from Counter import COUNTER

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Griff')
    bg_color = (200, 200, 150)
    x = 100
    y = 100
    button = Button(screen, x, y)


    while True:
        Controls.events(button)
        screen.fill(bg_color)
        button.output()
        button.draw_counter()
        pygame.display.flip()


run()
