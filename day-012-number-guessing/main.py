import random

from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty(diff):
    if diff == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def check_answer(lives, attempt, number):
    if attempt > number:
        print("Too high")
        return lives - 1
    elif attempt < number:
        print("Too low")
        return lives - 1
    else:
        print(f"You got it! The answer was {number}")


def start_game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100")
    number = random.randint(0, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard")

    lives = set_difficulty(difficulty)

    attempt = 0
    while attempt != number:
        print(f"You have {lives} attempts remaining to guess the number")
        attempt = int(input("Make a guess: "))
        lives = check_answer(lives, attempt, number)

        if lives == 0:
            print(f"You've run out of guesses, you lose. The right number was {number}")
            return
        elif attempt != number:
            print("Guess again.")


start_game()
