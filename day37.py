class Solution:
    def solveSudoku(self, board):
        
        def is_valid(row, col, num):
            # Check row
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():
            # Find empty cell
            for row in range(9):
                for col in range(9):

                    if board[row][col] == '.':
                        
                        # Try numbers 1 to 9
                        for num in "123456789":

                            if is_valid(row, col, num):
                                board[row][col] = num

                                # Recursively solve
                                if solve():
                                    return True

                                # Backtrack
                                board[row][col] = '.'

                        return False

            # No empty cells
            return True

        solve()