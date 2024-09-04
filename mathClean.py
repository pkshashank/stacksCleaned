import os
import re

path = ".//textFiles"
dir_list = os.listdir(path)

def replaceStrings(strBeg, strEnd, str, strReplace):
    if strBeg not in str:
        return str
    else:
        begIndex = str.find(strBeg)
        endIndex = str[begIndex:].find(strEnd) + begIndex
        head = str[:begIndex]
        return head + strReplace + replaceStrings(strBeg, strEnd, str[endIndex + len(strEnd):], strReplace)
    
def deleteStrings(strBeg, strEnd, str):
    if strBeg not in str:
        return str
    else:
        begIndex = str.find(strBeg)
        endIndex = str[begIndex:].find(strEnd) + begIndex
        head = str[:begIndex]
        return head + str[begIndex + len(strBeg):endIndex] + deleteStrings(strBeg, strEnd, str[endIndex + len(strEnd):])

# Cleans all math
def mathCleaner(inFileName,outFileName):
    inFile = open(inFileName, "r")
    outFile = open(outFileName, "w")
    for line in inFile:
        line = re.sub("\$\$.*?\$\$", "MATH", line) 
        line = re.sub("\$.*?\$", "MATH", line) 
        line = re.sub("\\\label{.*?}", "", line) 
        line = re.sub("\\\cite{.*?}", "REF", line)
        line = re.sub("\\\href{.*?}{.*?}", "REF", line)
        

        line = line.replace("\\begin{enumerate}","<CASES>")
        line = line.replace("\\begin{itemize}","<CASES>")
        line = line.replace("\\end{enumerate}","</CASES>")
        line = line.replace("\\end{itemize}","</CASES>")
        line = line.replace("\\setcounter{enumi}{6}","")
        line = re.sub("\\\item", "CASE:", line) 
        line = re.sub("CASE:\[.*?\]","CASE:", line)
        line = replaceStrings("(\\romannumeral", ")", line, "CASE:")
        
        line = line.replace("\\begin{slogan}","[")
        line = line.replace("\\end{slogan}","]")

        line = replaceStrings("\\begin{equation}", "\\end{equation}", line, "MATH")
        line = replaceStrings("\\begin{reference}", "\\end{reference}", line, "REF")
        line = replaceStrings("\\begin{align*}", "\\end{align*}", line, "MATH")
        line = replaceStrings("\\begin{eqnarray*}", "\\end{eqnarray*}", line, "MATH")
        line = replaceStrings("\\begin{history}", "\\end{history}", line, "")
        line = replaceStrings("\\begin{matrix}", "\\end{matrix}", line, "MATH")
        line = replaceStrings("\\ref{", "}", line, "REF")
        line = replaceStrings("\\cite[","}", line, "REF")
        line = replaceStrings("\\footnote{", "}", line, "")
        

        line = deleteStrings("{\\it ", "}", line)
        line = deleteStrings("\\emph{", "}", line)
        line = deleteStrings("{\\bf", "}", line)
        
        line = re.sub("\\\end{.*?}", "", line)
        line = line.replace("\\begin{lemma}", "LEM\t")
        line = line.replace("\\begin{definition}", "DEF\t")
        line = line.replace("\\begin{theorem}", "THM\t")
        line = line.replace("\\begin{proposition}", "PRP\t")


        line = line.replace("\\'e", "e") # for etale
        line = line.replace("\\'E", "E") # for Etale
        line = line.replace("\\\"a", "a") # for K\\"ahler
        line = line.replace("\\`e", "e") # for Crit\\`ere`
        line = line.replace("\\\'a", "a") # for Kov\\'acs
        line = line.replace("\\\"o", "o") # for Jotrdan-H\\"older"
        line = line.replace("\\\"u", "u") # for K\\"unneth
        line = deleteStrings("{\\v ", "}", line) # for {\\v C}ech (the caron symbol)

        outFile.write(line)


for filename in dir_list:
    inFileName = ".//textFiles//" + filename
    outFileName = ".//mathCleaned//" + filename[:-4] + ".txt"
    mathCleaner(inFileName,outFileName)
