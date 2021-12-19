from pprint import pprint

def get_greatest_values(coordinate_list):
    """finds the max x and y coordinates"""
    greatest_x = 0
    greatest_y = 0
    # unpack tuples from list
    for line_coords in coordinate_list:
        # line origin coordinates
        line_origin = line_coords[0]
        x1 = line_origin[0]
        y1 = line_origin[1]
        # line end coordinates
        line_end = line_coords[1]
        x2 = line_end[0]
        y2 = line_end[1]
        # check origin points for greatest values
        if int(y1) > greatest_y:
            greatest_y = int(y1)
        if int(x1) > greatest_x:
            greatest_x = int(x1)
        # check end points for greatest values
        if int(y2) > greatest_y:
            greatest_y = int(y2)
        if int(x2) > greatest_x:
            greatest_x = int(x2)
    return greatest_x, greatest_y

with open('vent_coordinates.txt', 'r') as doc:
    # list contains a sub-list of tuple coordinates
    # x1, y1 : origin
    # x2, y2 : end
    coordinate_list = []
    dirty_doc = doc.readlines()
    # clean the data
    for coordinate in dirty_doc:
        semi_cleaned_coordinate = coordinate.rstrip().split(' -> ')
        origin_tup = tuple(semi_cleaned_coordinate[0].split(','))
        end_tup = tuple(semi_cleaned_coordinate[1].split(','))
        line_tups = [origin_tup, end_tup]
        coordinate_list.append(line_tups)
    
    # create a map/list consisting a list of lists (list for line index = y values) of lists(list for item index = x values)
    pseudo_map = []
    
    # find greatest coordinates needed to construct list indicies
    greatest_x, greatest_y = get_greatest_values(coordinate_list)

    # list holding lines, refered to by index (however many lines of coordinated there are)
    for num in range(greatest_y + 1):
        coordinate_line = []
        for num in range(greatest_x +1):
            x_index = []
            coordinate_line.append(x_index)
        pseudo_map.append(coordinate_line)

    pprint(coordinate_list)

    # iterate through coordinates
    for line_coords in coordinate_list:
        # line origin coordinates
        line_origin = line_coords[0]
        x1 = int(line_origin[0])
        y1 = int(line_origin[1])
        # line end coordinates
        line_end = line_coords[1]
        x2 = int(line_end[0])
        y2 = int(line_end[1])

        # log vertical lines into pseudo_map
        if x1 == x2:
            mapped_origin_point = pseudo_map[y1][x1]
            mapped_end_point = pseudo_map[y2][x2]
            if len(mapped_origin_point) > 0 or len(mapped_end_point) > 0:
                pseudo_map[y1][x1] = [sum(pseudo_map[y1][x1] + [1])]        # start point
                pseudo_map[y2][x2] = [sum(pseudo_map[y2][x2] + [1])]        # end point
            else:
                pseudo_map[y1][x1] = [1]         # start point
                pseudo_map[y2][x2] = [1]            # end point

            # get remaining points in line
            smallest_y = min(y1, y2)
            largest_y = max(y1, y2)

            for num in range(smallest_y + 1, largest_y):
                missing_point = pseudo_map[num][x2]
                if len(missing_point) > 0:
                    pseudo_map[num][x2] = [sum(pseudo_map[num][x2] + [1])]
                else:
                    pseudo_map[num][x2] = [1]

        # log horizontal lines into pseudo_map
        if y1 == y2:
            mapped_origin_point = pseudo_map[y1][x1]
            mapped_end_point = pseudo_map[y2][x2]
            if len(mapped_origin_point) > 0 or len(mapped_end_point) > 0:
                pseudo_map[y1][x1] = [sum(pseudo_map[y1][x1] + [1])]        # start point
                pseudo_map[y2][x2] = [sum(pseudo_map[y2][x2] + [1])]           # end point
            else:
                pseudo_map[y1][x1] = [1]          # start point
                pseudo_map[y2][x2] = [1]            # end point

            # get remaining points in line
            smallest_x = min(x1, x2)
            largest_x = max(x1, x2)

            for num in range(smallest_x + 1, largest_x):
                missing_point = pseudo_map[y2][num]
                if len(missing_point) > 0:
                    pseudo_map[y2][num] = [sum(pseudo_map[y2][num] + [1])]
                else:
                    pseudo_map[y2][num] = [1]

        # log diagonal lines
        if x1 != x2 and y1 != y2:
            # downward diagonal
            mapped_origin_point = pseudo_map[y1][x1]
            mapped_end_point = pseudo_map[y2][x2]
            # add start and end point to map
            if len(mapped_origin_point) > 0 or len(mapped_end_point) > 0:
                pseudo_map[y1][x1] = [sum(pseudo_map[y1][x1] + [1])]        # start point
                pseudo_map[y2][x2] = [sum(pseudo_map[y2][x2] + [1])]           # end point
            else:
                pseudo_map[y1][x1] = [1]          # start point
                pseudo_map[y2][x2] = [1]            # end point

            # add missing diagonal points
            if y1 < y2:
                # downward right diagonal
                if x1 < x2:
                    diag_x = x1 + 1
                    diag_y = y1 + 1
                    while diag_x != x2 and diag_y != y2:
                        if len(pseudo_map[diag_y][diag_x]) > 0:
                            pseudo_map[diag_y][diag_x] = [sum(pseudo_map[diag_y][diag_x] + [1])]
                            diag_x += 1
                            diag_y += 1
                        else:
                            pseudo_map[diag_y][diag_x] = [1]
                            diag_x += 1
                            diag_y += 1

                # downward left diagonal
                else:
                    diag_x = x1 - 1
                    diag_y = y1 + 1
                    while diag_x != x2 and diag_y != y2:
                        if len(pseudo_map[diag_y][diag_x]) > 0:
                            pseudo_map[diag_y][diag_x] = [sum(pseudo_map[diag_y][diag_x] + [1])]
                            diag_x -= 1
                            diag_y += 1
                        else:
                            pseudo_map[diag_y][diag_x] = [1]
                            diag_x -= 1
                            diag_y += 1
            
            # upward diagonal
            if y1 > y2:
                # upward right diagonal
                if x1 < x2:
                    diag_x = x1 + 1
                    diag_y = y1 - 1
                    while diag_x != x2 and diag_y != y2:
                        if len(pseudo_map[diag_y][diag_x]) > 0:
                            pseudo_map[diag_y][diag_x] = [sum(pseudo_map[diag_y][diag_x] + [1])]
                            diag_x += 1
                            diag_y -= 1
                        else:
                            pseudo_map[diag_y][diag_x] = [1]
                            diag_x += 1
                            diag_y -= 1

                # upward left diagonal
                else:
                    diag_x = x1 - 1
                    diag_y = y1 - 1
                    while diag_x != x2 and diag_y != y2:
                        if len(pseudo_map[diag_y][diag_x]) > 0:
                            pseudo_map[diag_y][diag_x] = [sum(pseudo_map[diag_y][diag_x] + [1])]
                            diag_x -= 1
                            diag_y -= 1
                        else:
                            pseudo_map[diag_y][diag_x] = [1]
                            diag_x -= 1
                            diag_y -= 1

    # pprint(pseudo_map)
    overlap_count = 0
    for index, line in enumerate(pseudo_map):
        # print(index, line)
        for count in line:
            if len(count) > 0:
                for num in count:
                    # print(num)
                    if num >= 2:
                        # print(num)
                        overlap_count += 1
    
    print(overlap_count)