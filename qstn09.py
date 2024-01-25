def isValidSudoku(board):
    # Check each row
    for row in board:
        if not isValidSet(row):
            return False
    
    # Check each column
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not isValidSet(column):
            return False
    
    # Check each 3x3 subgrid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not isValidSet(subgrid):
                return False
    
    return True
def isValidSet(nums):
    seen = set()
    for num in nums:
        if num != ".":
            if num in seen:
                return False
            seen.add(num)
    return True

# Example usage with the provided Sudoku board
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))