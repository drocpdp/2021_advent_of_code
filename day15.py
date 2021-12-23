from day_util import DayUtil
from collections import deque

def get_data():
    data = DayUtil().open_file("day15")
    return [[int(col) for col in row] for row in data]


def day15():
    # If using BFS, len of deque gets too long. Switching to more of a DP solution
    data = get_data()
    djikstra = [[float('inf') for col in row] for row in data]
    djikstra[0][0] = 0

    for row in range(len(djikstra)):
        for col in range(len(djikstra[0])):
            for rrow, ccol in ((row,col+1), (row+1, col)):
                if rrow < len(data) and ccol < len(data[0]):
                    djikstra[rrow][ccol] = min(djikstra[row][col] + data[rrow][ccol], djikstra[rrow][ccol])
    return djikstra[-1][-1]


print(day15())