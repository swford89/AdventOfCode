from os import remove
from pprint import pprint

# figure out life_support_rating 
# life_support_rating = oxygen_generator_rating * co2_scrubber_rating

# oxygen_generator_rating = find MOST COMMON bit in current position --> discard rest until one number left
# co2_scrubber_rating     = find LEAST COMMON bit in current position -> discard rest until one number left

def count_binary(binaries_list):
    for index in INDICIES_DICT.keys():
        for binary_key in INDICIES_DICT[index].keys():
            INDICIES_DICT[index][binary_key] = 0
    for binary in binaries_list:
        for index, num in enumerate(binary):
            if INDICIES_DICT[index]:
                if num in INDICIES_DICT[index].keys():
                    INDICIES_DICT[index][num] += 1
    return INDICIES_DICT

def o2_generator_filter(binaries_list, INDICIES_DICT):
    """
    function to return o2_generator_rating
    filters according to most common values
    """
    sequence_check_string = ''
    # continue to make the sequence string
    for index in INDICIES_DICT.keys():
        # break condition for last binary
        if len(binaries_list) == 1:
            break
        INDICIES_DICT = count_binary(binaries_list)  
        # pprint(INDICIES_DICT)
        # pprint(f"Index #{index}")

        # filter the binaries_list 
        if INDICIES_DICT[index]['0'] < INDICIES_DICT[index]['1']:
            most_common = '1'
            sequence_check_string += most_common
            binaries_list = [binary for binary in binaries_list if binary[index] == most_common and sequence_check_string in binary[:index+1]]

        elif INDICIES_DICT[index]['0'] > INDICIES_DICT[index]['1']:
            most_common = '0'
            sequence_check_string += most_common
            binaries_list = [binary for binary in binaries_list if binary[index] == most_common and sequence_check_string in binary[:index+1]]

        elif INDICIES_DICT[index]['0'] == INDICIES_DICT[index]['1']:
            most_common = '1'
            sequence_check_string += most_common
            binaries_list = [binary for binary in binaries_list if binary[index] == most_common and sequence_check_string in binary[:index+1]]

    o2_generator_rating = int(binaries_list[0], 2)
    return o2_generator_rating

def co2_scrubber_filter(binaries_list, INDICIES_DICT):
    """
    function that returns the co2_scrubber_rating
    filtering according to least common value
    """
    sequence_check_string = ''
    for index in INDICIES_DICT.keys():
        # break condition for last binary
        if len(binaries_list) == 1:
            break
        INDICIES_DICT = count_binary(binaries_list)  
        pprint(INDICIES_DICT)
        pprint(f"Index #{index}")

        # filter the binaries_list 
        if INDICIES_DICT[index]['0'] < INDICIES_DICT[index]['1']:
            least_common = '0'
            sequence_check_string += least_common
            binaries_list = [binary for binary in binaries_list if binary[index] == least_common and sequence_check_string in binary[:index+1]]

        elif INDICIES_DICT[index]['0'] > INDICIES_DICT[index]['1']:
            least_common = '1'
            sequence_check_string += least_common
            binaries_list = [binary for binary in binaries_list if binary[index] == least_common and sequence_check_string in binary[:index+1]]

        elif INDICIES_DICT[index]['0'] == INDICIES_DICT[index]['1']:
            least_common = '0'
            sequence_check_string += least_common
            binaries_list = [binary for binary in binaries_list if binary[index] == least_common and sequence_check_string in binary[:index+1]]

    co2_scrubber_rating = int(binaries_list[0], 2)
    return co2_scrubber_rating

with open('diagnostic.txt', 'r') as doc:
    diagnostic_doc = doc.readlines()
    
    # clean the binaries to prep for counting MOST and LEAST common values
    binaries_list = []
    for dirty_binary in diagnostic_doc:
        cleaned_binary = dirty_binary.rstrip()
        binaries_list.append(cleaned_binary)

    # ditionary to hold binary counts at indicies
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

    co2_scrubber_rating = co2_scrubber_filter(binaries_list, INDICIES_DICT)
    o2_generator_rating = o2_generator_filter(binaries_list, INDICIES_DICT)
    life_support_rating = co2_scrubber_rating * o2_generator_rating
   
    print(f"""
    co2_scrubber_rating: {co2_scrubber_rating}
    o2_generator_rating: {o2_generator_rating}
    life_support_rating: {life_support_rating}
    """)
    