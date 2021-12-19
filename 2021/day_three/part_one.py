from pprint import pprint

with open('diagnostic.txt', 'r') as doc:
    diagnostic_doc = doc.readlines()
    binaries_list = []
    INDICIES_DICT = {
        0: {'0': 0, '1': 0},
        1: {'0': 0, '1': 0},
        2: {'0': 0, '1': 0},
        3: {'0': 0, '1': 0},
        4: {'0': 0, '1': 0},
        5: {'0': 0, '1': 0},
        6: {'0': 0, '1': 0},
        7: {'0': 0, '1': 0},
        8: {'0': 0, '1': 0},
        9: {'0': 0, '1': 0},
        10: {'0': 0, '1': 0},
        11: {'0': 0, '1': 0},
    }

    # clean the binaries and get decimal value for gamma_rate
    for dirty_binary in diagnostic_doc:
        cleaned_binary = dirty_binary.rstrip()
        binaries_list.append(cleaned_binary)

    # iterate through binary numbers to find most and least common values at indicies
    for binary in binaries_list:
        for index, num in enumerate(binary):
            if INDICIES_DICT[index]:
                if num in INDICIES_DICT[index].keys():
                    INDICIES_DICT[index][num] += 1

    # find most common value at indicies to get gamma_rate
    gamma_binary = ''
    for key in INDICIES_DICT.keys():
        if INDICIES_DICT[key]['0'] > INDICIES_DICT[key]['1']:
            gamma_binary += '0'
        else:
            gamma_binary += '1'

    gamma_rate = int(gamma_binary, 2)

    # flip the gamma_binary to get epsilon_binary
    epsilon_binary = ''
    for char in gamma_binary:
        if char == '0':
            epsilon_binary += '1'
        if char == '1':
            epsilon_binary += '0'

    epsilon_rate = int(epsilon_binary, 2)

    # get power_rate by multiplying gamma and epsilon
    power_rate = gamma_rate * epsilon_rate
    
    print(f"""
    Gamma rate: {gamma_rate}
    Epsilon rate: {epsilon_rate}
    Power rate: {power_rate}
    """)