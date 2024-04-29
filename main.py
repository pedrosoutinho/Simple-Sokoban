import sys

import pygame

from gameState import State
from utils import parseLevel
from graphics import Renderer

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

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                renderer.close()
                quit()
