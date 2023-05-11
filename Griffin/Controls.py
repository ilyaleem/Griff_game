import pygame, sys


def events(button):
    # Обработка события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if button.rect.collidepoint(event.pos):
                    button.on_click()
                    mouse_down = True
                    button.update(mouse_down)

        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == pygame.BUTTON_LEFT:
                mouse_down = False
                button.update(mouse_down)