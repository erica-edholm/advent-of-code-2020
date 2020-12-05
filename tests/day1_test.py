import unittest

from solvers.day1 import Day1


class TestDay1(unittest.TestCase):

    data = [1721, 979, 366, 299, 675, 1456]
    day1 = Day1()

    def test_solve_part_1(self):
        expected_solution = 514579
        solution = self.day1.solve_part_1(self.data)
        self.assertEqual(expected_solution, solution)

    def test_solve_part_2(self):
        expected_solution = 241861950
        solution = self.day1.solve_part_2(self.data)
        self.assertEqual(expected_solution, solution)
