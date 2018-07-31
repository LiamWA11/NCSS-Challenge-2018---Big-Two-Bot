import random
import program

SUITS = ['H', 'S', 'D', 'C']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']


PLAYER_HANDS = []
IS_START_OF_ROUND = True
PLAY_TO_BEAT = []
ROUND_HISTORY = []
TRICK_HISTORY = []
PLAYER_NO = -1
HAND_SIZES = [-1, -1, -1, -1]
SCORES= [0, 0, 0, 0]
ROUND_NO = -1


def card_generator() -> list:
    cards = []
    for suit in SUITS:
        for value in VALUES:
            cards.append(value + suit)
    return cards


def hand_generator(deck: list) -> list:
    generated_hands = []
    for i in range(4):
        hand = []
        for i in range(13):
            card_id = random.randint(0, len(deck) - 1)
            hand.append(deck.pop(card_id))
        generated_hands.append(hand)
    return generated_hands


def update_hand_sizes(hand_sizes: list[int], player_hands: list[str]) -> list:
    for i in range(3):
        hand_sizes[i] = len(player_hands[i])
    return hand_sizes


def process_round(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
    raise NotImplementedError


def play():
    global PLAYER_HANDS

    PLAYER_HANDS = hand_generator(card_generator())

    for round in range(10):
        global ROUND_NO
        global HAND_SIZES
        global SCORES

        ROUND_NO = round
        HAND_SIZES = update_hand_sizes(HAND_SIZES, PLAYER_HANDS)

        for score in SCORES:
            if score >= 100:
                break

        

        process_round()

    raise NotImplementedError

if __name__ == '__main__':
    play()