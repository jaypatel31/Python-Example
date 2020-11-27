import math

totalNumber = input("Enter Total Number - ")
totalNumber = int(totalNumber)
i=0
numlist = list()
j=0

print()
for i in range(totalNumber):
    num = input("Enter The "+str(j+1)+" Number - ")
    numlist.append(int(num))
    j += 1 
maxnum = max(numlist)
minnum = min(numlist)
print()
print()
print("Maximum Number:",maxnum)
print()
print("Minimum Number:",minnum)