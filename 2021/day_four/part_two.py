with open('bingo_game.txt', 'r') as doc:
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
    COMPLETE_LINE = ['XX', 'XX', 'XX', 'XX', 'XX']
    final_score = 0
    final_num = ''
    winning_card_index = 0
    card_column_dict = {}
    winning_cards_list = []

    # create dictionary to hold column count
    for card_index in range(len(cards)):
        card_column_dict[card_index] = [{'winning_status': False}]
        for index_num in range(5):
            index_dict = {index_num: 0}
            card_column_dict[card_index].append(index_dict)

    # draw number
    for num in draw_nums:
        # draw card                                  
        for card in cards:                         
            card_index = cards.index(card)
            if COMPLETE_LINE in card or card_column_dict[card_index][0]['winning_status'] == True:
                continue
            # parse card lines
            for line in card:                       
                # log numbers found on card
                if num in line:                   
                    index_num = line.index(num)
                    line[index_num] = FOUND_NUM
                    found_row_count = line.count(FOUND_NUM)
                    line_index = card.index(line)
                    card[line_index] = line

                    # process card with complete row
                    if line == COMPLETE_LINE:
                        card_column_dict[card_index][0] = {'winning_status': True}
                        final_num = num
                        winning_card_index = card_index
                        winning_card = cards[card_index]
                        winning_cards_list.append(winning_card)
                        remaining_nums = []
                        remaining_num_sum = 0
                        for card in cards[card_index]:
                            for card_num in card:
                                if card_num != FOUND_NUM:
                                    remaining_nums.append(int(card_num))
                        remaining_num_sum = sum(remaining_nums)
                        final_score = int(final_num) * remaining_num_sum

                        print(f"""
                        completed, with number: {final_num}
                        card index: {card_index}
                        card: {cards[card_index]}
                        Total sum of remaining nums: {remaining_num_sum}
                        final score: {final_score}
                        """)
                        
                        continue

                    # create sub-dictionary to count found index in columns, if it doesn't exist
                    for list_item in card_column_dict[card_index]:
                        for inner_key in list_item.keys():
                            if type(inner_key) == str and list_item[inner_key] == True:
                                continue
                            if inner_key == index_num:
                                list_item[index_num] += 1

                                # process card with complete column
                                if list_item[index_num] == 5:
                                    card_column_dict[card_index][0] = {'winning_status': True}
                                    final_num = num
                                    winning_card_index = card_index
                                    winning_card = cards[card_index]
                                    winning_cards_list.append(winning_card)
                                    remaining_nums = []
                                    remaining_num_sum = 0
                                    for card in cards[card_index]:
                                        for card_num in card:
                                            if card_num != FOUND_NUM:
                                                remaining_nums.append(int(card_num))
                                    remaining_num_sum = sum(remaining_nums)
                                    final_score = int(final_num) * remaining_num_sum

                                    print(f"""
                                    completed, with number: {final_num}
                                    card index: {card_index}
                                    card: {cards[card_index]}
                                    Total sum of remaining nums: {remaining_num_sum}
                                    final score: {final_score}
                                    """)
