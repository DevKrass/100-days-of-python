# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    blueprint = file.readlines()

names = []
with open("./Input/Names/invited_names.txt", mode="r") as file:
    for line in file:
        name = line.strip()
        names.append(name)

for name in names:
    blueprint[0] = f"Dear {name},\n"
    with open(f"./Output/ReadyToSend/letter_to_{name}.docx", mode="w") as file:
        file.writelines(blueprint)
