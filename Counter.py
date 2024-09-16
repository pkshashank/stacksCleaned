import os
# Get the list of all files and directories
import re


path = ".//mathCleaned"
dir_list = os.listdir(path)

outFile1 = open("AllDefs.txt", "w")


index = 1

for filename in dir_list:
    inFileName = ".//mathCleaned//" + filename
    inFile = open(inFileName, "r")
    for line in inFile:
        if line.startswith("DEF"):
            outFile1.write(line[4:].strip() + "\n")
    inFile.close()

    
outFile1.close()
#print(lexicon)


