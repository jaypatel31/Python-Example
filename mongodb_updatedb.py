import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

myquery = {"address":"Surat"}

newvalue = {"$set":{"address":"Naroda"}}

mycol.update_one(myquery,newvalue)
print("After Updation")
print()
for x in mycol.find({},{"_id":0}):
    print(x)
