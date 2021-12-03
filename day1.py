def day1():
    fp = open('./day1.txt', 'r')
    measures = [int(l) for l in fp.readlines()]
    fp.close()

    prev = None
    increases = 0
    for m in measures:
        if not prev:
            prev = m
        else:
            if m > prev:
                increases += 1
            prev = m
    return increases

def day1_2():
    fp = open('./day1.txt', 'r')
    measures = [int(l) for l in fp.readlines()]
    fp.close()

    increases = 0
    total = sum(measures[0:2])
    L, R = 0, 2
    while R + 1 < len(measures):
        new_total = total + measures[R+1]
        new_total -= measures[R-2]
        if new_total > total:
            increases += 1
        R += 1
    return increases

print(day1_2())