# read expense lines from .txt doc
with open('expense_input.txt', 'r') as expense_doc:
    expense_lines = expense_doc.readlines()
    # iterate through lines, strip trailing new line, convert string num into int
    expense_nums = []
    for line in expense_lines:
        text_line = line.rstrip()
        num_line = int(text_line)
        expense_nums.append(num_line)
    
    potential_pair = []
    for index, num in enumerate(expense_nums):
        step_index = index + 1
        # iterate through nums and add them together to see if they equal 2020
        while step_index in range(len(expense_nums) - 1):
            if num + expense_nums[step_index] == 2020:
                potential_pair.append(num)
                potential_pair.append(expense_nums[step_index])
                break
            else:
                step_index += 1
        if sum(potential_pair) == 2020:
            break
        
    print(potential_pair)
    print(potential_pair[0] * potential_pair[1])
            

