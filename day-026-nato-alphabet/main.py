import pandas

student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}

word = input("Enter a word: ").upper()

output = [dictionary[letter] for letter in word]

print(output)
