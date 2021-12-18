from day_util import DayUtil
from collections import Counter

def get_data():
    data = DayUtil().open_file("day14")
    initial = data[0]
    template = {fr.strip():to.strip() for (fr,to) in [data[i].split("->") for i in range(2, len(data))]}
    return (initial,template)

def day14():
    polymer, template = get_data()
    polymer = [p for p in polymer]
    for _ in range(10):
        pairs = ["".join(pair) for pair in zip(polymer[0::1], polymer[1::1])]
        
        insertions = [template["".join(pair)] for pair in pairs]
        
        new_polymer = [None]*(len(insertions)+len(polymer))

        new_polymer[0::2], new_polymer[1::2] = polymer,insertions
        
        polymer = new_polymer

    c = Counter(polymer)
    (_, most_common) = (c.most_common(1)[0])
    (_, least_common) = (c.most_common()[:-2:-1][0])
    return most_common - least_common


print(day14())