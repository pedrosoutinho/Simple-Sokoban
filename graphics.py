import pygame
from gameState import State
from utils import Tile


class Renderer:
    # scale of one cell in pygame
    cellSize: int = 80

    playerSprite = pygame.image.load("sprites/player.png")
    groundSprite = pygame.image.load("sprites/ground.png")
    crateSprite = pygame.image.load("sprites/crate.png")
    wallSprite = pygame.image.load("sprites/wall.png")
    targetSprite = pygame.image.load("sprites/target.png")
    correctSprite = pygame.image.load("sprites/correct.png")

    # dictionary to map tile to sprite
    tileSprite = {
        Tile.EMPTY: groundSprite,
        Tile.BOX: crateSprite,
        Tile.TARGET: targetSprite,
        Tile.WALL: wallSprite,
        Tile.PLAYER: playerSprite,
        Tile.TARGET_BOX: correctSprite,
        Tile.TARGET_PLAYER: playerSprite
    }

    def __init__(self, state: State) -> None:
        pygame.init()
        self.Height = state.length * self.cellSize
        self.Width = state.width * self.cellSize
        self.screen = pygame.display.set_mode((self.Width, self.Height))
        pygame.display.set_caption("Sokoban")

    def close(self) -> None:
        pygame.quit()

    def updateState(self, state: State) -> None:
        # background rgb color
        self.screen.fill((30, 30, 30))

        for pos in state.positions():
            px = pos.x * self.cellSize
            py = pos.y * self.cellSize
            self.screen.blit(self.tileSprite[pos.value(state.tiles)], (px, py))

        pygame.display.update()
