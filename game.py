from copy import deepcopy
from gameState import State
from utils import Vector2D


class Game:
    stateHistory: list[State]
    initialState: State

    def __init__(self, initialState: State):
        self.stateHistory = [initialState]
        self.initialState = initialState

    def currentState(self) -> State:
        return self.stateHistory[-1]

    def movePlayer(self, direction: Vector2D) -> None:
        stateNow = deepcopy(self.currentState())
        if stateNow.playerMove(stateNow.playerPosition(), direction):
            self.stateHistory.append(stateNow)

    def undoMove(self) -> bool:
        if len(self.stateHistory) > 1:
            self.stateHistory.pop()
            return True
        return False

    def resetGame(self) -> None:
        self.stateHistory = [self.initialState]

    def won(self) -> bool:
        return self.currentState().won()
