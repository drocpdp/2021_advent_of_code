from day_util import DayUtil
from collections import defaultdict

def populate_graph():
    graph = defaultdict(list)
    data = DayUtil().open_file("day12")
    for line in data:
        fr, to = line.split("-")
        graph[fr].append(to)
        if fr != "start":
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
                if node.upper() == node or (node.lower() == node and node not in path):
                    new_path = path + [node]
                    stack.append(new_path)
    return len(paths)

print(day12())