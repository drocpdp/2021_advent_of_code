from day_util import DayUtil
from functools import reduce

def day10():
    lines = DayUtil().open_file("day10")
    stack = []
    total = 0
    key = {
            "(" : ")",
            "{" : "}", 
            "[" : "]",
            "<" : ">"
    }
    score = {
            ")":3,
            "]":57,
            "}":1197,
            ">":25137
    }
    for line in lines:
        for ch in line:
            if ch in key:
                stack.append(ch)
            else:
                if key[stack[-1]] != ch:
                    total += score[ch]
                    break
                else:
                    stack.pop()
    return total

def day10_2():
    lines = DayUtil().open_file("day10")
    key = {
            "(" : ")",
            "{" : "}", 
            "[" : "]",
            "<" : ">"
    }
    score = {
            ")" : 1,
            "]" : 2,
            "}" : 3,
            ">" : 4
    }

    totals = []

    for line in lines:
        stack = []
        valid = True
        for ch in line:
            if ch in key:
                stack.append(ch)
            else:
                if key[stack[-1]] != ch:
                    valid = False
                    break
                else:
                    stack.pop()
        total = 0
        if valid:
            while stack:
                total = (total * 5) + score[key[stack.pop()]]
            totals.append(total)
    totals.sort()
    return totals[len(totals) // 2]

#print(day10())
print(day10_2())