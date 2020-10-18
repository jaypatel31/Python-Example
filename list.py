print("******************String Finder*******************");
str = input("Enter Any String :")

words = str.split()
tmp=["X"]
Firstfound = 0
repet = []
for word in words :
    word = word.lower()
    if word in tmp :
        Firstfound = Firstfound+1
        repet.append(word)
    tmp.append(word)

print("Total Repeted Words : ", Firstfound)
print("Words Are", repet)
