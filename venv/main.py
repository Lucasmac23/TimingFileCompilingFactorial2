# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from FactorialTimingFileCompilerScript import *
from contrastCombinator import *
import itertools
directory = '/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep'
baseTimingFiles={"Small":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Small.txt","Large":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Large.txt","Money":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Money.txt","Candy":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/Candy.txt","Framing":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Framing.txt", "Gain":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Gain.txt", "Gist":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Gist.txt", "Mixed":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Mixed.txt", "Risk":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_01_Risk.txt", "Loss":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_Loss.txt", "NoFraming":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_NoFraming.txt", "Sure":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_Sure.txt", "Verbatim":"/System/Volumes/Data/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep/sub-001/func/HC_02_Verbatim.txt"}


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
for i in totalContrastList:
    indvContrastList=i.split("_")
    dictList=baseTimingFiles.keys()
    if i not in dictList:
        outputName=i
        print("-------------------------------")
        print("Adding Timing Files for: " + i)
        print("-------------------------------")
        #Need to edit this part to switch between overlap and addition modes. If addition mode, need to feed in the right timing file (e.g., "VFraming+MFraming")
        if indvContrastList.count("Mixed") + indvContrastList.count("Gist") + indvContrastList.count("Verbatim") >= 2:
           tempList=[]
           for j in list(itertools.combinations(indvContrastList, len(indvContrastList)-(indvContrastList.count("Mixed") + indvContrastList.count("Gist") + indvContrastList.count("Verbatim"))+1)):
               if j.count("Verbatim")+j.count("Mixed")+j.count("Gist")<indvContrastList.count("Mixed") + indvContrastList.count("Gist") + indvContrastList.count("Verbatim"):
                    tempList.append("_".join(j))
           checker=True
           for j in tempList:
                    if j not in dictList:
                        print("Adding Timing Files for: " + j)
                        checker=False
                        input("Continue?")
           if checker:
                    timingFile1=baseTimingFiles[tempList[0]]
                    timingFile2=baseTimingFiles[tempList[1]]
                    mode="addition"

        #handles the mode switch from overlap to addition when first making the different framing timing files
        else:
            timingFile1=baseTimingFiles[indvContrastList[0]]
            timingFile2=baseTimingFiles[indvContrastList[1]]
            mode="overlap"
        print("***************************************")
        print("Starting Compilation of " + outputName + ", contrast #" + str(currentContrastNumber) + " out of " + str(
            totalContrastListLength) + "...")
        print("#" * currentContrastNumber + "_" * (totalContrastListLength - currentContrastNumber))
        print("***************************************")
        baseTimingFiles[i]:recursiveFolderExplorer(directory, mode=mode, timingFileList=[[timingFile1],[timingFile2]], outputName=[outputName])

        currentContrastNumber+=1






