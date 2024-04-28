import enum from Enum

class Cell(Enum):
    EMPTY = 0
    BOX = 1
    TARGET = 2
    WALL = 3
    PLAYER = 4

    def __str__(self) -> str:
        return {
            Cell.EMPTY: ' ',
            Cell.BOX: '$',
            Cell.TARGET: '.',
            Cell.WALL: '#',
            Cell.PLAYER: '@'
        }[self]

def parseTile(tile: str) -> Cell:
    return {
        ' ': Cell.EMPTY,
        '$': Cell.BOX,
        '.': Cell.TARGET,
        '#': Cell.WALL,
        '@': Cell.PLAYER
    }[tile]

class Vector2D:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def value(self, state: List[List[Cell]]) -> Cell:
        return state[self.y][self.x]

    def setValue(self, state: List[List[Cell]], value: Cell):
        state[self.y][self.x] = value

