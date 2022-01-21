from day_util import DayUtil
import operator

stack = []

def get_min(operands):
    return min(operands)

def get_max(operands):
    return max(operands)

def multiply(operands):
    total = operands[0]
    for i in range(1, len(operands)):
        total *= operands[i]
    return total

def adding(operands):
    total = operands[0]
    for i in range(1, len(operands)):
        total += operands[i]
    return total

def is_equal(operands):
    return 1 if operands.count(operands[0]) == len(operands) else 0

def greater_than(operands):
    # stack pushed right to left, but read left to right
    return 1 if operands[1] > operands[0] else 0

def less_than(operands):
    # stack pushed right to left, but read left to right
    return 1 if operands[1] < operands[0] else 0

operators = {
    0: adding,
    1: multiply,
    2: get_min,
    3: get_max,
    5: greater_than,
    6: less_than,
    7: is_equal
}

def get_data():
    data = DayUtil().open_file("day16")
    binary_padded = ""
    for hexa in data:
        for ch in hexa:
            binary_padded += '{:04b}'.format(int(ch, 16))
    return binary_padded

def get_integer(bin_sequence):
    # sequence can be string or list
    val = 0
    for ch in bin_sequence:
        val = val * 2 + int(ch)
    return val

def process_packet(start_ptr, inpt):
    global packet_version_sum
    ptr = start_ptr
    packet_version = get_integer(inpt[ptr:ptr+3])
    ptr += 3
    type_id = get_integer(inpt[ptr:ptr+3])
    ptr += 3
    if type_id == 4:
        ptr = process_literal(ptr, inpt)
    else:
        stack.append(operators[type_id])
        ptr = process_operator(ptr, inpt)
    return ptr # return last pointer, if invalid return None

def process_operator(start_ptr, inpt):
    ptr = start_ptr
    length_type_id = inpt[ptr]
    ptr += 1
    if length_type_id == '0':
        #length
        len_of_next_subpackets = get_integer(inpt[ptr:ptr+15])
        ptr += 15
        end_of_next_subpackets = ptr+len_of_next_subpackets
        while ptr < end_of_next_subpackets:
            ptr = process_packet(ptr, inpt)
    else:
        num_of_subpackets = get_integer(inpt[ptr:ptr+11])
        ptr += 11
        for _ in range(num_of_subpackets):
            ptr = process_packet(ptr, inpt)
    return ptr

def process_literal(start_ptr, inpt):
    ptr = start_ptr
    done = False
    literal = ''
    while done is False:
        if inpt[ptr] == '0':
            done = True
        ptr += 1
        literal += inpt[ptr:ptr+4]
        ptr += 4
    stack.append(get_integer(literal))
    return ptr # return last pointer, if invalid return None

def calculate(stack):
    op_stack, results_stack = [], []
    while stack:
        curr = stack.pop()
        if type(curr) == int:
            op_stack.append(curr)
        else:
            if op_stack:
                print('curr', curr, 'op_stack', op_stack, 'results_stack', results_stack)
                results_stack.append(curr(op_stack))
                op_stack = []
            else:
                print('curr', curr, 'op_stack', op_stack, 'results_stack', results_stack)
                answer = curr(results_stack)
                results_stack = [answer]
    print('op_stack', op_stack, 'results_stack', results_stack, 'stack', stack)
    print(results_stack)


def day16():
    """ each hex converts to 4 bits, some flags are 3 bits."""
    bin_str_input = get_data()
    ptr = 0
    while ptr != None:
        ptr = process_packet(ptr, bin_str_input)
        ptr = None



day16()

print(stack)
calculate(stack)



