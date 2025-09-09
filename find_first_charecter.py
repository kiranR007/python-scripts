def  countNonRepeating(inputstr):
    resSeen =[]
    resUnseen = []
    for ele in inputstr:
        if ele in resUnseen:
            resSeen.append(ele)
            resUnseen.remove(ele)
        elif resSeen:
            continue
        else:
            resUnseen.append(ele)
    if resUnseen:
        return inputstr.find(resUnseen[0])
    else:
        return -1
print(countNonRepeating(input()))