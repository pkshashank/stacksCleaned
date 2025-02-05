# Read from AllPosCleaned.txt and count the how many sentences have a plural occurence

infile = open("AllPosCleaned.txt", "r")
outfile = open("PluralSentences.txt", "w")

totalSentences = 0
pluralSentences = 0

for line in infile:
    totalSentences += 1
    if "NNS" in line or "NNPS" in line:
        pluralSentences += 1
        outfile.write(line)

        
print("Total Sentences: ", totalSentences)
print("Plural Sentences: ", pluralSentences)
print ("Percentage of Plural Sentences: ", (pluralSentences/totalSentences)*100)

infile.close()
outfile.close()