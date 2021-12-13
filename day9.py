from day_util import DayUtil
from functools import reduce
import heapq



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

def day9_2():
    """
    Utilize an iterative (but space-heavy) DFS and a heapq() to store length and keep track of top n
    lengths of basins.
    """
    input = [[int(ch) for ch in row] for row in DayUtil().open_file("day9")]
    visited = [[False for ch in row] for row in input]
    
    all_basins = []
    basin, stack = [], []

    for row in range(len(input)):
        for col in range(len(input[0])):
            stack.append((row,col))
            while stack:
                y,x = stack.pop()
                if visited[y][x] is False and input[y][x] != 9:
                    basin.append((y,x))
                    visited[y][x] = True
                    if input[y][x] == 9:
                        visited[y][x] = True
                for yy,xx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
                    if 0 <= yy < len(input) and 0 <= xx < len(input[0]):
                        if visited[yy][xx] is False and input[yy][xx] != 9:
                            stack.append((yy,xx))
            heapq.heappush(all_basins,len(basin))
            basin = []
    return reduce(lambda a,b: a*b, heapq.nlargest(3,all_basins))

#day9()
print(day9_2())

"""
Could be a disjoint graph find/union problem.
Instead of a list, use a dict for quicker lookup.
NOTE: per requirements --> all other locations will always be part of only one basin.
    So there will not be any "true peaks" within an area.

parents = {}

def find(node):
    if node not in parents:
        parents[node] = node
        return node
    if parents[node] == node:
        return node
    else:
        return parents[node]
    return find(parents[node])

def union(fr, to):
    parent_a = find(fr)
    parent_b = find(to)
    if parent_a == parent_a or parent_b == parent_b:
        if parent_a == parent_a:
            parents[parent_b] = parent_a
        else:
            parents[parent_a] = parent_b
    else:
        parents[parent_b] = parent_a
    return
"""

