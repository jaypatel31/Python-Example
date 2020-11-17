thisset = set()

ip = input("Enter The Length of the Set- ")
ip =int(ip)
i=0
for i in range(ip):
    stName = input("Enter the name of student- ")
    thisset.add(stName)

StaticName = {'Jimmy','Gohil'}
thisset.update(StaticName)
print("Total Student - ",thisset)
print("Length Of Student - ",len(thisset))
removing = thisset.pop()
print("Removed Item - ",removing)
