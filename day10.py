from day_util import DayUtil

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

print(day10())