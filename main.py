import sys

import pygame

from gameState import State
from utils import Vector2D, parseLevel
from graphics import Renderer
from game import Game

LEFT = Vector2D(-1, 0)
RIGHT = Vector2D(1, 0)
UP = Vector2D(0, -1)
DOWN = Vector2D(0, 1)

if __name__ == '__main__':
    # choose level
    args = sys.argv[1:]
    level = int(args[0]) if args else 0

    # open file txt
    try:
        with open(f"levels/{level}.txt") as file:
            levelData = file.read()
    except FileNotFoundError:
        print(f"Level {level} not found")
        sys.exit()

    initialState = State(parseLevel(levelData))
    renderer = Renderer(initialState)
    renderer.updateState(initialState)
    game = Game(initialState)

    while not game.won():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                renderer.close()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    game.movePlayer(UP)
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    game.movePlayer(DOWN)
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    game.movePlayer(LEFT)
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    game.movePlayer(RIGHT)
                elif event.key == pygame.K_r:
                    game.resetGame()
                elif event.key == pygame.K_BACKSPACE:
                    game.undoMove()

                renderer.updateState(game.currentState())

    print("gg")
    renderer.close()
