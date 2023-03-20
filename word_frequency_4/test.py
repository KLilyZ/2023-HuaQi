import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test_mongodb
collection = db.students_info
student = {"id": "002",
           "name": "李灿",
           "age": 20,
           "gender": "女",
           "height": 160
           }
result = collection.insert_one(student)
print(result)