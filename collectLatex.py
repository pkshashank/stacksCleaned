import os
path = ".//mathCleaned"
dir_list = os.listdir(path)

setOfLatex = set()

for filename in dir_list:
    inFileName = ".//mathCleaned//" + filename
    inFile = open(inFileName, "r")
    for line in inFile:
        for word in line.split():
            if "\\" in word:
                if word == "resp.\\" or word == "(resp.\\" or word == "w.r.t.\\":
                    pass
                elif word == "e.g.\\" or word == "(e.g.\\" or word == "MATH.\\":
                    pass
                elif word == "i.e.\\" or word == "(eg.\\":
                    pass
                else:
                    setOfLatex.add(word)
            if "MATH``MATH" in word:
                print(filename)
    inFile.close()

print(setOfLatex)
