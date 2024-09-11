
def POSFinder(infileName,outfileName):
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    Conjunctions = set()
    CardinalNumbers = set()
    Determiners = set()
    ForeignWords = set()
    Prepositions = set()
    Adjectives = set()
    Modals = set()
    Nouns = set()
    Predeterminers = set()
    Pronouns = set()
    Adverbs = set()
    Verbs = set()
    toWrite = []
    setPOS = set()
    for line in infile:
        for word in line.split():
            index = word.find("_")
            tag = word[index+1:]
            lexeme = word[:index]
            setPOS.add(tag + " " + lexeme)
            if tag == "CC":
                Conjunctions.add(lexeme)
            elif tag == "CD":
                CardinalNumbers.add(lexeme)
            elif tag == "DT":
                Determiners.add(lexeme)
            elif tag == "FW":
                ForeignWords.add(lexeme)
            elif tag == "IN":
                Prepositions.add(lexeme)
            elif tag == "JJ" or tag == "JJR" or tag == "JJS":
                Adjectives.add(lexeme)
            elif tag == "MD":
                Modals.add(lexeme)
            elif tag == "NN" or tag == "NNS" or tag == "NNP" or tag == "NNPS":
                Nouns.add(lexeme)
            elif tag == "PDT":
                Predeterminers.add(lexeme)
            elif tag == "PRP" or tag == "PRP$":
                Pronouns.add(lexeme)
            elif tag == "RB" or tag == "RBR" or tag == "RBS":
                Adverbs.add(lexeme)
            elif tag == "VB" or tag == "VBD" or tag == "VBG" or tag == "VBN" or tag == "VBP" or tag == "VBZ":
                Verbs.add(lexeme)
    infile.close()
    outfile.write("Conjunctions: " + str(len(Conjunctions)) + "\n")
    outfile.write("Cardinal Numbers: " + str(len(CardinalNumbers)) + "\n")
    outfile.write("Determiners: " + str(len(Determiners)) + "\n")
    outfile.write("Foreign Words: " + str(len(ForeignWords)) + "\n")
    outfile.write("Prepositions: " + str(len(Prepositions)) + "\n")
    outfile.write("Adjectives: " + str(len(Adjectives)) + "\n")
    outfile.write("Modals: " + str(len(Modals)) + "\n")
    outfile.write("Nouns: " + str(len(Nouns)) + "\n")
    outfile.write("Predeterminers: " + str(len(Predeterminers)) + "\n")
    outfile.write("Pronouns: " + str(len(Pronouns)) + "\n")
    outfile.write("Adverbs: " + str(len(Adverbs)) + "\n")
    outfile.write("Verbs: " + str(len(Verbs)) + "\n\n\n")
    for elements in setPOS:
        toWrite.append(elements + "\n")
    toWrite.sort()
    outfile.writelines(toWrite)
    outfile.close()


POSFinder("AllNoTags.pos","Lexicon.txt")


