import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    """Return random card from deck of cards"""
    return random.choice(cards)


def count_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def game_start():

    print(art.logo)
    player_hand = []
    computer_hand = []
    computer_score = -1
    player_score = -1
    game_over = False

    for _ in range(2):
        player_hand.append(draw_card())
        computer_hand.append(draw_card())

    while not game_over:
        player_score = count_score(player_hand)
        computer_score = count_score(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: n") == "y":
                player_hand.append(draw_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(draw_card())
        computer_score = count_score(computer_hand)

    # Change score from 0 flag to value 21 so it displays correctly when printed
    if player_score == 0:
        player_score = 21

    if computer_score == 0:
        computer_score = 21

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    game_start()
