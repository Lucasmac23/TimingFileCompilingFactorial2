import itertools

outputList=[]
def recursiveContrastCombo(inputList):
    """
    :param inputList:
    :return: recursively constructed output List
    """
    i=0
    j=1
    outputList=[]
    if len(inputList)==2:
        output = withinListContrastCombinations([inputList[i]] + inputList[j:], True)
        outputList += output
    while j<len(inputList):
        outputList=withinListContrastCombinations(inputList, True)
        while i < len(outputList):
            if j < len(inputList)-1:
                output=withinListContrastCombinations([outputList[i]]+inputList[j+1:], True)
                outputList+=output
                j+=1
                i+=1
            else:
                return outputList
    return outputList

def withinListContrastCombinations(inputList, recursiveCall=False):
    """

    :param inputList: 1d List of strings
    :param recursiveCall: Boolean to check if this function is called using the recursive helper function
    :return: returns a list with all possible combinations of the given list (e.g., if input was ["a","b","c"]
            output would be ["a_b", "a_b_c", "a_c", "b_c"]
    """
    i = 0
    j=1
    outputList=[]
    if recursiveCall:
        k=j
        while k<len(inputList):
            outputList.append("_".join([inputList[i]] + [inputList[k]]))
            k+=1
    else:
        while i < len(inputList)-1:
            k = j
            while k < len(inputList):
                outputList.append("_".join([inputList[i]] + [inputList[k]]))
                if k+1!=len(inputList) and recursiveCall==False:
                    output1=recursiveContrastCombo([outputList[-1]]+inputList[k+1:])
                    output2=[]
                    for thing in output1:
                        output2+=recursiveContrastCombo([thing]+inputList[k+2:])
                    outputList+=output1
                    outputList+=output2

                k += 1
            i += 1
            j+=1
    return outputList

def contrastCombinator(inputList):
    outputList=[]
    i=0
    while i < len(inputList):
        feedList=inputList[i]
        outputList+=withinListContrastCombinations(feedList)
        outputList.append("_".join(inputList[0]))
        i+=1

    filteredOutputList=filterContrasts(outputList)
    #print(outputList)
    #print("Total Combinations: " + str(len(outputList)))
    return(filteredOutputList)


# MutuallyExclusiveContrastList=[["Verbatim","Mixed","Gist"],["Gain","Loss"],["Candy","Money"],["Large", "Small"],["Framing","NoFraming"],["Risk","Sure"]]


def filterContrasts(inputList):
    MutuallyExclusiveContrastsList = [["Gain", "Loss"], ["Candy", "Money"], ["Framing", "NoFraming"], ["Risk", "Sure"]]
    #MutuallyExclusiveContrastsList = [["Verbatim", "Mixed", "Gist"], ["Gain", "Loss"], ["Candy", "Money"], ["Large", "Small"], ["Framing", "NoFraming"], ["Risk", "Sure"]]
    outputList=[]
    i=0
    orderedList = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    while i<len(inputList):
        tempList=inputList[i].split("_")
        #13
        addCheck=True
        for j in MutuallyExclusiveContrastsList:
            if j[0] in tempList:
                if j[1] in tempList:
                    addCheck = False
        for item in tempList:
            if len(tempList)>3:
                if tempList.count(item)>1:
                    addCheck=False
        if orderedList[(len(tempList)-1)].count(inputList[i])!=0:
            addCheck=False
        if addCheck:
            if outputList.count(inputList[i])==0:
                orderedList[(len(tempList)-1)].append(inputList[i])
        i+=1

    #print(orderedList)
    finalTemp=list(itertools.chain.from_iterable(orderedList))
    return finalTemp
   #might need to revert
#new_foods = [time for sublist in orderedList for time in sublist]

    return orderedList



