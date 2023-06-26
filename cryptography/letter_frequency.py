

import string

# Create a dictionary of the letters
letter_dict = {}
all_letters = string.ascii_lowercase

for char in all_letters:
    letter_dict[char] = 0


with open("text.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        words = line.split(" ")
        print(words)





