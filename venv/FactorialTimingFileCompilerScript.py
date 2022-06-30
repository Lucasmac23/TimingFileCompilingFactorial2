import os
# assign directory

import openpyxl
from openpyxl import load_workbook
directory = '/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep'
CWD=input("What is your pwd? (You can get this by talking pwd into terminal): ").strip()
# iterate over files in
# that directory
if CWD.count('venv')==0:
    CWD=CWD+"/venv"
timingFileList=[]
outputName=[]
outputExcelPath=CWD+'/TotalTimingFileList'

#load excel file
workbook = load_workbook(filename=CWD+'/TotalTimingFileListTemplate.xlsx')
#open workbook
sheet = workbook.active
def addToExcel(location, content):
    #modify the desired cell
    sheet[location].value = content
#v,m,g
#Gain, Loss
#candy, money
#Large, Medium, Small
#50, 60, 67,
#if from the same sublist, add files. If from others, take overlap.
#[[v,m,g],[gain,loss],[candy,money],[Large, Medium, Small], [50,60,67]?]

#Interesting Contrasts
#Gframing vs VNoframing
#VFraming vs GNoFraming

#   Framing, NoFraming
#   Risk, Sure



#actually making the new timing file
def numberOverlap(d1, d2):
    #returns a new list that contains the matches of d1 and d2. Returns "\n" empty string if no matches
    i=0
    j=0
    d3=[]
    if d2[0]=="*" or d1[0]=="*":
        d3.append("*")
        return d3
    else:
        while True:
            if i+1==len(d1):
                while j<len(d2):
                    if d1[i]==d2[j]:
                        d3+=[str(d1[i])]
                        j+=1
                    else:
                        j+=1
                break
            elif j+1==len(d2):
                while i<len(d1):
                    if d1[i]==d2[j]:
                        d3+=[str(d1[i])]
                        i+=1
                    else:
                        i+=1
                break
            elif float(d1[i])==float(d2[j]):
                d3+=[str(d1[i])]
                i+=1
                j+=1
            elif float(d2[j])>float(d1[i]):
                i+=1
            elif float(d1[i])>float(d2[j]):
                j+=1
    if len(d3)==0:
        d3.append("*")
    return d3
def numberAdder(d1, d2, rewrite=False):
    if rewrite:
        d3=d1+d2
        return list(map(str,d3))
    else:
        d3=[]
        d3=d1+d2
        d3=sorted(list(map(float, d3)))
    return list(map(str,d3))

def timingFileCompiler(filesList, mode, rewrite):
    """def: splits up the files in filelist into lines and then makes a list containing each number in each line.
        parameters: filesList=list of the paths to the timing files needed to be compiled
                    mode = ("overlap" -> taking the overlap of the timing files (where they have the same numbers)
                            "addition" -> adding the timing files together based on mutual exclusive contrasts
                    output = list of the lines in the compiled output timing file
    """
    tempFileList=[]
    if len(filesList)>1:
        file1=filesList[0]
        file2=filesList[1]
        with open(file1) as f1:
            lines1 = f1.readlines()
        with open(file2) as f2:
            lines2 = f2.readlines()
        for i in range(4):
            splitlines1=(lines1[i].split())
            splitlines2=(lines2[i].split())
            if mode=="overlap":
                tempFileList.append(numberOverlap(splitlines1, splitlines2))
            elif mode=="addition":
                if "*" in splitlines2 and "*" in splitlines1:
                    rewrite=True
                elif "*" in splitlines2:
                    splitlines2=[]
                elif "*" in splitlines1:
                    splitlines1=[]
                tempFileList.append(numberAdder(splitlines1,splitlines2,rewrite))
        for num in range(len(tempFileList)):
            tempFileList[num]=" ".join(tempFileList[num])
        return tempFileList
    else:
        file=filesList[0]
        with open(file) as f1:
            lines1 = f1.readlines()
        for i in range(4):
            splitlines1 = (lines1[i].split())
            tempFileList.append(numberAdder(splitlines1, [], rewrite))
        for num in range(len(tempFileList)):
            tempFileList[num] = " ".join(tempFileList[num])
        return tempFileList

        #At end, have to change filesList[0] to the compiled timing file

