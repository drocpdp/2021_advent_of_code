class DayUtil:

    def open_file(day_str):
        fp = open('./{}.txt'.format(day_str), 'r')
        measures = [l.strip() for l in fp.readlines()]
        fp.close()           
        return measures

