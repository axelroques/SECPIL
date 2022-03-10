
from __init__ import BACKGROUND_COLOR, PALONNIER_WINDOW, NUMBER_WINDOW, JOYSTICK_WINDOW
from goal import GoalJoystick, GoalPalonnier
from player import Joystick, Palonnier
from gui import Background
import pygame


class Game:

    def __init__(self, screen, controller):
        self.running = True
        self.screen = screen
        self.controller = controller

        # Background
        self.bg = [Background(*params) for params in [PALONNIER_WINDOW,
                                                      NUMBER_WINDOW,
                                                      JOYSTICK_WINDOW]]

    def catch_exit(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
        if event.type == pygame.QUIT:
            self.running = False

    def draw(self, sprites):
        # Draw background
        self.screen.fill(BACKGROUND_COLOR)
        for bg in self.bg:
            self.screen.blit(bg.surf, bg.rect)

        # Draw sprites
        for sprite in sprites:
            self.screen.blit(sprite.surf, sprite.rect)
        # Display
        pygame.display.flip()


class First(Game):

    def __init__(self, screen, controller):
        super().__init__(screen, controller)

    def event_handler(self, player):
        """
        Two distinct paths depending on whether a controller is connected or not
        """

        # At least one controller is connected
        if self.controller != []:

            # Catch exit
            for event in pygame.event.get():
                self.catch_exit(event)

            # Joystick movement
            for joystick in self.controller:
                axes = joystick.get_numaxes()

                # Palonnier
                if axes == 3:
                    value = joystick.get_axis(2)
                    player.update(controller='palonnier',
                                  axis=2, value=value)

        # No controller
        if self.controller == []:

            # Catch exit
            for event in pygame.event.get():
                self.catch_exit(event)

            # Keyboard movement
            # KEYDOWN shows which keys were pressed on that frame only,
            # we need to use get_pressed()
            inputs = pygame.key.get_pressed()
            player.update(controller='keyboard', inputs=inputs)

    def run(self):

        # Initialization
        player = Palonnier()
        goal = GoalPalonnier()

        # Game clock
        clock = pygame.time.Clock()

        # Sprite group for easier rendering
        sprites = [player, goal]

        while self.running:

            self.event_handler(player)
            goal.update()

            # Draw
            self.draw(sprites)

            # 30 fps
            clock.tick(30)


class Second(Game):

    def __init__(self, screen, controller):
        super().__init__(screen, controller)

    def event_handler(self, player):
        """
        Two distinct paths depending on whether a controller is connected or not
        """

        # At least one controller is connected
        if self.controller != []:

            # Catch exit
            for event in pygame.event.get():
                self.catch_exit(event)

            # Joystick movement
            for joystick in self.controller:
                axes = joystick.get_numaxes()

                # Joystick
                if axes == 4:
                    for i in [0, 1]:
                        value = joystick.get_axis(i)
                        # Simple lower threshold on joystick value
                        if abs(value) > 0.05:
                            player.update(controller='joystick',
                                          axis=i, value=value)

        # No controller
        if self.controller == []:

            # Catch exit
            for event in pygame.event.get():
                self.catch_exit(event)

            # Keyboard movement
            # KEYDOWN shows which keys were pressed on that frame only,
            # we need to use get_pressed()
            inputs = pygame.key.get_pressed()
            player.update(controller='keyboard', inputs=inputs)

    def run(self):

        # Initialization
        player = Joystick()
        goal = GoalJoystick()

        # Game clock
        clock = pygame.time.Clock()

        # Sprite group for easier rendering
        sprites = [player, goal]

        while self.running:

            self.event_handler(player)
            goal.update()

            # Draw
            self.draw(sprites)

            # 30 fps
            clock.tick(30)


class Third(Game):

    def __init__(self, screen, controller):
        super().__init__(screen, controller)

    def event_handler(self, player_palonnier, player_joystick):
        """
        Here, two controllers must be connected
        """

        # Catch exit
        for event in pygame.event.get():
            self.catch_exit(event)

        # Controller movement
        for joystick in self.controller:
            axes = joystick.get_numaxes()

            # Joystick
            if axes == 4:
                for i in [0, 1]:
                    value = joystick.get_axis(i)
                    # Simple lower threshold on joystick value
                    if abs(value) > 0.05:
                        player_joystick.update(controller='joystick',
                                               axis=i, value=value)

            # Palonnier
            if axes == 3:
                value = joystick.get_axis(2)
                player_palonnier.update(controller='palonnier',
                                        axis=2, value=value)

    def run(self):

        # Initialization
        player_palonnier = Palonnier()
        player_joystick = Joystick()
        goal_palonnier = GoalPalonnier()
        goal_joystick = GoalJoystick()

        # Game clock
        clock = pygame.time.Clock()

        # Sprite group for easier rendering
        sprites = [player_palonnier, player_joystick,
                   goal_palonnier, goal_joystick]

        while self.running:

            self.event_handler(player_palonnier, player_joystick)
            goal_palonnier.update()
            goal_joystick.update()

            # Draw
            self.draw(sprites)

            # 30 fps
            clock.tick(30)
