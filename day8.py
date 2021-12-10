from day_util import DayUtil


def day8():
    input = DayUtil().open_file("day8")
    total = 0
    for line in input:
        output = line.split("|")[1].split()
        for string in output:
            if len(string) in (2,3,4,7):
                total += 1
    return total


print(day8())