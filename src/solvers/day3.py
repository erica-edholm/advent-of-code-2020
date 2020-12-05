from abc import ABC
from itertools import starmap

from solvers.solver import Solver


def predict_slope(forest, x_slope, y_slope):
    x = 0
    y = 0
    hit_trees = 0
    map_length = len(forest)
    map_width = len(forest[0])
    while y < map_length:
        hit_trees += forest[y][x % map_width] == "#"
        x += x_slope
        y += y_slope
    return hit_trees


class Day3(Solver, ABC):

    def solve_part_1(self, data):
        return predict_slope(data, 3, 1)

    def solve_part_2(self, data):
        first = predict_slope(data, 1, 1)
        second = predict_slope(data, 3, 1)
        third = predict_slope(data, 5, 1)
        forth = predict_slope(data, 7, 1)
        fifth = predict_slope(data, 1, 2)
        return first * second * third * forth * fifth


def solve(data):
    Day3().solve(data)
