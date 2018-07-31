RANK_DICT = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '0': 7, 'J': 8, 'Q': 9, 'K': 10, 'A': 11, '2': 12}
SUIT_DICT = {'D': 0, 'C': 1, 'H': 2, 'S': 3}

sorted_cards = []


def numerical_rank_card(card):
    return SUIT_DICT[card[1]] + RANK_DICT[card[0]]


def compare_cards(card):
    vals = [RANK_DICT[card[0]], SUIT_DICT[card[1]]]
    return vals


def is_higher(card1, card2):
    if compare_cards(card1) > compare_cards(card2):
        return True
    else:
        return False


def sort_cards(cards):
    sorted_cards = sorted(cards, key=compare_cards)
    return sorted_cards


def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
    """
    The parameters to this function are:
    * `hand`: A list of card strings that are the card(s) in your hand.
    * `is_start_of_round`: A Boolean that indicates whether or not the `play` function is being asked to make the first play of a round.
    * `play_to_beat`: The current best play of the trick. If no such play exists (you are the first play in the trick), this will be an empty list.
    * `round_history`: A list of *trick_history* entries.
      A *trick_history* entry is a list of *trick_play* entries.
      Each *trick_play* entry is a `(player_no, play)` 2-tuple, where `player_no` is an integer between 0 and 3 (inclusive) indicating which player made the play, and `play` is the play that said player made, which will be a list of card strings.
    * `player_no`: An integer between 0 and 3 (inclusive) indicating which player number you are in the game.
    * `hand_sizes`: A 4-tuple of integers representing the number of cards each player has in their hand, in player number order.
    * `scores`: A 4-tuple of integers representing the score of each player at the start of this round, in player number order.
    * `round_no`: An integer between 0 and 9 (inclusive) indicating which round number is currently being played.

    This function should return an empty list (`[]`) to indicate a pass (see "Playing a Round"), or a list of card strings, indicating that you want to play these cards to the table as a valid play.
    """

    sorted_cards = sort_cards(hand)

    # If we are starting a trick, we cannot pass.
    if len(play_to_beat) == 0:
        # If we are the first play in a round, the 3D must be in our hand. Play it.
        # Otherwise, we play a random card from our hand.
        if is_start_of_round:
            play = [sorted_cards[0]]
        else:
            for size in hand_sizes:
                if size < 3:
                    play = [sorted_cards[-1]]
                    return play
            play = [sorted_cards[0]]
        return play
    else:
        if hand_sizes[(player_no + 1) % 3] < 3:
            if is_higher(sorted_cards[-1], play_to_beat[0]):
                play = [sorted_cards[-1]]
                return play
        # print(sorted_cards)
        for size in hand_sizes:
            if size <= 6:
                for card in sorted_cards:
                    if is_higher(card, play_to_beat[0]):
                        play = [card]
                        return play
        for card in sorted_cards:
            if is_higher(card, play_to_beat[0]):
                rank_card = numerical_rank_card(card)
                rank_card_to_beat = numerical_rank_card(play_to_beat[0])
                if rank_card - rank_card_to_beat > 12:
                    play = []
                    return play
                play = [card]
                return play

    # We don't know how to play any other kinds of tricks, so play a pass.
    return []


if __name__ == '__main__':
    # Write your own test cases for your `play` function here.
    # These can be run with the Run button and will not affect the tournament or marking.

    # Here's an example test case and testing code to kick you off.
    TESTS = [  # [ expected return value, inputs ]
        [['3D'], [['3D', '4D', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [], [[]], 0,
                  [13, 13, 13, 13], [0, 0, 0, 0], 0]],
        [['4D'], [['3D', '4D', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, ['3D'], [[]], 0,
                  [13, 13, 13, 13], [0, 0, 0, 0], 0]]
        # Add more tests here.
    ]

    # This runs the above test cases.
    for i, test in enumerate(TESTS):
        expected_return_value, inputs = test
        actual_return_value = play(*inputs)
        if actual_return_value == expected_return_value:
            print('PASSED {}/{}.'.format(i + 1, len(TESTS)))
        else:
            print('FAILED {}/{}.'.format(i + 1, len(TESTS)))
            print('    inputs:', repr(inputs))
            print('  expected:', repr(expected_return_value))
            print('    actual:', repr(actual_return_value))