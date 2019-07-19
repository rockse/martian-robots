import unittest

from bot import Orientations, Commands, Planet

class OrientationsTest(unittest.TestCase):
 
    def setUp(self):
        self.orientation = Orientations('N')

    def test_orientations_value(self):
        self.assertEqual(self.orientation.value, 'N')


class CommandsTest(unittest.TestCase):
 
    def setUp(self):
        self.command = Commands('L')

    def test_commands_value(self):
        self.assertEqual(self.command.value, 'L')

class PlanetTest(unittest.TestCase):
 
    def setUp(self):
        self.mars = Planet(2, 3)


if __name__ == '__main__':
    unittest.main()