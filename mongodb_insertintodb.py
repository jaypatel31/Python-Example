import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

def askuser():
    global ip
    ip = input("Enter The Number of Cutomers To Be Intersted: ")
    try:
        ip = int(ip)
    except:
        print("Please Input Number Only")
        askuser()
askuser()

final = list()

for x in range(ip):
    name = input("Enter The Name of Customer: ")
    add = input("Enter The Address of Customer: ")
    tmp ={"name":name,"address":add}
    final.append(tmp)

x = mycol.insert_many(final)

print(len(x.inserted_ids), "Records Inserted")
