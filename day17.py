from day_util import DayUtil

isTest = True

def get_data():
    file_str = "day17_test" if isTest else "day17"
    data = DayUtil().open_file(file_str)
    return data

def day17():
    data = get_data()
    print(data)


day17()