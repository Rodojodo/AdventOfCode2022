file = open("input.txt")
text = file.read()



def getPriority(letter):
        if ord(letter) < 95:
            return ord(letter) - 38
            
        else:
            return ord(letter) - 96

def getMatch(compartment1, compartment2):
    # print(compartment1, compartment2)
    for firstItem in range(0, len(compartment1)):
            for secondItems in range(0, len(compartment1)):
                        if compartment1[firstItem] == compartment2[secondItems]:
                            return compartment2[secondItems]


person = text.split("\n")
peopleCompartment1 = [""]*300
peopleCompartment2 = [""]*300
x = 0

for eachBag in range(0, len(person)):
    peopleCompartment1[eachBag], peopleCompartment2[eachBag] = person[eachBag][:len(person[eachBag])//2], person[eachBag][len(person[eachBag])//2:]
    firstCompartment = peopleCompartment1[eachBag]
    secondCompartment = peopleCompartment2[eachBag]
    matchLetter = getMatch(list(firstCompartment),list(secondCompartment))
    x = x + getPriority(matchLetter)




print(x)
        
        




