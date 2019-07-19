import numpy as np

from enum import Enum

ALLOWED_COORDINATE = 50

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

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        if not isinstance(v, int) or v not in range(ALLOWED_COORDINATE): 
            raise Exception("x coordinate can be from 0 to 50")
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        if not isinstance(v, int) or v not in range(ALLOWED_COORDINATE):
            raise Exception("y coordinate can be from 0 to 50")
        self._y = v

    def __update_grid_accessibility(self, x, y):
        pass
    

class Robot():
    """Robot class"""
    pass


if __name__ == '__main__':
    pass