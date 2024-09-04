infile = open("All.txt", "r")

plurals = set()

for line in infile:
    for word in line.split():
        if word.endswith("s"):
            plurals.add(word)

infile.close()

print(plurals)