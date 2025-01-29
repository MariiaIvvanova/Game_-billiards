import pygame
from config import GAME_RES, FPS, COLORS
from core.game import Game
from core.grid import Grid
from core.renderer import Renderer
from core.input_handler import handle_input


def main():
    pygame.init()
    screen = pygame.display.set_mode(GAME_RES)
    clock = pygame.time.Clock()

    game = Game()
    grid = Grid()
    renderer = Renderer(screen)

    running = True
    while running:
        screen.fill(pygame.Color(COLORS["background"]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_input(game, event)

        game.update()
        grid.draw(screen, COLORS["grid"])
        renderer.draw_figure(game.figure, COLORS["figure"])

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
