file = open("input.txt")
text = file.read()
pairs = text.split("\n")

def splitByCouple(pairs):
    splitPair = [""]*len(pairs)
    for couple in range(0,len(pairs)):
        splitPair[couple] = pairs[couple].split("-")
    return splitPair

def splitByElf(splitPair):

    please1 = [[[]]]*len(splitPair)
    please2 = [[[]]]*len(splitPair)
    for couple in range(0,len(splitPair)):
        please1[couple] = splitPair[couple][0].split(",")
        please2[couple] = splitPair[couple][1].split(",")
    return please1,please2


def numberCheck(splitPair, individualNum):
    # print(splitPair, "\n", individualNum)
    numberOfOverlaps = 0
    for couple in range(0,len(splitPair)):
        if int(individualNum[0][couple][1]) >= int(individualNum[1][couple][0]) and int(individualNum[0][couple][1]) <= int(individualNum[1][couple][1]):
            numberOfOverlaps = numberOfOverlaps + 1
        elif (int(individualNum[0][couple][0]) <= int(individualNum[1][couple][1]) and int(individualNum[0][couple][0]) >= int(individualNum[1][couple][0])):
            numberOfOverlaps = numberOfOverlaps + 1
        elif (int(individualNum[1][couple][0]) <= int(individualNum[0][couple][1]) and int(individualNum[1][couple][0]) >= int(individualNum[0][couple][0])):
            numberOfOverlaps = numberOfOverlaps + 1
        elif (int(individualNum[1][couple][1]) <= int(individualNum[0][couple][1]) and int(individualNum[1][couple][0]) >= int(individualNum[0][couple][0])):
            numberOfOverlaps = numberOfOverlaps + 1
    return numberOfOverlaps


splitPair = splitByCouple(pairs)
splitElf = splitByElf(splitPair)
x =  numberCheck(splitPair, splitElf)
print(x)