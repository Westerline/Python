# Load poem and read variables, will result in an emptry string on the second read, so we must reload the variable.
Poem = open('clouds.txt')

Poem.read()

Poem.read()

Poem = open('clouds.txt')

# Reading individual lines or all lines
Line = Poem.readline()

Lines = Poem.readlines()

# Iterate through each line in a file
Poem = open('clouds.txt')
for line in Poem:
    print(line.strip('\n'))
