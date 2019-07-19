import unittest

from bot import Orientations, Commands, Planet, Machine

class OrientationsTest(unittest.TestCase):
 
    def setUp(self):
        self.orientation_n = Orientations('N')
        self.orientation_s = Orientations('S')

    def test_orientations_value(self):
        self.assertEqual(self.orientation_n.value, 'N')
    
    def test_turn_right_north(self):
        self.orientation_n = self.orientation_n.turn_right()
        self.assertEqual(self.orientation_n.value, 'E')

    def test_turn_right_south(self):
        self.orientation_s = self.orientation_s.turn_right()
        self.assertEqual(self.orientation_s.value, 'W')

    def test_turn_left_north(self):
        self.orientation_n = self.orientation_n.turn_left()
        self.assertEqual(self.orientation_n.value, 'W')

    def test_turn_left_south(self):
        self.orientation_s = self.orientation_s.turn_left()
        self.assertEqual(self.orientation_s.value, 'E')

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
        self.orientation1 = Orientations('E')
        self.robot1 = Machine(self.mars, 1, 1, self.orientation1)
        self.orientation2 = Orientations('N')
        self.robot2 = Machine(self.mars, 3, 2, self.orientation2)
        self.orientation3 = Orientations('N')
        self.robot3 = Machine(self.mars, 3, 2, self.orientation3)
    
    def test_process_command(self):
        commands = ['R', 'F', 'R', 'F', 'R', 'F', 'R', 'F']
        self.robot1.processor(commands)
        self.assertEqual(str(self.robot1), '1 1 E')

    def test_process_command_for_lost_bot(self):
        commands = ['F', 'R', 'R', 'F', 'L', 'L', 'F', 'F', 'R', 'R', 'F', 'L', 'L']
        self.robot2.processor(commands)
        self.assertEqual(str(self.robot2), '3 3 N LOST')

    def test_process_command_for_scent_grid_and_bot_not_lost(self):
        commands = ['F', 'R', 'R', 'F', 'L', 'L', 'F', 'F', 'R', 'R', 'F', 'L', 'L']
        self.robot2.processor(commands)
        commands =  commands + ['F', 'R']
        self.robot3.processor(commands)
        self.assertEqual(str(self.robot3), '3 3 E')
        



if __name__ == '__main__':
    unittest.main()