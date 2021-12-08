from day_util import DayUtil

def process_input():
    raw_input = DayUtil().open_file("day5")
    lines = []
    for line in raw_input:
        fr, to = line.split("->")
        (x1,y1),(x2,y2) = fr.split(','), to.split(',')
        lines.append([int(x1),int(y1),int(x2),int(y2)])
    return lines


from collections import defaultdict
def day5():
    lines = process_input()
    intersections = defaultdict(int)
    for x1,y1,x2,y2 in lines:
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for i in range(min(y1,y2), max(y1,y2)+1):
                    intersections[(x1,i)] += 1
            elif y1 == y2:
                for i in range(min(x1,x2), max(x1,x2)+1):
                    intersections[(i,y1)] += 1
    return sum([True for i in intersections if intersections[i] > 1])


from collections import defaultdict
def day5_2():
    lines = process_input()
    intersections = defaultdict(int)
    for x1,y1,x2,y2 in lines:
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for i in range(min(y1,y2), max(y1,y2)+1):
                    intersections[(x1,i)] += 1
            elif y1 == y2:
                for i in range(min(x1,x2), max(x1,x2)+1):
                    intersections[(i,y1)] += 1
        else:
            for inc in range(0,abs(x2-x1)+1):
                xxx = x1+inc if x1 < x2 else x1-inc
                yyy = y1+inc if y1 < y2 else y1-inc
                intersections[(xxx,yyy)] += 1
    return sum([True for i in intersections if intersections[i] > 1])



#print(day5())
print(day5_2())