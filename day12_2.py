from day_util import DayUtil
from collections import defaultdict

def populate_graph():
    graph = defaultdict(list)
    data = DayUtil().open_file("day12")
    for line in data:
        fr, to = line.split("-")
        graph[fr].append(to)
        if fr not in ("start","START"):
            graph[to].append(fr)
    return graph    

def day12():
    """Find all paths graph algo with a twist"""
    graph = populate_graph()
    paths = []
    stack = [["start"]]
    while stack:
        path = stack.pop()
        if path[-1] == "end":
            paths.append(path)
        else:
            for node in graph[path[-1]]:
                if node in ("start","START"):
                    continue
                if node == "end" or node.upper() == node:
                    stack.append(path + [node])
                else:
                    if path[0] == "start":
                        new_path = path + [node]
                        if new_path.count(node) == 2:
                            new_path[0] = "START"
                        stack.append(new_path)
                    else:
                        if path.count(node) < 1:
                            stack.append(path+[node])
    return len(paths)

print(day12())