import pygame
from config import W, H, TILE


class Grid:
    def __init__(self):
        self.grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

    def draw(self, screen, color):
        # Рисует сетку.
        for rect in self.grid:
            pygame.draw.rect(screen, color, rect, 1)
