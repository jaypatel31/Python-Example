listitem = list()
dictitem = dict()

totalStudent = input('Enter The Number of Students- ')
totalStudent = int(totalStudent)

i=0
for i in range(0,totalStudent):
    studentName = input('Enter Student Name- ')
    studentNumber = input('Enter Student Number- ')
    listitem.append(studentName)
    dictitem[studentName] = studentNumber

print('Last:',listitem[-1])
[print(list) for list in listitem]
print('Dict:',dictitem)
listitem.sort(key=str.lower)
print('After Sorting: ',listitem)
listitem.pop()
print('After Removing Last:',listitem)
