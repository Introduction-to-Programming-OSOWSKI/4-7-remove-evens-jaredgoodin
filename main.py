def removeEvens(k):
    newList = k
    numPopped = 0
    for i in range (0, len(k)):
        if newList[i - numPopped] % 2 == 0 and newList[i - numPopped] != 0:
            newList.pop(i - numPopped)
            numPopped = numPopped + 1

    return newList

