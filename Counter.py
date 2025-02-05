import os
# Get the list of all files and directories
import re


def deleteStrings(strBeg, strEnd, str):
    
    if strBeg not in str:
        return str
    else:
        begIndex = str.find(strBeg)
        endIndex = str[begIndex:].find(strEnd) + begIndex
        head = str[:begIndex]
        return head + str[begIndex + len(strBeg):endIndex] + deleteStrings(strBeg, strEnd, str[endIndex + len(strEnd):])

def replaceStrings(strBeg, strEnd, str, strReplace):
    if strBeg not in str:
        return str
    else:
        begIndex = str.find(strBeg)
        endIndex = str[begIndex:].find(strEnd) + begIndex
        head = str[:begIndex]
        return head + strReplace + replaceStrings(strBeg, strEnd, str[endIndex + len(strEnd):], strReplace)
    

path = ".//textFiles"
dir_list = os.listdir(path)

outFile1 = open("AllDefs.tex", "w")


index = 1

for filename in dir_list:
    inFileName = ".//textFiles//" + filename
    inFile = open(inFileName, "r")
    for line in inFile:
        if line.startswith("\\begin{definition}"):
            line = deleteStrings("\\begin{definition}", "\\end{definition}", line)
            line = replaceStrings("\\label{", "}", line, "")
            outFile1.write(line)
    inFile.close()

    
outFile1.close()
#print(lexicon)


