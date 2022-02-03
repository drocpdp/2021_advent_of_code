from day_util import DayUtil
from itertools import product

isTest = True

def get_data():
    target_points_real = product((i for i in range(169,206+1)), (j for j in range(-108,-68+1))) #full
    target_points_test = product((i for i in range(20,30+1)), (j for j in range(-10,-5+1))) #test    
    data = target_points_test if isTest else target_points_real
    return data

def day17():
    data = get_data()
    print(list(data))


day17()