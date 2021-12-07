from collections import defaultdict


class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

        self.positions = [int(x) for x in self.task_input[0].split(",")]

    def solve(self):
        align_positions = defaultdict(lambda: 0)

        for position in range(min(self.positions), max(self.positions)):
            for current_position in self.positions:
                align_positions[position] += abs(position - current_position)
        return min(align_positions.values())
