# read expense lines from .txt doc
with open('expense_input.txt', 'r') as expense_doc:
    expense_lines = expense_doc.readlines()
    # iterate through lines, strip trailing new line, convert string num into int
    expense_nums = []
    for line in expense_lines:
        text_line = line.rstrip()
        num_line = int(text_line)
        expense_nums.append(num_line)
    # iterate through numbers and add three at a time to find what three add to 2020
    GOAL_NUMBER = 2020
    possible_three = []
    for index, num in enumerate(expense_nums):
        step_index = index + 1
        while step_index in range(len(expense_nums) - 1):
            third_num = GOAL_NUMBER - num - expense_nums[step_index]
            test_total = num + expense_nums[step_index] + third_num
            if third_num in expense_nums and test_total == GOAL_NUMBER:
                possible_three.append(num)
                possible_three.append(expense_nums[step_index])
                possible_three.append(third_num)
                break
            else:
                step_index += 1
        if sum(possible_three) == GOAL_NUMBER:
            break
    
    print(possible_three)
    print(sum(possible_three))
    print(possible_three[0] * possible_three[1] * possible_three[2])
