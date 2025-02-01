import pygame
from copy import deepcopy
from random import choice
from config import W, H, GAME_RES, FPS
from core.tetromino import figures
from core.renderer import draw_grid, draw_figure, draw_field
from core.input_handler import handle_input
from core.game import rotate_figure, break_lines, check_borders


def init_game():
    pygame.init()
    screen = pygame.display.set_mode(GAME_RES)
    clock = pygame.time.Clock()
    grid = [pygame.Rect(x * 30, y * 30, 30, 30) for x in range(W) for y in range(H)]
    field = [[0 for _ in range(W)] for _ in range(H)]
    return screen, clock, grid, field


def process_input():
    return handle_input(pygame.event.get())


def update_figure(figure, dx, rotate, field):
    figure_old = deepcopy(figure)
    for block in figure:
        block.x += dx
    if not check_borders(figure, field, W, H):
        figure = deepcopy(figure_old)
    if rotate:
        figure = rotate_figure(figure, field)
    return figure


def update_animation(figure, field, anim_count, anim_speed, anim_limit):
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for block in figure:
            block.y += 1
        if not check_borders(figure, field, W, H):
            for block in figure_old:
                field[block.y][block.x] = pygame.Color("White")
            field = break_lines(field)
            figure = deepcopy(choice(figures))
            anim_limit = 2000
    return figure, field, anim_count, anim_limit


def draw_game(screen, grid, figure, field):
    screen.fill(pygame.Color('black'))
    draw_grid(screen, grid)
    draw_figure(screen, figure, pygame.Color("white"))
    draw_field(screen, field)
    pygame.display.flip()


def main():
    screen, clock, grid, field = init_game()
    anim_count, anim_speed, anim_limit = 0, 60, 2000
    figure = deepcopy(choice(figures))
    running = True

    while running:
        running, dx, rotate, drop_speed = process_input()
        if drop_speed:
            anim_limit = drop_speed
        figure = update_figure(figure, dx, rotate, field)
        figure, field, anim_count, anim_limit = update_animation(figure, field, anim_count, anim_speed, anim_limit)
        draw_game(screen, grid, figure, field)
        clock.tick(FPS)


if __name__ == "__main__":
    main()

