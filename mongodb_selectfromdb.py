import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

ls = mycol.find({},{ "_id": 0, "name": 1, "address": 1 })

for x in ls:
    print(x)
