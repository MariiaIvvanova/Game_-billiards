import pygame
from copy import deepcopy
from random import choice
from config import W, H, GAME_RES, FPS
from core.tetromino import figures
from core.utils import check_borders
from core.renderer import draw_grid, draw_figure, draw_field
from core.input_handler import handle_input


def rotate_figure(figure, field):
    """Вращение фигуры вокруг её центра."""
    center = figure[0]
    figure_old = deepcopy(figure)
    for block in figure:
        x = block.y - center.y
        y = block.x - center.x
        block.x = center.x - x
        block.y = center.y + y
    if not check_borders(figure, field, W, H):
        return figure_old  # Откат вращения при коллизии
    return figure


def break_lines(field):
    """Удаление полностью заполненных линий."""
    line = H - 1
    for row in range(H - 1, -1, -1):
        count = sum(1 for i in range(W) if field[row][i])
        field[line] = field[row]
        if count < W:
            line -= 1
        else:
            field[line] = [0] * W  # Очищаем линию
    return field


def main():
    pygame.init()
    screen = pygame.display.set_mode(GAME_RES)
    clock = pygame.time.Clock()

    grid = [pygame.Rect(x * 30, y * 30, 30, 30) for x in range(W) for y in range(H)]
    field = [[0 for _ in range(W)] for _ in range(H)]

    anim_count, anim_speed, anim_limit = 0, 60, 2000
    figure = deepcopy(choice(figures))

    running = True
    while running:
        # dx, rotate, drop_speed = 0, False, None
        running, dx, rotate, drop_speed = handle_input(pygame.event.get())

        if drop_speed:
            anim_limit = drop_speed

        # Движение по оси X
        figure_old = deepcopy(figure)
        for block in figure:
            block.x += dx
        if not check_borders(figure, field, W, H):
            figure = deepcopy(figure_old)

        # Вращение
        if rotate:
            figure = rotate_figure(figure, field)

        # Движение вниз
        anim_count += anim_speed
        if anim_count > anim_limit:
            anim_count = 0
            figure_old = deepcopy(figure)
            for block in figure:
                block.y += 1
            if not check_borders(figure, field, W, H):
                for block in figure_old:
                    field[block.y][block.x] = pygame.Color("White")
                field = break_lines(field)  # Проверяем удаление линий
                figure = deepcopy(choice(figures))
                anim_limit = 2000

        # Отрисовка
        screen.fill(pygame.Color('black'))
        draw_grid(screen, grid)
        draw_figure(screen, figure, pygame.Color("white"))
        draw_field(screen, field)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
