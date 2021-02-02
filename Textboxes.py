from Konstanten import *
import pygame


class TextBox:
    # Erzeugen einer Box mit Farbe & Text
    def __init__(self, rect, text=''):
        self.rect = pygame.Rect(rect)
        self.color = pygame.Color(20, 200, 20)
        self.text = text
        self.txt_surface = pygame.font.Font(
            None, 32).render(text, True, self.color)
        self.active = False
    # zeichnet textbox

    def draw(self, screen):
        # Zeichnen Textbox mit Rand in gleicher Farbe
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
    # Update des Textes in der Box

    def update(self, screen, text, score):
        # Übergibt den neuen Text
        self.txt_surface = pygame.font.Font(
            None, 32).render(text+" "+score, True, self.color)
        # erzeugt neuen Text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
