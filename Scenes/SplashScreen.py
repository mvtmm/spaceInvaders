from Scenes import GameScene
from SceneBase import SceneBase
import pygame
from Textboxes import *
from Konstanten import *
from Buttons import *

active_color = (255, 0, 0)
inactive_color = (0, 255, 0)


class SplashScreen(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def start_game(self):
        self.SwitchToScene(GameScene.GameScene())

    def options(self):
        pass

    def quit_game(self):
        pygame.quit()

    def ProcessInput(self, events, pressed_keys):
        for event in events:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                pass

    def Update(self):
        pass

    def Render(self, screen):

        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 250, 250))

        # Level und Punkte anzeigen
        level_label = TextBox((0, 0, 200, 32), "Level")
        score_label = TextBox((1000, 0, 200, 32), "Score")

        menuItems = [level_label, score_label]
        for box in menuItems:
            box.draw(screen)

        button("Start Game", 500, 200, 200, 50, active_color,
               inactive_color, screen, self.start_game)

        button("Options", 500, 400, 200, 50, active_color,
               inactive_color, screen, self.options)

        button("Quit", 500, 600, 200, 50, active_color,
               inactive_color, screen, self.quit_game)
