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

def transposed_data(rrow, ccol, data):
    root_row = rrow % len(data)
    root_col = ccol % len(data[0])
    root_value = data[root_row][root_col]
    multiplier = (rrow // len(data)) + (ccol // len(data[0]))
    new_value = (root_value + multiplier)
    if new_value > 9:
        new_value = new_value % 10 + (new_value // 10)
    return new_value



def day15_2():
    data = get_data()
    height = len(data) * 5
    length = len(data[0]) * 5

    djikstra = [[float('inf') for col in range(length)] for row in range(height)]
    djikstra[0][0] = 0

    for row in range(height):
        for col in range(length):
            for rrow, ccol in ((row,col+1), (row+1, col)):
                if rrow < height and ccol < length:
                    djikstra[rrow][ccol] = min(
                        djikstra[row][col] + transposed_data(rrow, ccol, data),
                        djikstra[rrow][ccol]
                        )
    return djikstra[-1][-2]

#print(day15())
print(day15_2())