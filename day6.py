"""
3,4,3,1,2
2,3,2,0,1,8
1,2,1,6,0,8
0,1,0,5,6,7,8



"""
from day_util import DayUtil
from collections import Counter

def extract_data():
    data = [int(d) for d in DayUtil().open_file("day6")[0].split(',')]
    return data


def day6():
    data = Counter(extract_data())
    for day in range(80):
        regenerate = data[0]
        for i in range(0, 8):
            data[i] = data[i+1]
        data[6] += regenerate
        data[8] = regenerate
    return sum(data.values())


print(day6())