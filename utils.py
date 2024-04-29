from enum import Enum


class Tile(Enum):
    EMPTY = 0
    BOX = 1
    TARGET = 2
    WALL = 3
    PLAYER = 4
    TARGET_BOX = 5
    TARGET_PLAYER = 6

    def __str__(self) -> str:
        assert self in Tile, "Invalid tile"
        return {
            Tile.EMPTY: ' ',
            Tile.BOX: '$',
            Tile.TARGET: '.',
            Tile.WALL: '#',
            Tile.PLAYER: '@',
            Tile.TARGET_BOX: '*',
            Tile.TARGET_PLAYER: '+'
        }[self]


def parseTile(char: str) -> Tile:
    assert len(char) == 1, "Invalid tile character"
    return {
        ' ': Tile.EMPTY,
        '$': Tile.BOX,
        '.': Tile.TARGET,
        '#': Tile.WALL,
        '@': Tile.PLAYER,
        '*': Tile.TARGET_BOX,
        '+': Tile.TARGET_PLAYER
    }[char]


def parseLevel(levelData: str) -> list[list[Tile]]:
    lines = levelData.splitlines()
    return [[parseTile(char) for char in line] for line in lines]


class Vector2D:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def value(self, state: list[list[Tile]]) -> Tile:
        return state[self.y][self.x]

    def setValue(self, state: list[list[Tile]], value: Tile) -> None:
        state[self.y][self.x] = value
