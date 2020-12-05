import unittest
from itertools import starmap

from solvers.day2 import Day2, parse_password_policy, is_valid_first_password_policy


class TestDay1(unittest.TestCase):
    data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    day2 = Day2()

    def test_parse_password_policy(self):
        expected_solution = [(1, 3, 'a', 'abcde'), (1, 3, 'b', 'cdefg'), (2, 9, 'c', 'ccccccccc')]
        solution = list(map(parse_password_policy, self.data))
        self.assertEqual(expected_solution, solution)

    def test_is_valid_first_password_policy(self):
        parsed_data = [(1, 3, 'a', 'abcde'), (1, 3, 'b', 'cdefg'), (2, 9, 'c', 'ccccccccc')]
        expected_solution = [True, False, True]
        solution = list(starmap(is_valid_first_password_policy, parsed_data))
        self.assertEqual(expected_solution, solution)

    def test_solve_part_1(self):
        expected_solution = 2
        solution = self.day2.solve_part_1(self.data)
        self.assertEqual(expected_solution, solution)

    def test_solve_part_2(self):
        expected_solution = 1
        solution = self.day2.solve_part_2(self.data)
        self.assertEqual(expected_solution, solution)
