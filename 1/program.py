file = open("input.txt")
text = file.read()
splitByGroup = text.split("\n\n")


splitByLine = [0] * 3000
totalCal = [0] * len(splitByGroup)

for loop in range(0,len(splitByGroup)):
    splitByLine[loop] = splitByGroup[loop].split("\n")

for counter in range(0,len(splitByGroup)):
    x = 0
    for loop in range(0,len(splitByLine[counter])):
        x = x + int(splitByLine[counter][loop])
    totalCal[counter] = x

biggestCal = max(totalCal)
totalCal.remove(biggestCal)
secondBiggestCal = max(totalCal)
totalCal.remove(secondBiggestCal)
thirdBiggestCal = max(totalCal)
totalBigCal = biggestCal + secondBiggestCal + thirdBiggestCal
print(totalBigCal)




