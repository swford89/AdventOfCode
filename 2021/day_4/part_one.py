with open('example_game.txt', 'r') as doc:
    # clean the numbers to be drawn
    dirty_draw_nums = doc.readlines(1)
    draw_nums = []
    for nums in dirty_draw_nums:
        cleaned_num_line = nums.rstrip().split(sep=',')
        for num in cleaned_num_line:
            draw_nums.append(num)

    # clean the bingo cards
    dirty_card_lines = doc.readlines()
    cleaned_card_lines = [card_line.rstrip().lstrip().split() for card_line in dirty_card_lines]
    cards = []
    start_index = 1
    stop_index = 6
    for line in cleaned_card_lines:
        card = cleaned_card_lines[start_index:stop_index]
        if len(card) == 0:
            break
        else:
            cards.append(card)
            start_index = stop_index + 1
            stop_index += 6

    # initialize tracking variables
    FOUND_NUM = 'XX'
    final_score = 0
    final_number = ''
    winning_card_index = 0
    card_column_dict = {}

    # draw bingo numbers
    drawing = True
    # draw number
    for num in draw_nums:
        # draw card                                  
        for card in cards:                         
            card_index = cards.index(card)
            # parse card lines
            for line in card:                       
                # log numbers found on card
                if num in line:                    
                    num_index = line.index(num)
                    line[num_index] = FOUND_NUM
                    found_row_count = line.count(FOUND_NUM)
                    # create sub-dictionary to count found index in columns, if it doesn't exist
                    try:
                        card_column_dict[card_index][num_index]       
                    except KeyError:
                        card_column_dict[card_index] = {num_index: 0}
                    card_column_dict[card_index][num_index] += 1
                    line_index = card.index(line)
                    card[line_index] = line
    
                    # check for compete row
                    if found_row_count == 5:
                        winning_card_index = card_index
                        final_number = num

                        print(f"""
                        completed row, with number: {num}
                        card index: {card_index}
                        card: {cards[card_index]}
                        """)

                        remaining_nums = []
                        remaining_num_sum = 0
                        for line in cards[card_index]:
                            for card_num in line:
                                if card_num != FOUND_NUM:
                                    print(card_num)
                                    remaining_nums.append(int(card_num))
                        remaining_num_sum = sum(remaining_nums)
                        final_score = int(final_number) * remaining_num_sum
                        print(f"""
                        Total sum of remaining nums: {remaining_num_sum}
                        final score: {final_score}
                        """)

                        drawing = False
                        break

                    if drawing == False:
                        break
            if drawing == False:
                break
        if drawing == False:
            break
                 
