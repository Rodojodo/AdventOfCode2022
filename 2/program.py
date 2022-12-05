

file = open("input.txt")
strategy = file.read()
roundArray = strategy.split("\n")
filledRound = [""]*2500
score = 0
response = [""]*2500

for loop in range(0, 2500):
    filledRound[loop] = [""]*2
    filledRound[loop] = roundArray[loop].split(" ")
    if filledRound[loop][1] == "Y":
        score = score + 3
    elif filledRound[loop][1] == "Z":
        score = score + 6


    if filledRound[loop][0] == "A" and filledRound[loop][1] == "X":
        response[loop] = "Z"
    if filledRound[loop][0] == "A" and filledRound[loop][1] == "Y":
        response[loop] = "X"    
    if filledRound[loop][0] == "A" and filledRound[loop][1] == "Z":
        response[loop] = "Y"

    if filledRound[loop][0] == "B" and filledRound[loop][1] == "X":
        response[loop] = "X"
    if filledRound[loop][0] == "B" and filledRound[loop][1] == "Y":
        response[loop] = "Y"
    if filledRound[loop][0] == "B" and filledRound[loop][1] == "Z":
        response[loop] = "Z"


    if filledRound[loop][0] == "C" and filledRound[loop][1] == "X":
        response[loop] = "Y"
    if filledRound[loop][0] == "C" and filledRound[loop][1] == "Y":
        response[loop] = "Z"
    if filledRound[loop][0] == "C" and filledRound[loop][1] == "Z":
        response[loop] = "X"
    print(response[loop])

    if response[loop] == "X":
        score = score + 1
    if response[loop] == "Y":
        score = score + 2
    if response[loop] == "Z":
        score = score + 3

print(score)



