import numpy as np

from enum import Enum

class Orientations(Enum):
    """Available Orientations"""
    X_PLUS_ONE = "E"
    X_MINUS_ONE = "W"
    Y_PLUS_ONE = "N"
    Y_MINUS_ONE = "S"


class Movement():
    pass

class Commands(Enum):
    """Available Commands"""
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"
    pass

class Planet():
    """Planet is a rectangular grid
    like [1, 1
          1, 0]
    where 1 represents general grid location
    and 0 represents scented grid location
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__grid = np.ones((x, y))
    

class Robot():
    """Robot class"""
    pass


if __name__ == '__main__':
    pass