
def POSFinder(infileName,outfileName):
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    toWrite = []
    setPOS = set()
    for line in infile:
        for word in line.split():
            index = word.find("_")
            tag = word[index+1:]
            lexeme = word[:index]
            setPOS.add(tag + " " + lexeme)
    infile.close()
    for elements in setPOS:
        toWrite.append(elements + "\n")
    toWrite.sort()
    outfile.writelines(toWrite)
    outfile.close()


POSFinder("AllNoMath.pos","Lexicon.txt")


