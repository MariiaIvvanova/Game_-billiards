import pygame
from copy import deepcopy
from random import choice
from config import W, H, GAME_RES, FPS, palette
from core.tetromino import figures, Figure
from core.renderer import draw_grid, draw_figure, draw_field
from core.input_handler import handle_input
from core.game import rotate_figure, break_lines, check_borders


def init_game():
    pygame.init()
    status = "menu"
    screen = pygame.display.set_mode(GAME_RES)
    clock = pygame.time.Clock()
    grid = [pygame.Rect(x * 30, y * 30, 30, 30) for x in range(W) for y in range(H)]
    field = [[0 for _ in range(W)] for _ in range(H)]
    return screen, clock, grid, field, status


def process_input(status):
    return handle_input(pygame.event.get(), status)


def update_figure(figure, dx, rotate, field):
    figure_old = deepcopy(figure)
    for block in figure:
        block.x += dx
    if not check_borders(figure, field, W, H):
        figure = deepcopy(figure_old)
    if rotate:
        figure = rotate_figure(figure, field)
    return figure


def update_animation(figure, field, anim_count, anim_speed, anim_limit, f_object):
    status = "to play"
    color = f_object.color
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for block in figure:
            block.y += 1
        if not check_borders(figure, field, W, H):
            for block in figure_old:
                if block.y == 0:
                    status = "game over"
                field[block.y][block.x] = pygame.Color(f_object.color)
            field = break_lines(field)
            figure = deepcopy(choice(figures))
            color = choice(palette)
            anim_limit = 2000
    return figure, color, field, anim_count, anim_limit, status


def draw_game(screen, grid, figure, color, field, back_ground, status):
    if status == "to play":
        screen.fill(pygame.Color('black'))
        screen.blit(back_ground, (0, 0))
        draw_grid(screen, grid)
        draw_figure(screen, figure, pygame.Color(color))
        draw_field(screen, field)
    pygame.display.flip()


def main():
    screen, clock, grid, field, status = init_game()
    anim_count, anim_speed, anim_limit = 0, 60, 2000
    figure = deepcopy(choice(figures))
    figure = Figure(figure, choice(palette))
    menu_screen = pygame.image.load('assets/заставка1.png')
    menu_screen = pygame.transform.scale(menu_screen, (300, 600))
    game_over_screen = pygame.image.load('assets/game_over.webp')
    game_over_screen = pygame.transform.scale(game_over_screen, (300, 600))
    back_ground = pygame.image.load('assets/рабочий_стол_игры.jpeg')
    back_ground = pygame.transform.scale(back_ground, (300, 600))
    screen.blit(menu_screen, (0, 0))
    running = True

    while running:
        running, dx, rotate, drop_speed, status = process_input(status)
        if drop_speed:
            anim_limit = drop_speed
        if status == "to play":
            figure.figure = update_figure(figure.figure, dx, rotate, field)
            figure.figure, figure.color, field, anim_count, anim_limit, status = update_animation(figure.figure, field, anim_count, anim_speed, anim_limit, figure)
        elif status == "game over":
            screen.blit(game_over_screen, (0, 0))
        draw_game(screen, grid, figure.figure, figure.color,  field, back_ground, status)
        clock.tick(FPS)


if __name__ == "__main__":
    main()

