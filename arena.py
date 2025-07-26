import pygame

class Arena:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (30, 20, 10), (0, self.screen.get_height() - 100, self.screen.get_width(), 100))
