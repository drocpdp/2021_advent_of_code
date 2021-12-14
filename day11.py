from day_util import DayUtil

def day11():
    grid = [[int(pt) for pt in line] for line in DayUtil().open_file("day11")]
    total_zeros = 0
    for day in range(100):
        zeros_remain = increment(grid)
        total_zeros += len(zeros_remain)
        while zeros_remain:
            row,col = zeros_remain.pop()
            more_zeros = zero(row,col,grid)
            total_zeros += len(more_zeros)
            zeros_remain.extend(more_zeros)
    return total_zeros


def increment(grid):
    zeros = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] = (grid[row][col] + 1) % 10
            if grid[row][col] == 0:
                zeros.append((row,col))
    return zeros

def zero(row, col, grid):
    new_zeros = []
    for rrow, ccol in ((row-1,col-1),(row-1,col),(row-1,col+1),(row,col+1),(row+1,col+1),(row+1,col),(row+1,col-1),(row,col-1)):
        if 0 <= rrow < len(grid) and 0 <= ccol < len(grid[0]):
            if grid[rrow][ccol] != 0:
                grid[rrow][ccol] = (grid[rrow][ccol] + 1) % 10
                if grid[rrow][ccol] == 0:
                    new_zeros.append((rrow,ccol))
    return new_zeros



print(day11())