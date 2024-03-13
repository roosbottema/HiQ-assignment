import unittest
from robot import Robot

class TestRobot(unittest.TestCase):
    def test_place(self):
        robot = Robot()
        robot.place(-1, 0, "NORTH")
        self.assertEqual(robot.x, None, "Should be None")

    def test_lower_y_limit(self):
        robot = Robot()
        robot.place(0,0,"SOUTH")
        robot.move()
        self.assertEqual(robot.y, 0, "Should be 0")

    def test_upper_y_limit(self):
        robot = Robot()
        robot.place(0, 5, "NORTH")
        robot.move()
        self.assertEqual(robot.y, 5, "Should be 5")

    def test_lower_x_limit(self):
        robot = Robot()
        robot.place(0,0,"WEST")
        robot.move()
        self.assertEqual(robot.x, 0, "Should be 0")

    def test_upper_x_limit(self):
        robot = Robot()
        robot.place(5, 0, "EAST")
        robot.move()
        self.assertEqual(robot.x, 5, "Should be 5")

    def test_move(self):
        robot = Robot()
        robot.place(1,2, "NORTH")
        robot.move()
        self.assertEqual(robot.y, 3, "Should be 3")

    def test_ignore_move(self):
        robot = Robot()
        robot.move()
        self.assertEqual(robot.x, None, "Should be None")

    def test_left(self):
        robot = Robot()
        robot.place(3,2,"NORTH")
        robot.left()
        self.assertEqual(robot.f, "WEST", "Should be WEST")

    def test_ignore_left(self):
        robot = Robot()
        robot.left()
        self.assertEqual(robot.f, None, "Should be None")

    def test_right(self):
        robot = Robot()
        robot.place(3, 3, "WEST")
        robot.right()
        self.assertEqual(robot.f, "NORTH", "Shoudl be NORTH")

    def test_ignore_right(self):
        robot = Robot()
        robot.right()
        self.assertEqual(robot.f, None, "Should be None")

if __name__ == "__main__":
    unittest.main()