import pygame
from copy import deepcopy
from random import choice
from config import W, H, GAME_RES, RES, FPS, palette, TILE
from core.tetromino import figures, Figure
from core.renderer import draw_grid, draw_figure, draw_field
from core.input_handler import handle_input
from core.game import rotate_figure, break_lines, check_borders


# Инициализация игры
def init_game():
    pygame.init()
    status = "menu"
    screen = pygame.display.set_mode(RES)
    game_sc = pygame.Surface(GAME_RES)
    clock = pygame.time.Clock()
    grid = [pygame.Rect(x * 30, y * 30, 30, 30) for x in range(W) for y in range(H)]
    field = [[0 for _ in range(W)] for _ in range(H)]
    return screen, game_sc, clock, grid, field, status


# Загрузка всех изображений
def load_images():
    menu_screen = pygame.image.load('assets/заставка1.png')
    menu_screen = pygame.transform.scale(menu_screen, RES)

    game_over_screen = pygame.image.load('assets/game_over.webp')
    game_over_screen = pygame.transform.scale(game_over_screen, RES)

    back_ground = pygame.image.load('assets/рабочий_стол_игры.jpeg')
    back_ground = pygame.transform.scale(back_ground, RES)

    bg = pygame.image.load("assets/bg.jpeg")
    bg = pygame.transform.scale(bg, RES)

    return menu_screen, game_over_screen, back_ground, bg


# Обработка ввода
def process_input(status):
    return handle_input(pygame.event.get(), status)


# Обновление фигуры
def update_figure(figure, dx, rotate, field):
    figure_old = deepcopy(figure)
    for block in figure:
        block.x += dx
    if not check_borders(figure, field, W, H):
        figure = deepcopy(figure_old)
    if rotate:
        figure = rotate_figure(figure, field)
    return figure


def update_animation(figure, field, anim_count, anim_speed, anim_limit, f_object, next_figure):
    score = 0  # Локальная переменная для счёта
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
            field = break_lines(field)  # Получаем новый счёт после удаления линий

            # Заменить текущую фигуру на следующую
            figure = deepcopy(next_figure)
            next_figure = deepcopy(choice(figures))  # Обновляем следующую фигуру

            color = choice(palette)
            anim_limit = 2000
    return figure, color, field, anim_count, anim_limit, status, next_figure


# Отображение игры
def draw_game(screen, game_sc, grid, figure, color, field, back_ground, status):
    if status == "to play":
        game_sc.blit(back_ground, (0, 0))  # Фон для игрового поля
        draw_grid(game_sc, grid)
        draw_figure(game_sc, figure, pygame.Color(color))
        draw_field(game_sc, field)
        screen.blit(game_sc, (0, 0))  # Отображение игрового поля на экране
    pygame.display.flip()


def draw_next_figure(screen, next_figure, palette, scale=1):
    next_figure_rect = pygame.Rect((W * TILE) + 50, 50, 30 * scale, 30 * scale)
    block_size = TILE * scale
    for i, block in enumerate(next_figure):
        x_offset = (block[0] * block_size) - 100
        y_offset = (block[1] * block_size)

        block_rect = pygame.Rect(next_figure_rect.x + x_offset, next_figure_rect.y + y_offset, block_size, block_size)
        pygame.draw.rect(screen, pygame.Color(palette[0]), block_rect)


def draw_text(screen, text, x, y, font_size=30):
    font = pygame.font.SysFont("Arial", font_size)
    text_surface = font.render(text, True, pygame.Color("white"))
    screen.blit(text_surface, (x, y))


# Главная функция игры
def main():
    screen, game_sc, clock, grid, field, status = init_game()
    anim_count, anim_speed, anim_limit = 0, 60, 2000
    figure = deepcopy(choice(figures))
    figure = Figure(figure, choice(palette))
    next_figure = deepcopy(choice(figures))

    # Загрузка изображений
    menu_screen, game_over_screen, back_ground, bg = load_images()
    running = True

    while running:
        running, dx, rotate, drop_speed, status = process_input(status)
        if drop_speed:
            anim_limit = drop_speed

        screen.blit(bg, (0, 0))  # Отрисовка основного фона

        if status == "menu":
            screen.blit(menu_screen, (0, 0))  # Показываем меню
        elif status == "to play":
            draw_next_figure(screen, next_figure, palette)
            figure.figure = update_figure(figure.figure, dx, rotate, field)
            figure.figure, figure.color, field, anim_count, anim_limit, status, next_figure = update_animation(
                figure.figure, field, anim_count, anim_speed, anim_limit, figure, next_figure)  # Передаём score обратно

            # Отрисовка игры
            draw_game(screen, game_sc, grid, figure.figure, figure.color, field, back_ground, status)  # Отрисовка сетки и фигур

        elif status == "game over":
            screen.blit(game_over_screen, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