#recursively Iterate through directory to get individual subject timing files in timing File List
def recursiveFolderExplorer(directory, mode, timingFileList=[], outputName=[], rewrite=False, override=False, prompt1=False, currentExcelLine=1, newExcelNumber=2, workbook=workbook, sheet=sheet):
    if currentExcelLine==2:
        workbook = load_workbook(filename=CWD + '/TotalTimingFileListTemplate.xlsx')
        sheet = workbook.active


    SubjList = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '011', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '027', '028', '029', '030', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '113', '114', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132']
    if prompt1:
        directory='/Volumes/Reyna-Lab-1/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep'
    else:
        directory='/Volumes/Reyna-Lab/Lab/HotCold/Databases/HC_1stHalfFunctional/Output/fmriprep'
    for SubjNum in SubjList:
        localCount = 0
        addToExcel('A'+str(currentExcelLine), outputName[0])
        addToExcel('B' + str(currentExcelLine), 'sub-'+SubjNum)
        outputFilePath=directory+"/sub-"+ SubjNum +"/func/timingFiles/"+outputName[0]+".txt"
        #print("outputFilePath: "+outputFilePath)
        subjTimingFileList=[]
        if not rewrite:
            if override:
                fileExists=False
                while not fileExists:
                    for n in timingFileList[0][0][1]:
                        tempPath=timingFileList[0][0][0][:timingFileList[0][0][0].rfind("fmriprep/")] + "fmriprep/sub-"+SubjNum+"/func/timingFiles/" + n
                        fileExists=os.path.exists(tempPath)
                        if fileExists:
                            subjTimingFileList.append(timingFileList[0][0][0][:timingFileList[0][0][0].rfind("fmriprep/")] + "fmriprep/sub-"+SubjNum+"/func/timingFiles/" + n)
                            break
                    if not fileExists:
                        input("error found on timingFileList[0]")
                fileExists=False
                while not fileExists:
                    for n in timingFileList[1][0][1]:
                        tempPath = timingFileList[1][0][0][:timingFileList[1][0][0].rfind("fmriprep/")] + "fmriprep/sub-" + SubjNum + "/func/timingFiles/" + n
                        fileExists = os.path.exists(tempPath)
                        if fileExists:
                            subjTimingFileList.append(timingFileList[1][0][0][:timingFileList[1][0][0].rfind("fmriprep/")] + "fmriprep/sub-" + SubjNum + "/func/timingFiles/" + n)
                            break
                    if not fileExists:
                        input("error found on timingFileList[1]")
            else:
                for a in timingFileList:
                    for item in a:
                        subjTimingFileList.append(item[:item.rfind('-')+1]+SubjNum+'/func/timingFiles'+item[item.rfind('/'):])
        else:
            for i in timingFileList:
                subjTimingFileList.append(i[0][:i[0].rfind("fmriprep/")] + "fmriprep/sub-"+SubjNum+"/func/" + i[0][i[0].rfind("/"):])
        print("\rAdding to subject #" + str(SubjNum) + " out of 132:"+"#" * int(SubjNum) + "_" * (len(SubjList) - int(SubjNum)), end='')
        with open(outputFilePath, 'w') as f:
            returnedFileLines=timingFileCompiler(subjTimingFileList, mode, rewrite)
            for line in returnedFileLines:
                for number in line:
                    localCount+=1
            fileContents=('\n'.join(returnedFileLines))
            if fileContents=='':
                input("ERROR----timingFile Script Writing Empty File")
            f.writelines(fileContents)
            f.close
        addToExcel('C' + str(currentExcelLine), str(localCount))
        currentExcelLine+=1
    workbook.save(outputExcelPath+str(newExcelNumber)+".xlsx")
    return outputFilePath
