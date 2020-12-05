import unittest
from itertools import starmap

from solvers.day3 import Day3, predict_slope


class TestDay1(unittest.TestCase):
    data = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"]
    day3 = Day3()

    def test_predict_slope(self):
        slopes = [(self.data, 1, 1), (self.data, 3, 1), (self.data, 5, 1), (self.data, 7, 1), (self.data, 1, 2)]
        expected_solution = [2, 7, 3, 4, 2]
        solution = list(starmap(predict_slope, slopes))
        self.assertEqual(expected_solution, solution)

    def test_solve_part_1(self):
        expected_solution = 7
        solution = self.day3.solve_part_1(self.data)
        self.assertEqual(expected_solution, solution)

    def test_solve_part_2(self):
        expected_solution = 336
        solution = self.day3.solve_part_2(self.data)
        self.assertEqual(expected_solution, solution)
