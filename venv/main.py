# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
ALL HOPE ABANDON YE WHO ENTER HERE...
"""


from FactorialTimingFileCompilerScript import *
from contrastCombinator import *
import itertools
import os
directory = '/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep'
prompt1=input("Type 1 if on Reyna-Lab; Type 2 if one Reyna-Lab-1: ")=="2"
if prompt1:
    baseTimingFiles={"Small":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Small.txt","Large":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Large.txt","Money":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Money.txt","Candy":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Candy.txt","Framing":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Framing.txt", "Gain":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Gain.txt", "Gist":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Gist.txt", "Mixed":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Mixed.txt", "Risk":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Risk.txt", "Loss":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Loss.txt", "NoFraming":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/NoFraming.txt", "Sure":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Sure.txt", "Verbatim":"/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Verbatim.txt"}
else:
    baseTimingFiles={"Small":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Small.txt","Large":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Large.txt","Money":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Money.txt","Candy":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Candy.txt","Framing":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Framing.txt", "Gain":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Gain.txt", "Gist":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Gist.txt", "Mixed":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Mixed.txt", "Risk":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Risk.txt", "Loss":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Loss.txt", "NoFraming":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/NoFraming.txt", "Sure":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Sure.txt", "Verbatim":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/Verbatim.txt"}

    #for i in range(len(baseTimingFiles)):
        #print("---------------------------------")
        #print("starting compiling for: " + baseTimingFiles[i])
        #print("---------------------------------")
        #recursiveFolderExplorer(directory, mode="addition", timingFileList=[baseTimingFiles[i]])
    #Note that reward was excluded and may need to be included in future.
    #addition mode when combining these: ["Verbatim","Mixed","Gist"],["Large", "Small"]]
    #MutuallyExclusiveContrastList=[["Verbatim","Mixed","Gist"],["Gain","Loss"],["Candy","Money"],["Large", "Small"],["Framing","NoFraming"],["Risk","Sure"]]
MutuallyExclusiveContrastList=[["Verbatim","Mixed","Gist","Gain","Loss","Candy","Money","Large", "Small","Framing","NoFraming","Risk","Sure"]]
totalContrastList=contrastCombinator(MutuallyExclusiveContrastList)
print(totalContrastList)
print("Total Combinations: " + str(len(totalContrastList)))
totalContrastListLength=len(totalContrastList)
currentContrastNumber=1


def addingHelper(baseTimingFiles, directory, mode, timingFile1, timingFile2=[], outputName="", totalContrastListLength=0,
                 currentContrastNumber=0, override=False, rewrite=False, prompt1=prompt1):
    print("Starting Compilation of " + outputName + ", contrast #" + str(currentContrastNumber) + " out of " + str(totalContrastListLength) + "...", end='\n')
    print("#" * currentContrastNumber + "_" * (totalContrastListLength - currentContrastNumber)+"\n")
    currentContrastNumber += 1
    if rewrite:
        returnTest = recursiveFolderExplorer(directory, mode=mode, timingFileList=[[timingFile1]],
                                             override=override,
                                             outputName=[outputName], rewrite=True, prompt1=prompt1)
    else:
        returnTest = recursiveFolderExplorer(directory, mode=mode, timingFileList=[[timingFile1], [timingFile2]],
                                             override=override,
                                             outputName=[outputName], rewrite=False, prompt1=prompt1)

    baseTimingFiles[outputName] = returnTest
    return currentContrastNumber

#[Gist,Gain,Risk, Framing, Mixed,Loss,NoFraming,Sure,Verbatim
baseTimingFilesCopyDict={
"Money":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Money.txt",
"Candy":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Candy.txt",
"Small":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Small.txt",
"Large":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Large.txt",
"Verbatim":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_Verbatim.txt",
"Sure":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_Sure.txt",
"NoFraming":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_NoFraming.txt",
"Loss":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_Loss.txt",
"Mixed":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Mixed.txt",
"Framing":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Framing.txt",
"Gist":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Gist.txt",
"Gain":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Gain.txt",
"Risk":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Risk.txt"
}
rewrite = input("Would you like to rewrite copies of base timing files? (y/n): ")=="y"

if rewrite:
    for thing in baseTimingFilesCopyDict.keys():
        outputName=thing
        timingFile1 = baseTimingFilesCopyDict[thing]
        mode="addition"
        addingHelper(baseTimingFiles, directory, mode, timingFile1,
                    totalContrastListLength,outputName=outputName,
                     override=False, rewrite=True, prompt1=prompt1)
else:
    for i in totalContrastList:
        os.system('clear')
        indvContrastList=i.split("_")
        dictList=baseTimingFiles.keys()
        abortRedundantError=False
        if i not in dictList:
            outputName=i
            print("Adding Timing Files for: " + i +"\n")
            #Need to edit this part to switch between overlap and addition modes. If addition mode, need to feed in the right timing file (e.g., "VFraming+MFraming")
            if indvContrastList.count("Mixed") + indvContrastList.count("Gist") + indvContrastList.count("Verbatim") >= 2:
               tempList=[]
               if indvContrastList.count("Mixed") + indvContrastList.count("Gist") + indvContrastList.count("Verbatim")==3:
                   abortRedundantError=True
               else:
                   abortRedundantError=False
                   for j in list(itertools.combinations(indvContrastList, len(indvContrastList)-(indvContrastList.count("Mixed") + indvContrastList.count("Gist") + indvContrastList.count("Verbatim"))+1)):
                       if j.count("Verbatim")+j.count("Mixed")+j.count("Gist")<indvContrastList.count("Mixed") + indvContrastList.count("Gist") + indvContrastList.count("Verbatim"):
                            tempList.append("_".join(j))
                   checker=True
                   breaker=False
                   for j in tempList:
                            if j not in dictList:
                                localOutputName=j
                                print("Adding Timing Files for: " + j +"\n")
                                #reply=input("Continue? (yes/override): ")
                                reply="override"
                                if reply=="yes":
                                    tempSplitting=j.split("_")
                                    timingFile1=baseTimingFiles[tempSplitting[0]]
                                    timingFile2=baseTimingFiles[tempSplitting[1]]
                                    mode="overlap"
                                    if not abortRedundantError:
                                     currentContrastNumber=addingHelper(baseTimingFiles, directory, mode, timingFile1,
                                                                         timingFile2, localOutputName, totalContrastListLength,
                                                                         currentContrastNumber, override=False, rewrite=rewrite, prompt1=prompt1)
                                elif reply=="override":
                                    #This whole mess is to get the total combinations of the name of the file we want
                                    outputNames1 = []
                                    shortenedName = tempList[0]
                                    newinput = shortenedName.split('_')
                                    testing = itertools.permutations(newinput)
                                    for i in list(map(list, testing)):
                                        outputNames1.append('_'.join(i) + ".txt")
                                    outputNames2 = []
                                    shortenedName = tempList[1]
                                    newinput = shortenedName.split('_')
                                    testing = itertools.permutations(newinput)
                                    for i in list(map(list, testing)):
                                        outputNames2.append('_'.join(i) + ".txt")
                                    timingFile1 = ["/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/", outputNames1]
                                    timingFile2 = ["/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/",outputNames2]
                                    if prompt1:
                                        timingFile1=["/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/",outputNames1]
                                        timingFile2=["/System/Volumes/Data/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/timingFiles/",outputNames2]
                                    mode="addition"
                                    if not abortRedundantError:
                                        currentContrastNumber = addingHelper(baseTimingFiles, directory, mode, timingFile1,
                                                                         timingFile2, outputName, totalContrastListLength,
                                                                         currentContrastNumber, override=True, rewrite=rewrite, prompt1=prompt1)
                                    checker=False
                                else:
                                    checker=False
                   if checker:
                        timingFile1=baseTimingFiles[tempList[0]]
                        timingFile2=baseTimingFiles[tempList[1]]
                        mode="addition"
                        if not abortRedundantError:
                            currentContrastNumber = addingHelper(baseTimingFiles, directory, mode, timingFile1,
                                                                         timingFile2, outputName, totalContrastListLength,
                                                                         currentContrastNumber, override=False, rewrite=rewrite, prompt1=prompt1)

            #handles the mode switch from overlap to addition when first making the different framing timing files
            else:
                timingFile1=baseTimingFiles[indvContrastList[0]]
                timingFile2=baseTimingFiles[indvContrastList[1]]
                mode="overlap"
                if not abortRedundantError:
                    currentContrastNumber = addingHelper(baseTimingFiles, directory, mode, timingFile1,
                                                                         timingFile2, outputName, totalContrastListLength,
                                                                         currentContrastNumber, rewrite=rewrite, prompt1=prompt1)
