from day_util import DayUtil
from collections import Counter

def extract_data():
    data = [int(d) for d in DayUtil().open_file("day7")[0].split(',')]
    #data = [16,1,2,0,4,2,7,1,2,14] # test data
    return data

def get_val_for_alignment_position(align_idx, data):
    total = 0
    for item in data:
        total += abs(align_idx - item) * (data[item])
    return total

def get_val(align_idx, data):
    total = 0
    for item in data:
        n = abs(align_idx - item)
        n_n = n * (n+1) // 2
        total += n_n * (data[item])
    return total

def day7():
    data = Counter(extract_data())
    min_value = float('inf')
    for i in range(max(data)):
        min_value = min(get_val(i, data), min_value)
    print(min_value)

day7() #