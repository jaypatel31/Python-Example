import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

ls = mycol.find({},{ "_id": 0}).limit(5)

for x in ls:
    print(x)
