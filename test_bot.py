import unittest

from bot import Orientations, Commands, Planet, Machine

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

    def test_get_coordinate(self):
        self.assertEqual(self.mars.get_coordinate(1, 1), 1)

    def test_get_coordinate_out_of_grid_raise_exception(self):
        with self.assertRaises(IndexError):
            self.mars.get_coordinate(7, 8)

    def test_set_coordinate(self):
        self.mars.set_coordinate(1, 1, 0)
        self.assertEqual(self.mars.get_coordinate(1, 1), 0)

    def test_set_coordinate_out_of_grid_raise_exception(self):
        with self.assertRaises(IndexError):
            self.mars.set_coordinate(7, 8, 0)

    def test_high_value_coordinate_raise_exception(self):
        with self.assertRaises(ValueError):
            Planet(51, 3)

    def test_negative_value_raise_exception(self):
        with self.assertRaises(ValueError):
            Planet(-5, 3)


class MachineTest(unittest.TestCase):
 
    def setUp(self):
        self.mars = Planet(5, 3)
        self.robot = Machine(self.mars, 2, 3, 'L')

    def test_process_command(self):
        #self.assertEqual(self.robot.process_command('L'), 0)
        pass

        



if __name__ == '__main__':
    unittest.main()