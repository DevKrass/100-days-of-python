import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level
# Password characters are concatenated in order

password = ""

for char in range(nr_letters):
    password += random.choice(letters)


for char in range(nr_symbols):
    password += random.choice(symbols)


for char in range(nr_numbers):
    password += random.choice(numbers)

print(password)

# Hard Level
# Password characters are concatenated in random order

password_as_list = list(password)

random.shuffle(password_as_list)

shuffled_password = ""
for char in password_as_list:
    shuffled_password += char

print(shuffled_password)
