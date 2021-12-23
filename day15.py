from day_util import DayUtil
from collections import deque

def get_data():
    data = DayUtil().open_file("day15_test")
    return [[int(col) for col in row] for row in data]


def day15():
    # djikstra algo
    # first with DFS, then with priority queue if suboptimal
    data = get_data()
    visited = [[False for col in row] for row in data]
    djikstra = [[float('inf') for col in row] for row in data]
    djikstra[0][0] = 0
    dq = deque([(0,0)])
    visited[0][0] = True
    while dq:
        y,x = dq.popleft()
        visited[y][x] = True
        for yy,xx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
            if 0 <= yy < len(djikstra) and 0 <= xx < len(djikstra[0]) and visited[yy][xx] is False:
                djikstra[yy][xx] = min(djikstra[y][x] + data[yy][xx], djikstra[yy][xx])
                dq.append([yy,xx])
    return djikstra[-1][-1]

print(day15())