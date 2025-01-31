from copy import deepcopy
from core.tetromino import Tetromino
from config import W, H


class Game:
    def __init__(self):
        self.figure = Tetromino(0)
        self.anim_count, self.anim_speed, self.anim_limit = 0, 60, 2000

    def check_borders(self):
        # Проверка выхода за границы.
        for block in self.figure.blocks:
            if block.x < 0 or block.x >= W or block.y >= H:
                return False
        return True

    def update(self):
        # Обновление состояния (падение фигуры).
        score = 0 #счетчик очков
        self.anim_count += self.anim_speed
        if self.anim_count > self.anim_limit:
            self.anim_count = 0
            figure_old = deepcopy(self.figure.blocks)
            for block in self.figure.blocks:
                block.y += 1
            if not self.check_borders():
                self.figure.blocks = deepcopy(figure_old)
                self.anim_limit = 2000  # Сбрасываем скорость падения
                score += len(self.figure.blocks)  #

