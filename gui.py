
from __init__ import BACKGROUND_COLOR
import pygame


class Background:

    def __init__(self, x, y, w, h):

        self.surf = pygame.Surface((w, h))
        self.surf.fill((33, 33, 33))
        self.rect = self.surf.get_rect()

        # Moves the button's rect at x and y
        self.rect.x = x
        self.rect.y = y


class Button:

    def __init__(self, x, y):
        self.surf = pygame.Surface((300, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y

        # Moves the button's rect at x and y
        self.rect.x = x
        self.rect.y = y


class Text:

    def __init__(self, text, button):

        self.surf = pygame.font.SysFont(
            'Lato', 25).render(text, True, BACKGROUND_COLOR)
        self.rect = self.surf.get_rect(center=button.rect.center)
