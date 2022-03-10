
from __init__ import WIDTH, HEIGHT, PALONNIER_WINDOW, JOYSTICK_WINDOW, NUMBER_WINDOW
import numpy as np
import pygame


class GoalPalonnier(pygame.sprite.Sprite):

    def __init__(self):
        super(GoalPalonnier, self).__init__()

        self.surf = pygame.image.load("Assets/square.png").convert()
        self.rect = self.surf.get_rect()

        # Movement logic
        self.directions = ['left', 'right']
        self.init_direction = np.random.choice(self.directions)
        self.last_direction = self.init_direction

        # Initial position
        self.x = (WIDTH-self.surf.get_width())/2
        self.y = PALONNIER_WINDOW[1] + \
            PALONNIER_WINDOW[3]/2-self.surf.get_height()/2
        self.rect.x = self.x
        self.rect.y = self.y

    def get_centered_pos(self):
        return self.x+self.surf.get_width()/2, self.y+self.surf.get_height()/2

    def update(self):

        # Movement direction
        r = np.random.uniform()
        if r > 0.1:
            direction = self.last_direction
        else:
            direction = np.random.choice(
                [dir for dir in self.directions if dir != self.last_direction])
        self.last_direction = direction

        # Increment computation
        x, _ = self.get_centered_pos()
        if direction == 'left':
            min_width = PALONNIER_WINDOW[0]+self.surf.get_width()/2
            if x <= min_width:
                self.x = min_width-self.surf.get_width()/2
            else:
                self.x -= 5
        else:
            max_width = NUMBER_WINDOW[0] - \
                PALONNIER_WINDOW[0]-self.surf.get_width()/2
            if x >= max_width:
                self.x = max_width-self.surf.get_width()/2
            else:
                self.x += 5

        # Update rect position
        self.rect.x = self.x


class GoalJoystick(pygame.sprite.Sprite):

    def __init__(self):
        super(GoalJoystick, self).__init__()

        self.surf = pygame.image.load("Assets/cross.png")
        self.rect = self.surf.get_rect()

        self.directions = ['left', 'right', 'down', 'up']
        self.x = (WIDTH-self.surf.get_width())/2
        self.y = JOYSTICK_WINDOW[1] + \
            JOYSTICK_WINDOW[3]/2-self.surf.get_height()/2
        self.rect.x = self.x
        self.rect.y = self.y

        # Movement parameters
        self.n = 30*5
        self.increment = 0
        # Circle coordinates
        self.circle_center = (
            WIDTH/2, JOYSTICK_WINDOW[1]+(JOYSTICK_WINDOW[3]/2-60)/2+60)
        self.r = (JOYSTICK_WINDOW[3]/2-60)/2
        self.x_circle = list(self.circle_center[0] +
                             np.array([self.r*np.cos(2*np.pi*x/self.n)
                                       for x in range(self.n+1)]))
        self.y_circle = list(self.circle_center[1] +
                             np.array([self.r*np.sin(2*np.pi*y/self.n)
                                       for y in range(self.n+1)]))
        self.x_circle = self.x_circle[int(
            self.n//4):] + self.x_circle[:int(self.n//4)]
        self.y_circle = self.y_circle[int(
            self.n//4):] + self.y_circle[:int(self.n//4)]

        # Ellipse coordinates
        self.ellipse_center = (
            WIDTH/2, JOYSTICK_WINDOW[1]+JOYSTICK_WINDOW[3]/2+self.r)
        self.r_a = self.r
        self.r_b = 2*self.r_a
        self.x_ellipse = list(self.ellipse_center[0] +
                              np.array([self.r_b*np.cos(2*np.pi*x/self.n)
                                        for x in range(self.n+1)]))
        self.y_ellipse = list(self.ellipse_center[1] +
                              np.array([self.r_a*np.sin(2*np.pi*y/self.n)
                                        for y in range(self.n+1)]))
        self.x_ellipse = self.x_ellipse[int(
            3*self.n//4):] + self.x_ellipse[:int(3*self.n//4)]
        self.y_ellipse = self.y_ellipse[int(
            3*self.n//4):] + self.y_ellipse[:int(3*self.n//4)]

        # Waypoints
        self.x_waypoints = self.x_circle + self.x_ellipse[::-1]
        self.y_waypoints = self.y_circle + self.y_ellipse[::-1]

    def get_centered_pos(self):
        return self.x+self.surf.get_width()/2, self.y+self.surf.get_height()/2

    def update_random_walk(self):

        # Movement
        direction = np.random.choice(self.directions)
        x, y = self.get_centered_pos()
        if direction == 'left':
            min_width = JOYSTICK_WINDOW[0]+self.surf.get_width()/2
            if x <= min_width:
                self.x = min_width-self.surf.get_width()/2
            else:
                self.x -= 5
        elif direction == 'right':
            max_width = WIDTH-JOYSTICK_WINDOW[0]-self.surf.get_width()/2
            if x >= max_width:
                self.x = max_width-self.surf.get_width()/2
            else:
                self.x += 5
        elif direction == 'down':
            min_height = JOYSTICK_WINDOW[1]+self.surf.get_height()/2
            if y <= min_height:
                self.y = min_height-self.surf.get_height()/2
            else:
                self.y -= 5
        else:
            max_height = HEIGHT-JOYSTICK_WINDOW[0]-self.surf.get_height()/2
            if y >= max_height:
                self.y = max_height-self.surf.get_height()/2
            else:
                self.y += 5

        # Update rect position
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """
        Moving in an "8" shape
        """

        # Circle
        # self.rect.centerx = self.x_circle[self.increment % len(self.x_circle)]
        # self.rect.centery = self.y_circle[self.increment % len(self.y_circle)]

        # Ellipse
        # self.rect.centerx = self.x_ellipse[self.increment % len(
        #     self.x_ellipse)]
        # self.rect.centery = self.y_ellipse[self.increment % len(
        #     self.y_ellipse)]

        # Ellipse and circle combined
        self.rect.centerx = self.x_waypoints[self.increment % len(
            self.x_waypoints)]
        self.rect.centery = self.y_waypoints[self.increment % len(
            self.y_waypoints)]

        self.increment += 1
