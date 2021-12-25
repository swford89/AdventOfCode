with open('fuel_position.txt', 'r') as doc:
    position_doc = doc.readlines()
    position_list = []

    # clean fine to get proper position data
    for position_list_create in position_doc:
        string_position = position_list_create.rstrip().split(',')
        for position in string_position:
            position_list.append(int(position))
    
    # manipulate position data to get fuel efficient path
    fuel_sum_list = []

    # get highest and lowest furl position values to iterate goal position between
    highest_position = max(position_list)
    lowest_position = min(position_list)
    for goal_position in range(lowest_position, highest_position):
        # track fuel cost to get position to current goal and reset for next goal positon
        fuel_cost_list = []
        for position in position_list:
            if position > goal_position:
                fuel_difference = position - goal_position 
                fuel_cost_list.append(fuel_difference)
            if position == goal_position:
                fuel_cost_list.append(0)
            if position < goal_position:
                fuel_difference = goal_position - position
                fuel_cost_list.append(fuel_difference)

        fuel_sum = sum(fuel_cost_list)
        fuel_sum_list.append(fuel_sum)

    lowest_fuel_sum = min(fuel_sum_list)
    print(f"Lowest fuel cost: {lowest_fuel_sum}")