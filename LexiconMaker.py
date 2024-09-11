
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
            setPOS.add(tag + " " + lexeme.lower())
            if tag == "CC":
                Conjunctions.add(lexeme.lower())
            elif tag == "CD":
                CardinalNumbers.add(lexeme.lower())
            elif tag == "DT":
                Determiners.add(lexeme.lower())
            elif tag == "FW":
                ForeignWords.add(lexeme.lower())
            elif tag == "IN":
                Prepositions.add(lexeme.lower())
            elif tag == "JJ" or tag == "JJR" or tag == "JJS":
                Adjectives.add(lexeme.lower())
            elif tag == "MD":
                Modals.add(lexeme.lower())
            elif tag == "NN" or tag == "NNS" or tag == "NNP" or tag == "NNPS":
                Nouns.add(lexeme.lower())
            elif tag == "PDT":
                Predeterminers.add(lexeme.lower())
            elif tag == "PRP" or tag == "PRP$":
                Pronouns.add(lexeme.lower())
            elif tag == "RB" or tag == "RBR" or tag == "RBS":
                Adverbs.add(lexeme.lower())
            elif tag == "VB" or tag == "VBD" or tag == "VBG" or tag == "VBN" or tag == "VBP" or tag == "VBZ":
                Verbs.add(lexeme.lower())
    infile.close()
    outfile.write("Total Words: " + str(len(setPOS)) + "\n")
    outfile.write("Conjunctions (CC): " + str(len(Conjunctions)) + "\n")
    outfile.write("Cardinal Numbers (CD): " + str(len(CardinalNumbers)) + "\n")
    outfile.write("Determiners (DT): " + str(len(Determiners)) + "\n")
    outfile.write("Foreign Words (FW): " + str(len(ForeignWords)) + "\n")
    outfile.write("Prepositions (IN): " + str(len(Prepositions)) + "\n")
    outfile.write("Adjectives (JJ, JJR, JJS): " + str(len(Adjectives)) + "\n")
    outfile.write("Modals (MD): " + str(len(Modals)) + "\n")
    outfile.write("Nouns (NN, NNS, NNP, NNPS): " + str(len(Nouns)) + "\n")
    outfile.write("Predeterminers (PDT): " + str(len(Predeterminers)) + "\n")
    outfile.write("Pronouns (PRP, PRP$): " + str(len(Pronouns)) + "\n")
    outfile.write("Adverbs (RB, RBR, RBS): " + str(len(Adverbs)) + "\n")
    outfile.write("Verbs (VB, VBD, VBG, VBN, VBP, VBZ): " + str(len(Verbs)) + "\n\n")
    
    outfile.write("Lexicon: \n")
    for elements in setPOS:
        toWrite.append(elements + "\n")
    toWrite.sort()
    outfile.writelines(toWrite)
    outfile.close()


POSFinder("AllNoTags.pos","Lexicon.txt")


