if firstPass:
    if len(timingFileList) != 0:
        tempTimingFileList = timingFileList
        timingFileList = []
        for timingFile in tempTimingFileList:
            timingFileName = timingFile[0][timingFile[0].rfind("/") + 1:]
            timingFileList += [timingFileName]
        if outputName == []:
            if timingFileList[0][timingFileList[0].rfind("/") + 1:timingFileList[0].find(".txt")].find("HC_") != -1:
                outputName.append(timingFileList[0][timingFileList[0].rfind("_") + 1:timingFileList[0].find(".txt")])
            else:
                outputName.append(timingFileList[0][timingFileList[0].rfind("/") + 1:timingFileList[0].find(".txt")])
    else:
        while True:
            TimingFile = input(
                "Please provide the file path of the timing file you want to add (Hit Enter when Finished):  ")
            TimingFile = TimingFile.strip()
            if len(TimingFile) == 0:
                print("The timing file you want to compile includes:")
                for i in timingFileList:
                    print(i)
                if len(input("Is this correct? ENTER for YES, TYPE ANYTHING else for NO: ")) == 0:
                    break
                else:
                    pass
            else:
                if os.path.isfile(TimingFile):
                    TimingFileName = TimingFile[TimingFile.rfind("/") + 1:]
                    print(TimingFileName + " is a Great Choice")
                    timingFileList.append(TimingFileName)
                else:
                    print("ERROR: " + TimingFile + " is not a correct file path, please try again")
        outputName.append(input("What would you like the output timing file to be named? "))

if secondPass:
    for file in directory:
        if os.path.isfile(file):
            pass
        elif file.find("010") != -1:
            pass
        else:
            while True:
                print("ERROR: " + file + " is not a path for this subject!")
                userInput = input(
                    "Enter subject's proper timing file directory; type QUIT to exit the program; type CONTINUE to continue:")
                if userInput == "QUIT":
                    break
                elif userInput == "CONTINUE":
                    break
                else:
                    file = userInput
                    if os.path.isfile(file):
                        print("Great choice!")
                        break
                    else:
                        pass
    outputFilePath = directory[0][:directory[0].rfind("/")] + "/timingFiles/" + outputName[0] + ".txt"
    print("outputFilePath: " + outputFilePath)
    with open(outputFilePath, 'w') as f:
        f.writelines('\n'.join(timingFileCompiler(directory, mode)))
        f.close
    print("Adding " + outputName[0] + " to subject #" + str(currentSubject[0]) + " out of 124...")
    message = ("#" * currentSubject[0]) + "_" * (124 - currentSubject[0])
    print(message)
    if currentSubject[0] + 1 == 124:
        currentSubject[0] = 0
    else:
        currentSubject[0] += 1
    return outputFilePath

for filename in os.listdir(directory):
    if (filename.find("sub") != -1 and filename.find(".html") == -1):
        if filename.find("_") == -1:
            f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isdir(f):
            if f[f.rfind("/") + 1:] == "func":
                recursiveFolderExplorer(f, mode, firstPass=False, outputName=outputName)
            try:
                int(f[-3:])
                timingFilePaths = []
                for i in timingFileList:
                    a = f + "/func/timingFiles/" + i
                    timingFilePaths.append(f + "/func/" + i)
                recursiveFolderExplorer(timingFilePaths, mode, firstPass=False, secondPass=True, outputName=outputName)
            except:
                pass