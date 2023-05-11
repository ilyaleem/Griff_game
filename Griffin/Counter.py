import pygame
import sys


class COUNTER():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.value = 0
        self.font = pygame.font.SysFont('imoact', 50)
        self.text_color = (0, 0, 0)
        self.rect = pygame.Rect(x, y, 600, 50)

    def increment(self):
        self.value += 1

    def draw(self, screen):
        value_text = self.font.render(str(self.value), True, self.text_color)
        value_rect = value_text.get_rect()
        value_rect.center = self.rect.center
        screen.blit(value_text, value_rect)
