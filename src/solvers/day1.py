import math
from itertools import combinations

from solvers.solver import Solver


class Day1(Solver):
    match = 2020

    def find_faulty_entries(self, data, times):
        numbers = [int(i) for i in data]
        for combo in combinations(numbers, times):
            if sum(combo) == self.match:
                return math.prod(combo)
        return ValueError("Could not find a match")

    def solve_part_1(self, data):
        return self.find_faulty_entries(data, 2)

    def solve_part_2(self, data):
        return self.find_faulty_entries(data, 3)


def solve(data):
    Day1().solve(data)
