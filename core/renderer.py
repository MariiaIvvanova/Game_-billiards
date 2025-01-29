import pygame
from config import TILE


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

    def draw_figure(self, figure, color):
        # Рисует фигуру.
        for block in figure.blocks:
            self.figure_rect.x = block.x * TILE
            self.figure_rect.y = block.y * TILE
            pygame.draw.rect(self.screen, pygame.Color(color), self.figure_rect)
