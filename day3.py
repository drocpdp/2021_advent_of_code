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




"""
- life support rating = oxygen generator rating * CO2 scrubber rating
- left to right: 2 buckets: 
        all numbers with that bit most common
            tie, keep 1
        all numbers with that bit least common
            tie, keep 0

-first pass, divide buckets by first bit. Then iterate through each bucket 
    with index 1 to end.
-still will be O(n) (technically O(xn) with x being number of digits) but complexity 
    does not increase with number of input.
    -if we factor that numbers could increase in value, then we can say it will be
        O(xy) with x being # sig. digits, y being number of qty of input
-instead of iterating i for each sig. digit, let's keep a max value. If 
"""


def day3_b():
    input = DayUtil.open_file('day3')

    # find out set bit for each position
    bucket = [0]*len(input[0])
    for num in input:
        for i, ch in enumerate(num):
            if ch == '1':
                bucket[i] += 1
    mask_key = [1 if num >= len(input) // 2 else 0 for num in bucket]
    mask = 0
    for digit in mask_key:
        mask *= 2
        mask += digit
    print(mask_key)
    
    life_support_max, oxygen_gen_max = 0, 0
    life_support_num, oxygen_gen_num = 0, 0
    
    for num in input:
        curr_total = 0
        for i in range(len(num)):
            if int(num[i]) == mask_key[i]:
                curr_total *= 2
                curr_total += int(num[i])
            else:
                if curr_total > life_support_max:
                    life_support_num = num
                break

    for num in input:
        curr_total = 0
        for i in range(len(num)):
            if int(num[i]) != mask_key[i]:
                curr_total *= 2
                curr_total += int(num[i])
            else:
                if curr_total > oxygen_gen_max:
                    oxygen_gen_num = num
                break            

    print(life_support_num)
    print(oxygen_gen_num)

    int_life_support = 0
    for char in life_support_num:
        int_life_support *= 2
        int_life_support += int(char)
    print(int_life_support)

    int_oxygen_num = 0
    for char in oxygen_gen_num:
        int_oxygen_num *= 2
        int_oxygen_num += int(char)
    print(int_oxygen_num)    

    print(int_life_support * int_oxygen_num)







#print(day3_a())
print(day3_b())

