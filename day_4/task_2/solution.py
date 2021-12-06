class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

        self.numbers = [int(n) for n in task_input[0].split(",")]
        board_array = self.task_input[2:]
        self.boards = [Board(board_array[i+(i*5):(i*5) + i+5]) for i in range(len(board_array)//6)]

    def solve(self):
        for number in self.numbers:
            for board in self.boards:
                board.mark(number)

                if board.won():
                    unmarked_numbers = board.get_unmarked_numbers()
                    return sum(unmarked_numbers) * number


class Board:
    def __init__(self, board_input):
        self.board = []
        for row in board_input:
            number_row = [int(x) for x in row.replace("  ", " ").split(" ")]
            self.board.append(number_row)

    def mark(self, number):
        for i in range(5):
            for j in range(5):
                if number == self.board[i][j]:
                    self.board[i][j] = "x"

    def won(self):
        row, column = [], []
        for i in range(5):
            for j in range(5):
                row.append(self.board[i][j])
                column.append(self.board[j][i])
            if row.count("x") == 5 or column.count("x") == 5:
                return True
            row, column = [], []
        return False

    def get_unmarked_numbers(self):
        numbers = []
        for row in self.board:
            for number in row:
                if number != "x":
                    numbers.append(number)
        return numbers
