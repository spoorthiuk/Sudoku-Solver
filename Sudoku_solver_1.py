#Sudoku is one of the most popular logic based game. Here is an
#algorithm designed to solve any valid sudoku grid based on backtracking.
#However, it takes a significant amount of time to solve when there are a
#large number of blank spaces in the grid.
class SudokuSolver:
    def __init__(self, grid):
        self.board = grid

    def solve_puzzle(self):
        self.print_board()
        print('******************')
        self.solve()
        self.print_board()

    def print_board(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if (j + 1) % 3 == 0 and j != 8:
                    print(self.board[i][j], '\b|', end='')
                elif j != 8:
                    print(self.board[i][j], '\b,', end='')
                else:
                    print(self.board[i][j], end='')
            print()
            if (i + 1) % 3 == 0 and i != 8:
                print('------------------')

    def find_empty_spaces(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] == 0:
                    return i, j
        return False

    def is_valid(self, n, row, col):
        # check row
        for i in range(0, 9):
            if n == self.board[row][i] and i != col:
                return False
        # check column
        for i in range(0, 9):
            if n == self.board[i][col] and i != row:
                return False
        # check subgrid
        for i in range((row // 3) * 3, (row // 3) * 3 + 3):
            for j in range((col // 3) * 3, (col // 3) * 3 + 3):
                if (self.board[i][j] == n) and i != row and j != col:
                    return False
        return True

    def solve(self):
        empty_pos = self.find_empty_spaces()
        if not empty_pos:
            return True
        else:
            (row, col) = empty_pos
        for i in range(1, 10):
            if self.is_valid(i, row, col):
                board[row][col] = i
                if self.solve():
                    return True
                board[row][col] = 0
        return False


#Hardcoded grid description where 0 denotes blank spaces
board = [[0, 0, 0, 8, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 3, 0],
         [5, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 7, 0, 8, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 2, 0, 0, 3, 0, 0, 0, 0],
         [6, 0, 0, 0, 0, 0, 0, 7, 5],
         [0, 0, 3, 4, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 6, 0, 0]]

Game = SudokuSolver(board)
Game.solve_puzzle()
