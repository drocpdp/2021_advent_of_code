from day_util import DayUtil


def get_data():
    # [y,x] for each coordinate
    coords = [ (int(c[1]),int(c[0])) for c in [coord.split(",") for coord in DayUtil().open_file("day13_points")]]
    # [(x or y), (x or y line)]
    folds = [ [ff[0][-1],int(ff[1])] for ff in [f.split('=') for f in DayUtil().open_file("day13_folds")]]
    return (coords, folds)

"""
-if horizontal fold, FOLD bottom UP
-if vertical fold, FOLD LEFT

-Some of the dots might end up overlapping after the fold is complete, 
    but dots will never appear exactly on a fold line.

"""
def day13():
    coords, folds = get_data()
    fold_coord, fold_point = folds[0]
    new_coords = set()

    for y,x in coords:
        if fold_coord == 'x':
            if x > fold_point:
                new_point = (y, fold_point - (x - fold_point))
                new_coords.add(new_point)
            else:
                new_coords.add((y,x))
        else:
            if y > fold_point:
                new_point = (fold_point - (y - fold_point),x)
                new_coords.add(new_point)
            else:
                new_coords.add((y,x))
    return len(new_coords)

print(day13())