from Scenes import GameScene
from SceneBase import SceneBase
import pygame
from Textboxes import *
from Konstanten import *
from Buttons import *

active_color = (255, 0, 0)
inactive_color = (0, 255, 0)


class ScoreScreen(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        print("score")

    def start_game(self):
        self.SwitchToScene(GameScene.GameScene())

    def quit_game(self):
        quit()

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass
    
    def Render(self, screen):

        # For the sake of brevity, the title scene is a blank red screen
        #screen.fill((0, 0, 0))

        button("Continue", 500, 200, 200, 50, active_color, inactive_color, screen, self.start_game)
        button("Quits", 500, 600, 200, 50, active_color, inactive_color, screen, self.quit_game)