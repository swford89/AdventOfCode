from pprint import pprint

nums = range(3000)

# read sonar depth
with open('sonar_depth.txt', 'r') as doc:
    depth_doc = doc.readlines()
    depth_list = [int(depth.rstrip()) for depth in depth_doc ]
    num_sum_dict = {}
    # get sums for groups of three measurements 
    # count the increased sum-of-three measurements
    increment_start = 0
    increment_upto = 3
    for num in nums:
        three_slice = depth_list[increment_start:increment_upto]
        if len(three_slice) == 3:
            print(f"""
            {three_slice}
            {len(three_slice)}
            """)
            three_added = sum(three_slice)
            num_sum_dict[num] = three_added
            increment_start += 1
            increment_upto += 1
        else:
            break
    # evaluate values in dictionary to count increased sum-of-three measurements
    increased_sums = 0
    base_measure = num_sum_dict[0]
    for value in num_sum_dict.values():
        if value > base_measure:
            increased_sums += 1
            base_measure = value
        else:
            base_measure = value

    pprint(num_sum_dict)
    print(increased_sums)