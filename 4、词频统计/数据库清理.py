import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test_database"]
mycol = mydb["test_database"]

x = mycol.delete_many({})

print(x.deleted_count, "--数据已归零")