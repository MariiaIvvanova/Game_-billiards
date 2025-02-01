import pygame
from config import TILE


def draw_grid(screen, grid):
    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]


def draw_figure(screen, figure, color):
    figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
    for block in figure:
        figure_rect.x, figure_rect.y = block.x * TILE, block.y * TILE
        pygame.draw.rect(screen, color, figure_rect)


def draw_field(screen, field):
    figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col:
                figure_rect.x, figure_rect.y = x * TILE, y * TILE
                pygame.draw.rect(screen, col, figure_rect)
