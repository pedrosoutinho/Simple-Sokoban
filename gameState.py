from typing import Iterator
from utils import Vector2D, Tile


class State:
    length: int
    width: int
    tiles: list[list[Tile]]

    def __init__(self, tiles: list[list[Tile]]) -> None:
        self.length = len(tiles)
        self.width = len(tiles[0])
        self.tiles = tiles

    def inBounds(self, pos: Vector2D) -> bool:
        return 0 <= pos.x < self.width and 0 <= pos.y < self.length

    def moveBox(self, boxPos: Vector2D, delta: Vector2D) -> bool:
        endPos = boxPos + delta

        if not self.inBounds(endPos):
            return False

        if endPos.value(self.tiles) != Tile.EMPTY:
            return False

        if boxPos.value(self.tiles) == Tile.TARGET_BOX:
            boxPos.setValue(self.tiles, Tile.TARGET)
        else:
            boxPos.setValue(self.tiles, Tile.EMPTY)

        if endPos.value(self.tiles) == Tile.TARGET:
            endPos.setValue(self.tiles, Tile.TARGET_BOX)
        else:
            endPos.setValue(self.tiles, Tile.BOX)

        return True

    def playerMove(self, playerPos: Vector2D, delta: Vector2D) -> bool:
        endPos = playerPos + delta

        if not self.inBounds(endPos):
            return False

        if endPos.value(self.tiles) == Tile.WALL:
            return False

        if endPos.value(self.tiles) == Tile.BOX:
            if not self.moveBox(endPos, delta):
                return False

        playerPos.setValue(self.tiles, Tile.EMPTY)
        endPos.setValue(self.tiles, Tile.PLAYER)
        return True

    def won(self) -> bool:
        for pos in self.positions():
            if pos.value(self.tiles) == Tile.TARGET:
                return False
        return True

    def positions(self) -> Iterator[Vector2D]:
        for y in range(self.length):
            for x in range(self.width):
                yield Vector2D(x, y)
