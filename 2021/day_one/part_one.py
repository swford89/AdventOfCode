# read sonar depth
with open('sonar_depth.txt', 'r') as doc:
    depth_doc = doc.readlines()
    depth_list = [int(depth.rstrip()) for depth in depth_doc ]
    # iterate through depth_list and count the depth increases
    increase_depth_count = 0
    last_measure = depth_list[0]
    for depth in depth_list[1:]:
        if depth > last_measure:
            increase_depth_count += 1
            last_measure = depth
        else:
            last_measure = depth

    print(increase_depth_count)