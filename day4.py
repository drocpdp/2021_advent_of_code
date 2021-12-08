# run using day4_test.py (main())

"""
NOTES:
    -idea. If number selected, change to negative

BRUTE FORCE:
    -for each number selected:
        -for each board
            -traverse row by row, column ([row][col]) by column
                -if number there, check horizontal and vertically.
                    -if all numbers in row or column found, declare winner
dict to locate board? 
each number, which board?
"""
from collections import defaultdict

def day4_1(boards, picks):
    where = defaultdict(list)

    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                where[col].append((b,r,c))

    for pick in picks:
        for board,row,col in where[pick]:
            boards[board][row][col] *= -1
            if sum([True for val in boards[board][row] if val < 0]) == 5 or \
                sum([True for val in [boards[board][rrow][col] for rrow in range(5)] if val < 0]) \
                    == len(boards[board][row]):
                unmarked = 0
                for row in boards[board]:
                    for col in row:
                        if col >= 0:
                            unmarked += col
                return unmarked * pick
    return