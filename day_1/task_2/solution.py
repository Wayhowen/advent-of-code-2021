class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

    def solve(self):
        depths = [int(num) for num in self.task_input]
        output = self.find_increases_in_sliding_windows(depths)
        return output

    def find_increases_in_sliding_windows(self, depths):
        iteration = 0
        last_sliding_window = 0
        increases = 0
        while iteration < len(depths) - 2:
            sliding_window = depths[iteration] + depths[iteration + 1] + depths[iteration + 2]
            if last_sliding_window and sliding_window > last_sliding_window:
                increases += 1
            last_sliding_window = sliding_window
            iteration += 1
        return increases
