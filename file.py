fileName = input("Enter The Name Of File : ")

try :
    fileHandle = open(fileName+".txt")
except :
    print("File Cannot Opened ")
    quit()

word = input("Enter The Word To Be Searched : ")
word = word.lower()
found = 0
linenum = 0
indexs = []
for line in fileHandle :
    line = line.rstrip()
    line = line.lower()
    linenum=linenum+1
    if line.startswith(word) :
        found = found+1
        indexs.append(linenum)

print("Number of Words Found : "+str(found))
print("At Line Number :", indexs)
