import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

query = {"name":{"$gt":"J"}}
#query = {"name":{"$regex":"^J"}} Using Regex
#query = {"name":"JAY"} Normal
result = mycol.find(query,{"_id":0})

for x in result:
    print(x)
