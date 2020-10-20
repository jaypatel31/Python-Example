fname = input("Please Enter The File Name :")
try :
    fhandle = open(fname+".txt")
except :
    print("Can't Open A File")
    quit()

counts = dict()
for lines in fhandle :
    lines = lines.rstrip()
    words = lines.split()
    for word in words :
        counts[word] = counts.get(word,0)+1



def repeatedMost(num) :
    finalKey = None
    finalValue = None
    for key in counts :
        if finalValue is None or counts[key] > finalValue :
            finalValue = counts[key]
            finalKey = key
    counts[finalKey] = 0;
    print(num+" Most Repeated Word is '"+finalKey+"' Repeated :"+str(finalValue)+" times.")

repeatedMost("First")
repeatedMost("Second")
repeatedMost("Third")
