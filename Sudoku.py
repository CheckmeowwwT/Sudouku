import random


def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)).replace('0', '.'))


def is_safe(grid, size, row, col, num):
    for x in range(size):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    startRow = row - row % (3 if size == 9 else 2)
    startCol = col - col % (3 if size == 9 else 3)
    for i in range(3 if size == 9 else 2):
        for j in range(3 if size == 9 else 3):
            if grid[i + startRow][j + startCol] == num:
                return False

    return True


def solve_sudoku(grid, size):
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 0:
                for num in range(1, size + 1):
                    if is_safe(grid, size, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid, size):
                            return True
                        grid[row][col] = 0
                return False
    return True


def generate_sudoku(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for _ in range(size):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        num = random.randint(1, size)
        while not is_safe(grid, size, row, col, num) or grid[row][col] != 0:
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
            num = random.randint(1, size)
        grid[row][col] = num
    return grid


def remove_numbers(grid, size, level):
    puzzle = [row[:] for row in grid]
    if level == 'easy':
        remove_count = size * 2
    elif level == 'medium':
        remove_count = size * 3
    elif level == 'hard':
        remove_count = size * 5
    else:
        remove_count = size * 2

    while remove_count > 0:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        puzzle[row][col] = 0
        remove_count -= 1

    return puzzle


size = int(input("Enter the size of Sudoku (6 or 9): "))
difficulty = input("Enter the difficulty level (easy, medium, hard): ")

solved_grid = generate_sudoku(size)
if solve_sudoku(solved_grid, size):
    puzzle = remove_numbers(solved_grid, size, difficulty)
    print("\nSudoku Puzzle:")
    print_grid(puzzle)
    if input("\nEnter 1 to see the solution: ") == '1':
        print("\nSudoku Solution:")
        print_grid(solved_grid)
else:
    print("Failed to generate a Sudoku puzzle.")
