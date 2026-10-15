print("""        
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

Welcome to Treasure Island.
Your mission is to find the treasure
You're at a cross road. Where do you want to go?
""")

choice1 = input('Type "left" or "right"\n').lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come across a lake. Swim or wait for a boat?. Type "swim" or "wait"\n'
    ).lower()

    if choice2 == "wait":
        print(choice2)
        choice3 = input(
            "You are inside a cave with three colored doors."
            'Which door will you choose to open? Type "red", "blue" or "yellow"\n'
        )

        if choice3 == "red":
            print("You were burned by fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You were eaten by beasts. Gane Over.")
        else:
            print("Game Over.")

    elif choice2 == "swim":
        print("You were attacked by a trout. Game Over.")
    else:
        print("Game Over.")

else:
    print("Game Over.")
