import os
# Get the list of all files and directories
import re

path = ".//texRaw"
dir_list = os.listdir(path)



# A function to take a two file names and write all \\begin parts in a file
def writeBegin(inFileName, outFileName):
    inFile = open(inFileName, "r")
    outFile = open(outFileName, "w")

    headers = ['proposition','theorem','lemma', 'definition']

    copyCounter = 0
    for line in inFile:
        if copyCounter == 1:
            outFile.write(line[:-1] + " ")
        for header in headers:
            if line.startswith("\\begin{"+ header +"}"):
                outFile.write(line[:-1] + " ")
                copyCounter = 1
        for header in headers :
            if line.startswith("\\end{"+ header +"}"):
                outFile.write("\n")
                copyCounter = 0
    
    inFile.close()
    outFile.close()


for filename in dir_list:
    inFileName = ".//texRaw//" + filename
    outFileName = ".//textFiles//" + filename[:-4] + ".txt"
    writeBegin(inFileName,outFileName)
    
    
    


