from abc import ABC
from itertools import starmap

from solvers.solver import Solver


def parse_password_policy(password_policy):
    occurrence, chars = password_policy.split(" ", 1)
    int1, int2 = occurrence.split("-", 1)
    char, password = chars.split(": ", 1)
    return int(int1), int(int2), char, password


def is_valid_first_password_policy(int1, int2, char, password):
    return int1 <= password.count(char) <= int2


def is_valid_second_password_policy(int1, int2, char, password):
    return (password[int1-1] == char) ^ (password[int2-1] == char)


class Day2(Solver, ABC):

    def solve_part_1(self, data):
        parsed_data = map(parse_password_policy, data)
        is_valid_password = list(starmap(is_valid_first_password_policy, parsed_data))
        return is_valid_password.count(True)

    def solve_part_2(self, data):
        parsed_data = map(parse_password_policy, data)
        is_valid_password = list(starmap(is_valid_second_password_policy, parsed_data))
        return is_valid_password.count(True)


def solve(data):
    Day2().solve(data)
