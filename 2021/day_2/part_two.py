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
    aim_value = 0
    POSITION_DICT = {
        'forward': 1,           # increases horizontal_position; 
        'down': 1,              # increases aim_value
        'up': -1,               # decreased aim_value
    }

    for movement_tuple in position_list:
        movement = movement_tuple[0]
        step_value = movement_tuple[1]
        if movement in POSITION_DICT.keys():
            # log depth and aim values
            if movement == 'up' or movement == 'down':
                depth_aim_log = POSITION_DICT[movement] * step_value
                aim_value += depth_aim_log
            # log horizontal_position; aim * step_value to get new depth
            if movement == 'forward':
                horizontal_position += step_value
                depth_value += step_value * aim_value

    print(f"""
    Horizontal Position: {horizontal_position}
    Depth value: {depth_value}
    Aim value: {aim_value}
    Horizontal Postion and Depth Product: {horizontal_position * depth_value}
    """)

