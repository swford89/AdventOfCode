# read submarine position from doc
with open('position_depth.txt', 'r') as doc:
    position_doc = doc.readlines()
    position_list = []
    for position in position_doc:
        cleaned_position = position.rstrip().split()
        movement_tuple = (cleaned_position[0], int(cleaned_position[1]))
        position_list.append(movement_tuple)

    horizontal_position = 0
    depth_value = 0
    POSITION_DICT = {
        'forward': 1,
        'down': 1,
        'up': -1,
    }

    for movement_tuple in position_list:
        if movement_tuple[0] in POSITION_DICT.keys():
            movement = movement_tuple[0]
            step_value = movement_tuple[1]
            # depth logging here
            if movement == 'up' or movement == 'down':
                depth_to_log = POSITION_DICT[movement] * step_value
                depth_value += depth_to_log
            # horizontal logging here
            if movement == 'forward':
                horizontal_to_log = POSITION_DICT[movement] * step_value
                horizontal_position += horizontal_to_log

    horizontal_depth_product = horizontal_position * depth_value

    print(f"""
    Horizontal Position: {horizontal_position}
    Depth: {depth_value}
    Product of both: {horizontal_depth_product}
    """)
