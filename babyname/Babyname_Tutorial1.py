import random, string

letter_input1 = input('Choose a letter... "v" for a vowel, "c" for a consonant, "l" for either, or any other character.')
letter_input2 = input('Choose a letter... "v" for a vowel, "c" for a consonant, "l" for either, or any other character.')
letter_input3 = input('Choose a letter... "v" for a vowel, "c" for a consonant, "l" for either, or any other character.')
letter_input4 = input('Choose a letter... "v" for a vowel, "c" for a consonant, "l" for either, or any other character.')

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase

def generator():
    if letter_input1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input1 == "c":
        letter1 = random.choice(consonants)
    elif letter_input1 == "l":
        letter1 = random.choice(string.ascii_lowercase)
    else:
        letter1 = letter_input_1

    if letter_input2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input2 == "l":
        letter2 = random.choice(string.ascii_lowercase)
    else:
        letter2 = letter_input_2

    if letter_input3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input3 == "l":
        letter3 = random.choice(string.ascii_lowercase)
    else:
        letter3 = letter_input_3

    if letter_input4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input4 == "l":
        letter4 = random.choice(string.ascii_lowercase)
    else:
        letter4 = letter_input_4

    name = letter1 + letter2 + letter3 + letter4
    return (name)

for i in range(20):
    print(generator())