thisdect = dict()

ip = input("Enter The Length of the Dect - ")
ip =int(ip)
i=0
for i in range(ip):
    stid = input("Enter the Student Id - ")
    stName = input("Enter the name of student- ")
    stMark = input("Enter the Mark of student- ")
    tmp = dict()
    tmp['Name'] = stName
    tmp['Mark'] = stMark

    thisdect[stid] = tmp

getName = input("Enter The id of Student - ")
if getName in thisdect:
    print(thisdect[getName])
else:
    print("Not Found Sorry")
print("Full List - ",thisdect)
print('Total Length - ',len(thisdect))
