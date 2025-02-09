import pygame


def handle_input(events, status):
    dx, rotate, drop_speed = 0, False, None
    running = True  # Флаг работы игры
    for event in events:
        if event.type == pygame.QUIT:
            return False, dx, rotate, drop_speed, status  # Завершаем игру
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                drop_speed = 100
            elif event.key == pygame.K_UP:
                rotate = True
            elif event.key == pygame.K_SPACE:
                if status == "game over":
                    status = "try play"
                else:
                    status = "to play"
    return running, dx, rotate, drop_speed, status
