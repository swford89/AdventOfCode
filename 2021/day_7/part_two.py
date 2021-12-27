import sys

with open('fuel_position.txt', 'r') as doc:
    position_doc = doc.readlines()
    position_list = []

    # clean fine to get proper position data
    for position_list_create in position_doc:
        string_position = position_list_create.rstrip().split(',')
        for position in string_position:
            position_list.append(int(position))

    # manipulate position data to get fuel efficient path
    lowest_fuel = sys.maxsize

    # get highest and lowest furl position values to iterate goal position between
    highest_position = max(position_list)
    lowest_position = min(position_list)
    for goal_position in range(lowest_position + 1, highest_position):
        fuel_cost_list = []
        # check fuel cost to goal_position
        for position in position_list:
            fuel_cost_position = 0
            if position == goal_position:
                fuel_cost_list.append(0)
            if position > goal_position:
                position_diff = position - goal_position
                for num in range(1, position_diff + 1):
                    fuel_cost_position += num
                fuel_cost_list.append(fuel_cost_position)
            if position < goal_position:
                position_diff = goal_position - position
                for num in range(1, position_diff + 1):
                    fuel_cost_position += num
                fuel_cost_list.append(fuel_cost_position)

        fuel_sum = sum(fuel_cost_list)
        if fuel_sum < lowest_fuel:
            lowest_fuel = fuel_sum
        
    print(f"Lowest fuel cost: {lowest_fuel}")
