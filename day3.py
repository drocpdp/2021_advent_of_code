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
    input = DayUtil.open_file('day3')
    #input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    
    oxygen_input = input[:]
    zeroes, ones = [], []
    bit_position = 0
    while len(oxygen_input) > 1:
        for reading in oxygen_input:
            if reading[bit_position] == '0':
                zeroes.append(reading)
            else:
                ones.append(reading)
        oxygen_input = ones[:] if len(ones) >= len(zeroes) else zeroes[:]
        bit_position += 1
        zeroes, ones = [], []
    print(oxygen_input)

    co2_input = input[:]
    zeroes, ones = [], []
    bit_position = 0
    while len(co2_input) > 1:
        for reading in co2_input:
            if reading[bit_position] == '0':
                zeroes.append(reading)
            else:
                ones.append(reading)
        co2_input = zeroes[:] if len(zeroes) <= len(ones) else ones[:]
        bit_position += 1
        zeroes, ones = [], []
    print(co2_input)    

    oxygen = 0
    for digit in oxygen_input[0]:
        oxygen *= 2
        oxygen += int(digit)
    print(oxygen)

    co2 = 0
    for digit in co2_input[0]:
        co2 *= 2
        co2 += int(digit)
    print(co2)

    print(oxygen * co2)
print(day3_b())




