file = open("input.txt")
text = file.read()
characterArray = list(text)


def findBuffer(character):
    for loop in range(0,len(character)):
        if character[loop] != character[loop + 1] and character[loop] != character[loop + 2] and character[loop] != character[loop + 3] and character[loop + 1] != character[loop + 2] and character[loop+1] != character[loop + 3] and character[loop + 2] != character[loop + 3]:
            print(loop + 4)
            buffer = character[loop] + character[loop + 1] + character[loop + 2] + character[loop + 3]
            return buffer
print(findBuffer(characterArray))