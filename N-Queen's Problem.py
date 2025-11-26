def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    n = 4
    
    # Check same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_4queen():
    n = 4
    board = [["." for _ in range(n)] for _ in range(n)]
    
    solutions = []

    def backtrack(row):
        if row == n:
            # Convert board to readable format
            sol = [" ".join(board[r]) for r in range(n)]
            solutions.append(sol)
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'   # backtrack

    backtrack(0)
    return solutions


# MAIN
solutions = solve_4queen()

print("Total solutions for 4x4:", len(solutions))
print()

for sol in solutions:
    print("Solution:")
    for row in sol:
        print(row)
    print()
