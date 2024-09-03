import re

inFile = open("test.txt", "r")

# Function to put everything between strBeg and strEnd 
def deleteStrings(strBeg, strEnd, str):
    if strBeg not in str:
        return str
    else:
        begIndex = str.find(strBeg)
        endIndex = str[begIndex:].find(strEnd) + begIndex
        head = str[:begIndex]
        return head + str[begIndex + len(strBeg):endIndex] + deleteStrings(strBeg, strEnd, str[endIndex + len(strEnd):])

# Function to put everything between \begin{equation} and \end{equation} as MATH
def replaceStrings(strBeg, strEnd, str, strReplace):
    if strBeg not in str:
        return str
    else:
        begIndex = str.find(strBeg)
        endIndex = str[begIndex:].find(strEnd) + begIndex
        head = str[:begIndex]
        return head + strReplace + replaceStrings(strBeg, strEnd, str[endIndex + len(strEnd):], strReplace)

for line in inFile:
    line = deleteStrings("$", "$", line)
    print(line)

inFile.close()