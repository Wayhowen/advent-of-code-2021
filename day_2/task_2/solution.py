class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

    def solve(self):
        commands = [command.split() for command in self.task_input]
        output = self.find_depth_and_position(commands)
        return output

    def find_depth_and_position(self, commands):
        depth = 0
        position = 0
        aim = 0
        for command, number in commands:
            number = int(number)
            if command == "forward":
                position += number
                depth += aim * number
            elif command == "down":
                aim += number
            elif command == "up":
                aim -= number
        return depth * position
