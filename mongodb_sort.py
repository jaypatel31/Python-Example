import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print("Sorting Data in assecnding order with respect to Name")
print()
print()
mydoc = mycol.find({},{"_id":0}).sort("name") # for Descesnding : .sort("name":-1)

for x in mydoc:
    print(x)
