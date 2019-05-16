import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:50000/")

mydb = myclient["reportsdb"]

# mydict1 = { "name": "John", "address": "Highway 37" }

mycol = mydb["reports"]

# mycol.insert_one(mydict1)

print("These are the databases found : ")

print(myclient.list_database_names())

print("These are the contents of reports")
for row in mycol.find({},{"_id" : 1 }):
  print(row)
  