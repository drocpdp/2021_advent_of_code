from day_util import DayUtil
from collections import Counter, defaultdict

class LL:
    def __init__(self, val=None):
        self.next = None
        self.val = val

def get_data():
    data = DayUtil().open_file("day14")
    initial = data[0]
    paths = {fr.strip():to.strip() for (fr,to) in [data[i].split("->") for i in range(2, len(data))]}
    return (initial,paths)

def get_pairs_map(paths):
    pairs = {}
    for path in paths:
        single = paths[path]
        pairs[path] = [path[0]+single, single+path[1]]
    return pairs

def day14():
    initial_polymer, graph = get_data()
    pairs_map = get_pairs_map(graph)
    pairs_count = Counter()
    
    [pairs_count.update([initial_polymer[i:i+2]]) for i in range(len(initial_polymer)-1)]

    for _ in range(39):
        tmp_pairs = pairs_count.copy()
        for key in tmp_pairs:
            cnt = tmp_pairs[key]
            pair1, pair2 = pairs_map[key]
            pairs_count[pair1] += cnt
            pairs_count[pair2] += cnt
            if pairs_count[key] > 0:
                pairs_count[key] -= cnt
    letters_count = defaultdict(int)

    for pair in pairs_count:
        cnt = pairs_count[pair]
        pair1, pair2 = pairs_map[pair]
        for letter in pair1:
            letters_count[letter] = letters_count[letter] + cnt
    letters_count[[initial_polymer][-1][-1]] += 1
    
    answer = max(letters_count.values()) - min(letters_count.values())
    print(answer)



day14()
