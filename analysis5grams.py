#Read from plural5grams.txt
infile = open('plural5grams.txt', 'r')


cdCount = 0
dtCount = 0
inCount = 0
ccCount = 0
noneCount = 0


cdList = {}
dtList = {}
inList = {}
ccList = {}

for line in infile:
    if "_CD" not in line and "_DT" not in line and "_IN" not in line and "_CC" not in line:
        noneCount += 1

    words = line.split()
    for word in words:
        if word.endswith("_CD"):
            cdCount += 1
            cdList[word.split("_")[0].lower()] = cdList.get(word.split("_")[0].lower(), 0) + 1
        elif word.endswith("_DT"):
            dtCount += 1
            dtList[word.split("_")[0].lower()] = dtList.get(word.split("_")[0].lower(), 0) + 1
        elif word.endswith("_IN"):
            inCount += 1
            inList[word.split("_")[0].lower()] = inList.get(word.split("_")[0].lower(), 0) + 1
        elif word.endswith("_CC"):
            ccCount += 1
            ccList[word.split("_")[0].lower()] = ccList.get(word.split("_")[0].lower(), 0) + 1
        

print("CD: ", cdCount)
print("DT: ", dtCount)
print("IN: ", inCount)
print("CC: ", ccCount)
print("#Lines with none of these:", noneCount)

sorted_cdList = sorted(cdList.items(), key=lambda x: x[1], reverse=True)
sorted_dtList = sorted(dtList.items(), key=lambda x: x[1], reverse=True)
sorted_inList = sorted(inList.items(), key=lambda x: x[1], reverse=True)
sorted_ccList = sorted(ccList.items(), key=lambda x: x[1], reverse=True)

print("CD: ", sorted_cdList)
print("DT: ", sorted_dtList)
print("IN: ", sorted_inList)
print("CC: ", sorted_ccList)