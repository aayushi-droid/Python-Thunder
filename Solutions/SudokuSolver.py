grid = [
    [6, 5, 0, 8, 7, 3, 0, 9, 0],
    [0, 0, 3, 2, 5, 0, 0, 0, 8],
    [9, 8, 0, 1, 0, 4, 3, 5, 7],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 5, 0, 3],
    [5, 7, 8, 3, 0, 1, 0, 2, 6],
    [2, 0, 0, 0, 4, 8, 9, 0, 0],
    [0, 9, 0, 6, 2, 5, 0, 8, 1],
]
K = len(grid)


def print_sudoku():
    # Print Sudoku
    for i in range(K):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(K):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(grid[i][j], end=" ")


def missing_num(row, col):
    flag = 0
    for i in range(K):
        for j in range(K):
            # cell is unassigned
            if grid[i][j] == 0:
                row = i
                col = j
                flag = 1
                a = [row, col, flag]
                return a
    a = [-1, -1, flag]

    return a


# print(missing_num(0,0))


def is_safe(n, r, c):
    # row
    for i in range(K):
        if grid[r][i] == n:
            return False

    # column
    for i in range(K):
        if grid[i][c] == n:
            return False

    row_start = (r // 3) * 3
    col_start = (c // 3) * 3
    # checking submatrix
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if grid[i][j] == n:
                return False
    return True


def solver():
    row = 0
    col = 0
    a = missing_num(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    # number between 1 to 9
    for i in range(1, K + 1):
        if is_safe(i, row, col):
            grid[row][col] = i
            if solver():
                return True
            grid[row][col] = 0
    return False


if solver():
    print_sudoku()
else:
    print("Check Your Sudoku")
