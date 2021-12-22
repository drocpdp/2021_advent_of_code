from day_util import DayUtil

def get_data():
    data = DayUtil().open_file("day15_test")
    return [[int(col) for col in row] for row in data]


def day15():
    data = get_data()
    visited = [[False for col in row] for row in data]
    min_sum = float("inf")

    def backtrack(row, col, curr_sum):
        nonlocal min_sum
        curr_sum += data[row][col]
        if row == (len(data) - 1) and col == (len(data[0]) - 1):
            min_sum = min(min_sum, curr_sum)
            return
        for rrow, ccol in ((row-1,col),(row+1,col),(row,col-1),(row,col+1)):
            if 0 <= rrow < len(data) and 0 <= ccol < len(data[0]) and visited[rrow][ccol] is False:
                    visited[rrow][ccol] = True
                    backtrack(rrow,ccol, curr_sum)
                    visited[rrow][ccol] = False
        return

    backtrack(0,0,0)
    return min_sum


print(day15())