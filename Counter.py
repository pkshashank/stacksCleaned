import os
# Get the list of all files and directories
import re


path = ".//mathCleaned"
dir_list = os.listdir(path)

outFile1 = open("AllNoMath.txt", "w")


index = 1

for filename in dir_list:
    inFileName = ".//mathCleaned//" + filename
    inFile = open(inFileName, "r")
    for line in inFile:
        if "MATH" in line:
            pass
        elif "CASE" in line:
            pass
        elif "REF" in line:
            pass
        else:
            outFile1.write(line[3:].strip() + "\n")
            index += 1
    inFile.close()

    
outFile1.close()
#print(lexicon)


