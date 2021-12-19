# read password policy and passwords from doc
with open('password_doc.txt', 'r') as doc:
    policy_pass_lines = doc.readlines()
    valid_count = 0
    for line in policy_pass_lines:
        # prep data for processing: get integers, letter, password
        # corporate data DOES NOT use 0 index
        cleaned_pol_pass = line.rstrip().split()
        letter_range = cleaned_pol_pass[0].split(sep='-')
        index_range = int(letter_range[0]) -1, int(letter_range[1]) -1          # shift index -1 
        letter = cleaned_pol_pass[1].strip(':')
        password = cleaned_pol_pass[2]
        letter_count = password.count(letter)
        print(index_range)
        try:
            if letter == password[index_range[0]] or letter == password[index_range[1]]:
                print(f"""
                {letter}: {password}
                {password[index_range[0]]} and {password[index_range[1]]}
                """)
                if letter == password[index_range[0]] and letter == password[index_range[1]]:
                    pass
                else:
                    valid_count += 1
                    print(f"Added at {letter}, with password: {password}")
        except IndexError:
            pass
    
    print(valid_count)