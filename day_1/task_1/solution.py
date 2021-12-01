class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

    def solve(self):
        depths = [int(num) for num in self.task_input]
        output = self.find_increases(depths)
        return output

    def find_increases(self, depths):
        last_depth = None
        increases = 0
        for iteration, depth in enumerate(depths):
            if last_depth and depth > last_depth:
                increases += 1
            last_depth = depth
        return increases
