import os
# Get the list of all files and directories
import re

path = ".//mathCleaned"
dir_list = os.listdir(path)
outFile1 = open("All.txt", "w")
outFile2 = open("AllNoMath.txt", "w")

for filename in dir_list:
    inFileName = ".//mathCleaned//" + filename
    inFile = open(inFileName, "r")
    for line in inFile:
        outFile1.write(line)
        if "MATH" not in line:
            outFile2.write(line)
    inFile.close()
outFile1.close()
outFile2.close()

propCounter = 0
thmCounter = 0 
lemmaCounter = 0
defCounter = 0
proofCounter = 0
for filename in dir_list:
    inFileName = ".//textFiles//" + filename
    inFile = open(inFileName, "r")
    for line in inFile:
        if line.startswith("\\begin{proposition}"):
            propCounter += 1
        if line.startswith("\\begin{theorem}"):
            thmCounter += 1
        if line.startswith("\\begin{lemma}"):
            lemmaCounter += 1
        if line.startswith("\\begin{definition}"):
            defCounter += 1
        if line.startswith("\\begin{proof}"):
            proofCounter += 1
    inFile.close()

print("Propositions: ", propCounter)
print("Theorems: ", thmCounter)
print("Lemmas: ", lemmaCounter)
print("Definitions: ", defCounter)
print("Proofs: ", proofCounter)



