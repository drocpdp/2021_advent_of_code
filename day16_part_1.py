from day_util import DayUtil

packet_version_sum = 0

def get_data():
    data = DayUtil().open_file("day16_test")
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
    print('packet_version', packet_version)
    packet_version_sum += packet_version
    ptr += 3
    type_id = get_integer(inpt[ptr:ptr+3])
    print('type_id', type_id)
    ptr += 3
    if type_id == 4:
        ptr = process_literal(ptr, inpt)
    else:
        ptr = process_operator(ptr, inpt)
    return ptr # return last pointer, if invalid return None

def process_operator(start_ptr, inpt):
    print('process_operator()')
    ptr = start_ptr
    length_type_id = inpt[ptr]
    print('length_type_id', length_type_id)
    ptr += 1
    if length_type_id == '0':
        #length
        len_of_next_subpackets = get_integer(inpt[ptr:ptr+15])
        print('len_of_next_subpackets in bits', len_of_next_subpackets)
        ptr += 15
        end_of_next_subpackets = ptr+len_of_next_subpackets
        while ptr < end_of_next_subpackets:
            ptr = process_packet(ptr, inpt)
    else:
        num_of_subpackets = get_integer(inpt[ptr:ptr+11])
        print('num_of_subpackets', num_of_subpackets)
        ptr += 11
        for _ in range(num_of_subpackets):
            ptr = process_packet(ptr, inpt)
    return ptr

def process_literal(start_ptr, inpt):
    print('process_literal()')
    ptr = start_ptr
    done = False
    literal = ''
    while done is False:
        if inpt[ptr] == '0':
            done = True
        ptr += 1
        literal += inpt[ptr:ptr+4]
        ptr += 4
    print(literal, get_integer(literal))
    return ptr # return last pointer, if invalid return None

def day16():
    """ each hex converts to 4 bits, some flags are 3 bits."""
    bin_str_input = get_data()
    print(bin_str_input)
    ptr = 0
    while ptr != None:
        ptr = process_packet(ptr, bin_str_input)
        print(ptr)
        ptr = None


day16()
print('packet_version_sum', packet_version_sum)