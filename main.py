import pygame
from table import Table
from ball import Ball

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бильярд")

# Цвета
GREEN = (0, 100, 0)

# Объекты игры
table = Table(screen)
balls = [Ball(400, 300, 15, (255, 0, 0))]  # Пример красного шара

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка
    screen.fill(GREEN)
    table.draw()

    for ball in balls:
        ball.move()  # Движение шаров
        ball.draw(screen)  # Отрисовка шаров

    pygame.display.flip()

pygame.quit()
