from Konstanten import *
import pygame


class TextBox:

    def __init__(self, rect, text=''):
        self.rect = pygame.Rect(rect)
        self.color = pygame.Color(20, 200, 20)
        self.text = text
        self.txt_surface = pygame.font.Font(
            None, 32).render(text, True, self.color)
        self.active = False

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def update(self, screen, text, score):

        self.txt_surface = pygame.font.Font(
            None, 32).render(text+" "+score, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
