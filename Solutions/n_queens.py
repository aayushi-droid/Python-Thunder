# This is the solution to the famous n - queen problem.

# This is solved using recursion and backtracking.


# This is the main function which test queen at each possible position in the grid,
# and return whether the queen is safe or not.
def quuen_pos(arr, n):
    if sum(sum(a) for a in arr) == n:
        print('answer')
        printGrid(arr)

    # we loop through each possible location in the grid
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                if queen_safe(arr, i, j, n):
                    arr[i][j] = 1
                    quuen_pos(arr, n)

                    # backtracking step, making the cell available for checking again.
                    arr[i][j] = 0

    return False



# this is a helper function which tells wheteher the quuen is safe at given position
# or not.

def queen_safe(arr, row, col, n):

    # checking for the queen is same row.
    for i in range(n):
        if arr[i][col] == 1:
            return False

    # checking for queen is same column.
    for j in range(n):
        if arr[row][j] == 1:
            return False

    # checking for queen diagonally.
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                if abs(i - row) == abs(j - col):
                    return False



    return True


# this is the function to form grid, i.e. the arrangement of queens in the grid.

def form_grid(puzzle_string, grid):
    print('The Sudoku Problem')
    for i in range(0, len(puzzle_string), 4):
        row = puzzle_string[i:i + 4]
        temp = []
        for block in row:
            temp.append(int(block))
        grid.append(temp)
    printGrid(grid)

# function to print thr grid.

def printGrid(grid):
    for row in grid:
        print(row)

# setting every position to 0, i.e. all the positions are available.
initial_pos = '0000000000000000'
n = 4
grid = []
form_grid(initial_pos, grid)

quuen_pos(grid, n)
print('Safe queen position:')


# this code is contributed by Kaushalendra pandey.