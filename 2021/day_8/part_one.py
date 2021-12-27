from pprint import pprint

with open('seven_segment.txt', 'r') as doc:
    signal_doc = doc.readlines()
    correct_signal_output_dict = {
        '0': 'abcefg',          # length = 6
        '1': 'cf',                              # length = 2
        '2': 'acdeg',           # length = 5
        '3': 'acdfg',           # length = 5
        '4': 'bcdf',                            # length = 4
        '5': 'abdfg',           # length = 5
        '6': 'abdefg',          # length = 6
        '7': 'acf',                             # length = 3
        '8': 'abcdefg',                         # length = 7
        '9': 'abcdfg',          # length = 6
    }

    messed_signal_output_dict = {}
    # clean the file data for processing
    for entry in signal_doc:
        signal_and_output = entry.rstrip().split(' | ')
        signal_pattern = tuple(signal_and_output[0].split())
        output = tuple(signal_and_output[1].split())
        messed_signal_output_dict[signal_pattern] = output

    # counter variables for outputs with unique lengths
    one_counter = 0
    four_counter = 0
    seven_counter = 0
    eight_counter = 0

    for output_tuple in messed_signal_output_dict.values():
        for output in output_tuple:
            if len(output) == 2:
                one_counter += 1
            elif len(output) == 4:
                four_counter += 1
            elif len(output) == 3:
                seven_counter += 1
            elif len(output) == 7:
                eight_counter += 1

    unique_output_sum = one_counter + four_counter + seven_counter + eight_counter
    print(unique_output_sum)