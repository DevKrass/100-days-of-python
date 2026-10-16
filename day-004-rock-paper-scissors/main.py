import random

import ascii_art

options = ["rock", "paper", "scissors"]

art = [ascii_art.rock, ascii_art.paper, ascii_art.scissors]

player_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
)

player_choice = options[player_input]

print(art[player_input])

computer_input = random.randint(0, 1)

print(f"Computer chose \n {art[computer_input]}")

computer_choice = options[computer_input]

if player_choice == computer_choice:
    print("Draw")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("You win")
    elif computer_choice == "paper":
        print("You lose")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("You win")
    elif computer_choice == "scissors":
        print("You lose")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("You win")
    elif computer_choice == "rock":
        print("You lose")
