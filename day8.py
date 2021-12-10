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

def process_input(line):
    configs,output = line.split("|")
    return [[st for st in configs.split()],[st for st in output.split()]]

"""
my key:
     a      --
    b c    |  | 
     d      --
    e f    |  |
     g      --

mappings:
    -a: xor of 1 and 7
    -e: xor of 8 and 9
    -d: xor of 8 and 0
    -c: xor of 5 and 9
    -g: only unmapped key of 2
    -f: only unmapped key of 3
    -b: remaining unmapped key

"""
from collections import Counter

def day8_2():
    input = DayUtil().open_file("day8")
    #input = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

    main_total = 0

    for line in input:
        mapping = Counter()
        config,output = process_input(line)

        config.sort(key=lambda con: len(con))

        mapping[8] = Counter(config[-1])
        mapping[1] = Counter(config[0])
        mapping[7] = Counter(config[1])
        mapping[4] = Counter(config[2])

        for i, conf in enumerate(config):
            tmp = Counter(conf)
            if len(conf) == 5:
                if len(tmp & mapping[4]) == 2:
                    mapping[2] = tmp
                elif len(tmp & mapping[1]) == 2:
                    mapping[3] = tmp
                else:
                    mapping[5] = tmp
            elif len(conf) == 6:
                if len(tmp & mapping[5]) == 4:
                    mapping[0] = tmp
                elif len(tmp & mapping[3]) == 5:
                    mapping[9] = tmp
                else:
                    mapping[6] = tmp
        
        total = 0
        for letter in output:
            for m in mapping:
                if Counter(letter) == mapping[m]:
                    total *= 10
                    total += m
        main_total += total
    return main_total

#print(day8())
print(day8_2())