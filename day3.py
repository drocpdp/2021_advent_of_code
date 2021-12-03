from day_util import DayUtil


def day3_a():
    input = DayUtil.open_file("day3")
    max_len = len(max(input, key = len))
    bucket = [0]*max_len
    for num in input:
        for i, ch in enumerate(num):
            if ch == '1':
                bucket[i] += 1
    # actually want epsilon rate here so we can iterate this to apply shift
    bucket = [0 if b > len(input) // 2 else 1 for b in bucket]
    epsilon_rate = 0 #less common
    for b in range(len(bucket)):
        epsilon_rate *= 2
        epsilon_rate += bucket[b]

    inverse_mask = 2**len(bucket)-1
    gamma_rate = inverse_mask ^ epsilon_rate

    # now iterate epsilon rate and apply binary shift at each 1 to gamma rate to get total
    total = 0
    for i in range(len(bucket)):
        if bucket[i] == 1:
            shift = len(bucket) - i - 1
            total = total + (gamma_rate << shift)
    return total






def day3_b():
    fp = open('./day3.txt', 'r')
    measures = [l.split() for l in fp.readlines()]
    fp.close()   

print(day3_a())
