import random

from art import logo, vs
from game_data import data


def check_answer(choice, celebA, celebB, score):

    if (
        choice == "A"
        and celebA["follower_count"] > celebB["follower_count"]
        or choice == "B"
        and celebB["follower_count"] > celebA["follower_count"]
    ):
        celebB = celebA
        celebB = random.choice(data)

        while celebA == celebB:
            celebB = random.choice(data)

        score += 1
        game_over = False

        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score {score}")
        return score, game_over
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True
        return score, game_over


def start_game():

    print(logo)
    score = 0
    celebA = random.choice(data)
    celebB = random.choice(data)

    while celebA == celebB:
        celebB = random.choice(data)

    game_over = False
    while not game_over:
        print(
            f"Compare A: {celebA['name']}, {celebA['description']}, from {celebA['country']}."
        )
        print(vs)
        print(
            f"Against B: {celebB['name']}, {celebB['description']}, from {celebB['country']}."
        )

        choice = input("Who has more followers: Type 'A' or 'B': ").upper()
        score, game_over = check_answer(choice, celebA, celebB, score)


start_game()
