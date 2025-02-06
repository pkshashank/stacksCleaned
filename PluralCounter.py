
infile = open("PluralSentences.txt", "r")
outfile = open("plural5grams.txt", "w")

for line in infile:
    # print 5 words to the left of NNS
        words = line.split()
        for word in words:
            if word.endswith("NNS"):
                index = words.index(word)
                # arr = [s.split("_")[0] for s in words]
                arr = words
                if index < 5:
                    outfile.write(" ".join(arr[0:index + 1]) + "\n")
                else:
                    outfile.write(" ".join(arr[index-5:index + 1]) + "\n")
                    
    
outfile.close()
infile.close()

# Convert an array of string to a string
