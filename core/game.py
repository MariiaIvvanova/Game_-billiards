from copy import deepcopy
from config import W, H


def rotate_figure(figure, field):
    # Вращение фигуры вокруг её центра.
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
    line = H - 1
    for row in range(H - 1, -1, -1):
        count = sum(1 for i in range(W) if field[row][i])  # Подсчёт занятых ячеек в строке
        field[line] = field[row]
        if count < W:
            line -= 1
        else:
            field[line] = [0] * W
    return field


def check_borders(figure, field, W, H):
    for block in figure:
        if block.x < 0 or block.x >= W or block.y >= H or field[block.y][block.x]:
            return False
    return True
