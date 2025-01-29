import pygame


def handle_input(game, event):
    # Обрабатывает клавиши.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            game.figure.move(-1, 0)
        elif event.key == pygame.K_RIGHT:
            game.figure.move(1, 0)
        elif event.key == pygame.K_DOWN:
            game.anim_limit = 100  # Ускоряем падение

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            game.anim_limit = 2000  # Возвращаем стандартную скорость
