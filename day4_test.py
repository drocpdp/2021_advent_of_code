
from day4 import day4_1, day4_2
from day_util import DayUtil

picks = [79,9,13,43,53,51,40,47,56,27,0,14,33,60,61,36,72,48,83,42,10,86,41,75,16,80,15,93,95,45,68,96,84,11,85,63,18,31,35,74,71,91,39,88,55,6,21,12,58,29,69,37,44,98,89,78,17,64,59,76,54,30,65,82,28,50,32,77,66,24,1,70,92,23,8,49,38,73,94,26,22,34,97,25,87,19,57,7,2,3,46,67,90,62,20,5,52,99,81,4]
#picks = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
def _create_boards():
    """Create a list of 5x5 matrices"""
    boards = []
    boards_raw = DayUtil.open_file("boards")
    board = []
    count = 0
    for row in boards_raw:
        if row != "":
            board.append([int(nm) for nm in row.split()])
            count += 1
            if count % 5 == 0:
                boards.append(board)
                board = []
    return boards


#print(day4_1(_create_boards(), picks))
print(day4_2(_create_boards(), picks))
