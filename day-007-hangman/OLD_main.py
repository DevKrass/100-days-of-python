import random

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

display = []
for char in word:
    display.append("_")

print("".join(display))

right_guesses = 0
lives = 6
while right_guesses < len(word) or lives > 0:
    guess = input("Guess a letter: ")
    for i, char in enumerate(word):
        if char == guess and display[i] != char:
            display[i] = char
            right_guesses += 1
        else:
            lives -= 1
    print("".join(display))

if lives == 0:
    print("You Lose")
else:
    print("You Win")
