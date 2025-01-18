import pygame


class Table:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (100, 50, 0), (50, 50, 700, 500))  # Рамка
        pygame.draw.rect(self.screen, (0, 100, 0), (60, 60, 680, 480))  # Поле
        # Лузы
        for hole in [(60, 60), (740, 60), (60, 540), (740, 540), (400, 60), (400, 540)]:
            pygame.draw.circle(self.screen, (0, 0, 0), hole, 20)
