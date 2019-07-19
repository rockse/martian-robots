import numpy as np

from enum import Enum

ALLOWED_COORDINATE = 51

class Orientations(Enum):
    """Available Orientations"""
    X_PLUS_ONE = "E"
    X_MINUS_ONE = "W"
    Y_PLUS_ONE = "N"
    Y_MINUS_ONE = "S"

    def turn_right(self):
        if self.name == "X_PLUS_ONE":
            return self.Y_MINUS_ONE
        if self.name == "Y_MINUS_ONE":
            return self.X_MINUS_ONE
        if self.name == "X_MINUS_ONE":
            return self.Y_PLUS_ONE
        if self.name == "Y_PLUS_ONE":
            return self.X_PLUS_ONE

        raise ValueError
            
    
    def turn_left(self):
        if self.name == "X_PLUS_ONE":
            return self.Y_PLUS_ONE
        if self.name == "Y_PLUS_ONE":
            return self.X_MINUS_ONE
        if self.name == "X_MINUS_ONE":
            return self.Y_MINUS_ONE
        if self.name == "Y_MINUS_ONE":
            return self.X_PLUS_ONE

        raise ValueError
    
    @classmethod
    def help(cls):
        return f'''Avaiable commands are {cls.X_PLUS_ONE}, {cls.X_MINUS_ONE}, 
            {cls.Y_PLUS_ONE} and {cls.Y_MINUS_ONE}'''


class Movement():
    pass

class Commands(Enum):
    """Available Commands"""
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"
    
    @classmethod
    def help(cls):
        return f'Avaiable commands are {cls.LEFT}, {cls.RIGHT} and {cls.FORWARD}'

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
        self.__grid = np.ones((x+1, y+1), dtype='int')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        if not isinstance(v, int) or v not in range(ALLOWED_COORDINATE): 
            raise ValueError("x coordinate can be from 0 to 50")
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        if not isinstance(v, int) or v not in range(ALLOWED_COORDINATE):
            raise ValueError("y coordinate can be from 0 to 50")
        self._y = v

    def get_coordinate(self, a, b):
        if a not in range(ALLOWED_COORDINATE) or a not in range(ALLOWED_COORDINATE): 
            raise IndexError()
        
        return self.__grid[a, b]

    def set_coordinate(self, a, b, value):
        if a not in range(ALLOWED_COORDINATE) or a not in range(ALLOWED_COORDINATE): 
            raise IndexError()
        
        self.__grid[a, b] = value

    
class Machine():
    """Machine class"""

    def __init__(self, grid, x, y, orientation):
        self.orientation = orientation
        self.x = x
        self.y = y
        self.grid = grid
        self.__lost = False

    def __move_forward(self):
        last_position = (self.x, self.y)

        if self.orientation == Orientations.Y_PLUS_ONE:
            self.y = self.y + 1 
        if self.orientation == Orientations.Y_MINUS_ONE:
            self.y = self.y - 1 
        if self.orientation == Orientations.X_PLUS_ONE:
            self.x = self.x + 1 
        if self.orientation == Orientations.X_MINUS_ONE:
            self.x = self.x - 1

        try:
            if self.x < 0 or self.y < 0: raise IndexError()
            self.grid.get_coordinate(self.x, self.y)
        except IndexError:
            if self.grid.get_coordinate(*last_position) == 0:
                self.x, self.y = last_position
            else:
                self.x, self.y = last_position
                self.grid.set_coordinate(self.x, self.y, 0)
                self.__lost = True 

    def __turn_left(self):
        self.orientation = self.orientation.turn_left()

    def __turn_right(self):
        self.orientation = self.orientation.turn_right()

    def __process_command(self, command):
        if command not in [e.value for e in Commands]:
            raise Exception("Invalid command")

        if self.__lost is True: return
        
        if Commands(command) == Commands.LEFT:
            self.__turn_left()
        elif Commands(command) == Commands.RIGHT:
            self.__turn_right()
        elif Commands(command) == Commands.FORWARD:
            self.__move_forward()

    def processor(self, commands):
        for c in commands:
            self.__process_command(c)
    
    def __str__(self):
        description = ' '.join([str(self.x), str(self.y), self.orientation.value, 'LOST' if self.__lost else ''])
        return description.strip()


if __name__ == '__main__':
    pass