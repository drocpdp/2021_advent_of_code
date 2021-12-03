def day2_a():
    fp = open('./day2.txt', 'r')
    measures = [l.split() for l in fp.readlines()]
    fp.close()   

    fwd = dwn = 0

    for direction, qty in measures:
        if direction == "down":
            dwn += int(qty)
        elif direction == "up":
            dwn -= int(qty)
        else:
            fwd += int(qty)
    return fwd*dwn



def day2():
    fp = open('./day2.txt', 'r')
    measures = [l.split() for l in fp.readlines()]
    fp.close()   

    fwd = dwn = aim = 0

    for direction, qty in measures:
        qty = int(qty)
        if direction == "down":
            aim -= qty
        elif direction == "up":
            aim += qty
        else:
            fwd += qty
            dwn += aim*qty
    return fwd*dwn

print(day2())