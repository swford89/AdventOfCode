# read password policy and passwords from doc
with open('password_doc.txt', 'r') as doc:
    policy_pass_lines = doc.readlines()
    valid_count = 0
    for line in policy_pass_lines:
        # prep data for processing: get integers, letter, password
        cleaned_pol_pass = line.rstrip().split()
        letter_range = cleaned_pol_pass[0].split(sep='-')
        number_range = int(letter_range[0]), int(letter_range[1])
        letter = cleaned_pol_pass[1].strip(':')
        password = cleaned_pol_pass[2]
        letter_count = password.count(letter)
        if number_range[0] <= letter_count <= number_range[1]:
            valid_count += 1
    
    print(valid_count)