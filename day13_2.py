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
    new_coords = coords
    tmp = []
    for fold_coord, fold_point in folds:
        tmp = []
        for y,x in new_coords:
            if fold_coord == 'x':
                if x > fold_point:
                    new_point = (y, fold_point - (x - fold_point))
                    tmp.append(new_point)
                else:
                    tmp.append((y,x))
            else:
                if y > fold_point:
                    new_point = (fold_point - (y - fold_point),x)
                    tmp.append(new_point)
                else:
                    tmp.append((y,x))
        new_coords = tmp
    
    max_y = max(new_coords, key= lambda nc:nc[0])[0]
    max_x = max(new_coords, key= lambda nc:nc[1])[1]
    grid = [[" " for x in range(max_x+1)] for y in range(max_y+1)]

    for y,x in new_coords:
        grid[y][x] = "*"
    for row in grid:
        print("".join(row))


day13()