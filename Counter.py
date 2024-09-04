import os
# Get the list of all files and directories
import re

path = ".//mathCleaned"
dir_list = os.listdir(path)
outFile1 = open("All.txt", "w")
outFile2 = open("AllNoMath.txt", "w")

count = 0
for filename in dir_list:
    inFileName = ".//mathCleaned//" + filename
    inFile = open(inFileName, "r")
    for line in inFile:
        outFile1.write(line)
        if "MATH" not in line and "REF" not in line:
            outFile2.write(line)
        if " time." in line or " time " in line or " Time " in line:
            print(line)
            count += 1
    inFile.close()
outFile1.close()
outFile2.close()

print("worked")
print(count)



