from day_util import DayUtil


def day9():
    input = [[int(ch) for ch in row] for row in DayUtil().open_file("day9")]
    low_points = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            is_lower = True
            for rrow,ccol in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)):
                if 0 <= rrow < len(input) and 0 <= ccol < len(input[0]):
                    if input[rrow][ccol] <= input[row][col]:
                        is_lower = False
            if is_lower:
                low_points += input[row][col] + 1
    print(low_points)



day9()