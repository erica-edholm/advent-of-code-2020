import abc


class Solver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def solve_part_1(self, data):
        return "Solution for part 1 not implemented yet"

    @abc.abstractmethod
    def solve_part_2(self, data):
        return "Solution for part 2 not implemented yet"

    def solve(self, data):
        solver_name = self.__class__.__name__
        print('Solution for {0}:'.format(solver_name))
        print('Star 1: {0}'.format(self.solve_part_1(data)))
        print('Star 2: {0}'.format(self.solve_part_2(data)))
