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


print(day1())