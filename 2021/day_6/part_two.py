def age_fish(fish_timer_list, old_new_divider):
    """
    function to check for change condtions
    """
    # loop counter for making changes and ensuring they're in place and not skipped
    check_count = 0

    while check_count < 2:
        
        old_fish_slice = fish_timer_list[:old_new_divider]
        new_fish_slice = fish_timer_list[old_new_divider:]

        # age older fish and create new ones
        for index, fish_time in enumerate(fish_timer_list):
            if index == old_new_divider:
                break
            if fish_time == -1:
                fish_timer_list[index] = 6
            if fish_time == 6:
                new_fish = 8
                fish_timer_list.append(new_fish)
            
        # ensure the new fish age fully to 0 before adding back into old fish for new fish creation
        for index, fish_time in enumerate(fish_timer_list):
            if index < old_new_divider:
                continue
            if fish_time == -1:
                fish_timer_list[index] = 6
                old_new_divider += 1

        check_count += 1

    # print(f"old fish: {fish_timer_list[:old_new_divider]}, length: {len(fish_timer_list[:old_new_divider])}")
    # print(f"new fish: {fish_timer_list[old_new_divider:]}")
    # print(f"divider index: {old_new_divider}")

    return fish_timer_list, old_new_divider

with open('example_fish.txt', 'r') as doc:
    fish_doc = doc.readlines()
    fish_timer_list = []
    for line in fish_doc:
        cleaned_line = line.rstrip().split(',')
        for item in cleaned_line:
            fish_timer_list.append(int(item))
    
    print(f"Initial state: {fish_timer_list}\n")

    # iterate through days 
    day_count = 1
    # tracking variable index divide between old and new fish
    old_new_divider = len(fish_timer_list) - 1

    while day_count < 257:   

        # subtract time at end of day(for-loop iteration)
        fish_timer_list = [fish_time - 1 for fish_time in fish_timer_list]
        
        fish_timer_list, old_new_divider = age_fish(fish_timer_list, old_new_divider)   
            
        print(f"""
        After day #{day_count}
        Number of fish: {len(fish_timer_list)} 
        """)

        day_count += 1       