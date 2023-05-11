import pygame
from Counter import COUNTER


class Button():

    def __init__(self, screen, x, y):
        # Инициализация кнопки

        self.screen = screen
        self.image1 = pygame.image.load('image/pixil-frame-0 (1).png')
        self.image2 = pygame.image.load('image/pixil-frame444.png')
        self.current_image = self.image1
        self.rect = self.image1.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.counter = COUNTER(screen, x, y)

    def output(self):
        # Отрисовка кнопки
        self.screen.blit(self.current_image, self.rect)

    def is_hovered(self, mouse_pos):
        # Проверка, находится ли указатель мыши над кнопкой
        return self.rect.collidepoint(mouse_pos)

    def toggle_skin(self):
        if self.current_image == self.image1:
            self.current_image = self.image2
        else:
            self.current_image = self.image1

    def update(self, mouse_down):
        # Обновляем скин кнопки в зависимости от состояния кнопки мыши
        if mouse_down:
            self.current_image = self.image2
        else:
            self.current_image = self.image1

    def on_click(self):
        # Действия при клике на кнопку
        self.counter.increment()

    def draw_counter(self):
        # Отображение счетчика
        self.counter.draw(self.screen)