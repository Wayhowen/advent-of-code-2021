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
        for command, number in commands:
            number = int(number)
            if command == "forward":
                position += number
            elif command == "down":
                depth += number
            elif command == "up":
                depth -= number
        return depth * position
