file = open("input.txt")
text = file.read()
characterArray = list(text)


def findBuffer(character):

    for loop in range(0,len(character)):
        for counter in range(0,len(character)):
            if character[counter] != character[counter + 1] and character[counter] != character[counter + 2] and character[counter] != character[counter + 3] and character[counter] != character[counter + 4] and character[counter] != character[counter + 5] and character[counter] != character[counter + 6] and character[counter] != character[counter + 7] and character[counter] != character[counter + 8] and character[counter] != character[counter + 9] and character[counter] != character[counter + 10] and character[counter] != character[counter + 11] and character[counter] != character[counter + 12] and character[counter] != character[counter + 13]:
                if character[counter+1] != character[counter + 2] and character[counter+1] != character[counter + 3] and character[counter+1] != character[counter + 4] and character[counter+1] != character[counter + 5] and character[counter+1] != character[counter + 6] and character[counter+1] != character[counter + 7] and character[counter+1] != character[counter + 8] and character[counter+1] != character[counter + 9] and character[counter+1] != character[counter + 10] and character[counter+1] != character[counter + 11] and character[counter+1] != character[counter + 12] and character[counter+1] != character[counter + 13]:
                    if character[counter+2] != character[counter + 3] and character[counter+2] != character[counter + 4] and character[counter+2] != character[counter + 5] and character[counter+2] != character[counter + 6] and character[counter+2] != character[counter + 7] and character[counter+2] != character[counter + 8] and character[counter+2] != character[counter + 9] and character[counter+2] != character[counter + 10] and character[counter+2] != character[counter + 11] and character[counter+2] != character[counter + 12] and character[counter+2] != character[counter + 13]:
                        if character[counter+3] != character[counter + 4] and character[counter+3] != character[counter + 5] and character[counter+3] != character[counter + 6] and character[counter+3] != character[counter + 7] and character[counter+3] != character[counter + 8] and character[counter+3] != character[counter + 9] and character[counter+3] != character[counter + 10] and character[counter+3] != character[counter + 11] and character[counter+3] != character[counter + 12] and character[counter+3] != character[counter + 13]:
                            if character[counter+4] != character[counter + 5] and character[counter+4] != character[counter + 6] and character[counter+4] != character[counter + 7] and character[counter+4] != character[counter + 8] and character[counter+4] != character[counter + 9] and character[counter+4] != character[counter + 10] and character[counter+4] != character[counter + 11] and character[counter+4] != character[counter + 12] and character[counter+4] != character[counter + 13]:
                                if character[counter+5] != character[counter + 6] and character[counter+5] != character[counter + 7] and character[counter+5] != character[counter + 8] and character[counter+5] != character[counter + 9] and character[counter+5] != character[counter + 10] and character[counter+5] != character[counter + 11] and character[counter+5] != character[counter + 12] and character[counter+5] != character[counter + 13]:
                                    if character[counter+6] != character[counter + 7] and character[counter+6] != character[counter + 8] and character[counter+6] != character[counter + 9] and character[counter+6] != character[counter + 10] and character[counter+6] != character[counter + 11] and character[counter+6] != character[counter + 12] and character[counter+6] != character[counter + 13]:
                                        if character[counter+7] != character[counter + 8] and character[counter+7] != character[counter + 9] and character[counter+7] != character[counter + 10] and character[counter+7] != character[counter + 11] and character[counter+7] != character[counter + 12] and character[counter+7] != character[counter + 13]:
                                            if character[counter+8] != character[counter + 9] and character[counter+8] != character[counter + 10] and character[counter+8] != character[counter + 11] and character[counter+8] != character[counter + 12] and character[counter+8] != character[counter + 13]:
                                                if character[counter+9] != character[counter + 10] and character[counter+9] != character[counter + 11] and character[counter+9] != character[counter + 12] and character[counter+9] != character[counter + 13]:
                                                    if character[counter+10] != character[counter + 11] and character[counter+10] != character[counter + 12] and character[counter+1] != character[counter + 13]:
                                                        if character[counter+11] != character[counter + 12] and character[counter+11] != character[counter + 13]:
                                                            if character[counter+12] != character[counter + 13]:
                                                                print(counter+14)
                                                                return counter+14







                
print(findBuffer(characterArray))






# bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw