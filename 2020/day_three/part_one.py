# read map data to find route through trees
with open('tree_map.txt', 'r') as doc:
    tree_map = doc.readlines()
    tree_counter = 0
    open_square = '.'
    tree_square= '#'
    giant_string_map = ''
    for tree_row in tree_map:
        # move three to the right, down one, log the tree encounters
        # row index = 0 to 30
        cleaned_path = tree_row.rstrip()
        giant_string_map += cleaned_path

    print(giant_string_map)

    for square in giant_string_map[::33]:
        if square == tree_square:
            tree_counter += 1
 


        # print(len(cleaned_path))
        # move right three
        # skip to next line at same index as above
        # log tree if it's there

    print(tree_counter)
