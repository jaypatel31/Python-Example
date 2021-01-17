import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print("Total Database")
print()
print(myclient.list_database_names())
print()
print()
print("Total Collection in the selected Database")
print()
print(mydb.list_collection_names())
