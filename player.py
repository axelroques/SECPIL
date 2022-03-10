
from __init__ import JOYSTICK_WINDOW, NUMBER_WINDOW, WIDTH, HEIGHT, PALONNIER_WINDOW
import pygame


class Palonnier(pygame.sprite.Sprite):

    def __init__(self):
        super(Palonnier, self).__init__()

        self.surf = pygame.image.load("Assets/bottom.png")
        self.rect = self.surf.get_rect()

        # Initialize position at the center of the screen
        self.x = (WIDTH-self.surf.get_width())/2
        self.y = PALONNIER_WINDOW[1] + \
            PALONNIER_WINDOW[3]/2-self.surf.get_height()/2
        self.rect.x = self.x
        self.rect.y = self.y

    def get_centered_pos(self):
        return self.x+self.surf.get_width()/2, self.y+self.surf.get_height()/2

    def update(self, controller, axis=None, value=None, inputs=None):

        if controller == 'keyboard':
            x, _ = self.get_centered_pos()

            if inputs[pygame.K_LEFT]:
                min_width = PALONNIER_WINDOW[0]+self.surf.get_width()/2
                if x <= min_width:
                    self.x = min_width-self.surf.get_width()/2
                else:
                    self.x -= 7.5

            if inputs[pygame.K_RIGHT]:
                max_width = NUMBER_WINDOW[0] - \
                    PALONNIER_WINDOW[0]-self.surf.get_width()/2
                if x >= max_width:
                    self.x = max_width-self.surf.get_width()/2
                else:
                    self.x += 7.5

        elif controller == 'palonnier':
            x, _ = self.get_centered_pos()

            if axis == 2:
                min_width = PALONNIER_WINDOW[0] + self.surf.get_width()/2
                max_width = NUMBER_WINDOW[0] - \
                    PALONNIER_WINDOW[0]-self.surf.get_width()/2
                if (x <= min_width) and (value < 0):
                    self.x = min_width-self.surf.get_width()/2
                elif x >= max_width and (value > 0):
                    self.x = max_width-self.surf.get_width()/2
                else:
                    self.x += value*7.5

            else:
                pass

        else:
            print('Unknown controller name')
            pass

        # Update rect position
        self.rect.x = self.x


class Joystick(pygame.sprite.Sprite):

    def __init__(self):
        super(Joystick, self).__init__()

        self.surf = pygame.image.load("Assets/circle.png")
        self.rect = self.surf.get_rect()

        # Initialize position at the center of the screen
        self.x = (WIDTH-self.surf.get_width())/2
        self.y = JOYSTICK_WINDOW[1] + \
            JOYSTICK_WINDOW[3]/2-self.surf.get_height()/2
        self.rect.x = self.x
        self.rect.y = self.y

    def get_centered_pos(self):
        return self.x+self.surf.get_width()/2, self.y+self.surf.get_height()/2

    def update(self, controller, axis=None, value=None, inputs=None):

        if controller == 'keyboard':
            x, y = self.get_centered_pos()

            if inputs[pygame.K_LEFT]:
                min_width = JOYSTICK_WINDOW[0]+self.surf.get_width()/2
                if x <= min_width:
                    self.x = JOYSTICK_WINDOW[0]
                else:
                    self.x -= 7.5

            if inputs[pygame.K_RIGHT]:
                max_width = WIDTH-JOYSTICK_WINDOW[0]-self.surf.get_width()/2
                if x >= max_width:
                    self.x = max_width-self.surf.get_width()/2
                else:
                    self.x += 7.5

            if inputs[pygame.K_DOWN]:
                min_height = JOYSTICK_WINDOW[0]+self.surf.get_height()/2
                if y <= min_height:
                    self.y = min_height-self.surf.get_height()/2
                else:
                    self.y -= 7.5

            if inputs[pygame.K_UP]:
                max_height = HEIGHT-JOYSTICK_WINDOW[0]-self.surf.get_height()/2
                if y >= max_height:
                    self.y = HEIGHT-self.surf.get_height()
                else:
                    self.y += 7.5

        elif controller == 'joystick':
            x, y = self.get_centered_pos()

            min_width = JOYSTICK_WINDOW[0]+self.surf.get_width()/2
            max_width = WIDTH-JOYSTICK_WINDOW[0]-self.surf.get_width()/2
            min_height = JOYSTICK_WINDOW[1]+self.surf.get_height()/2
            max_height = HEIGHT-JOYSTICK_WINDOW[0]-self.surf.get_height()/2

            if axis == 0:
                if (x <= min_width) and (value < 0):
                    self.x = min_width-self.surf.get_width()/2
                elif (x >= max_width) and (value > 0):
                    self.x = max_width-self.surf.get_width()/2
                else:
                    self.x += value*7.5

            elif axis == 1:
                value = -value
                if (y <= min_height) and (value < 0):
                    self.y = min_height-self.surf.get_height()/2
                elif (y >= max_height) and (value > 0):
                    self.y = max_height-self.surf.get_height()/2
                else:
                    self.y += value*7.5

            else:
                pass

        else:
            print('Unknown controller name')
            pass

        # Update rect position
        self.rect.x = self.x
        self.rect.y = self.y
