def check_borders(figure, field, W, H):
    for block in figure:
        if block.x < 0 or block.x >= W or block.y >= H or field[block.y][block.x]:
            return False
    return True
