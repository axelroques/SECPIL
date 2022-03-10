
from __init__ import BACKGROUND_COLOR, WIDTH, HEIGHT
import pygame
from games import First, Second, Third
from gui import Button, Text


class Menu:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('SECPIL')

        # Game controllers
        self.joysticks = [pygame.joystick.Joystick(
            x) for x in range(pygame.joystick.get_count())]

        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.buttons = [Button(x, y) for x, y in zip([490, 490, 490, 490],
                                                     [40, 220, 400, 580])]
        self.texts = [Text(f'Test {i}', button)
                      for i, button in enumerate(self.buttons)]

    def check_game_controllers(self):
        if self.joysticks:
            print('Available controllers:')
            for joystick in self.joysticks:
                joystick.init()
                print(
                    f'\t- Name: {joystick.get_name()} ; Initialized: {joystick.get_init()}')
        else:
            print('No available controllers, defaulting to keyboard')

    def catch_exit(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
        if event.type == pygame.QUIT:
            self.running = False

    def draw(self):
        # Fill the screen with black
        self.screen.fill(BACKGROUND_COLOR)
        # Draw buttons
        for button in self.buttons:
            self.screen.blit(button.surf, button.rect)
        # Draw texts
        for text in self.texts:
            self.screen.blit(text.surf, text.rect)
        # Display
        pygame.display.flip()

    def run(self):

        # Monitor game controllers available
        self.check_game_controllers()

        # Game clock
        clock = pygame.time.Clock()

        click = False
        while self.running:

            # Mouse control
            mx, my = pygame.mouse.get_pos()

            # Detect clicks on menu buttons
            for i, button in enumerate(self.buttons):
                if button.rect.collidepoint((mx, my)):
                    if click:
                        if i == 0:
                            game = First(
                                self.screen, self.joysticks)
                            game.run()
                        elif i == 1:
                            game = Second(
                                self.screen, self.joysticks)
                            game.run()
                        elif i == 2:
                            if len(self.joysticks) < 2:
                                print('Please connect two controllers')
                            else:
                                game = Third(
                                    self.screen, self.joysticks)
                                game.run()
                        else:
                            print('Not implemented yet!')

            click = False
            # Event queue
            for event in pygame.event.get():

                # Exit conditions
                self.catch_exit(event)

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            # Draw
            self.draw()

            # 30 fps
            clock.tick(30)
