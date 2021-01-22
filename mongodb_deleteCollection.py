import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

query = {"name":"JAY"}
mycol.delete_one(query)
print("After Deletation:")
print()
print()

result = mycol.find({},{"_id":0})

for x in result:
    print(x)
