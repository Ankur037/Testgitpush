import pymongo

client = pymongo.MongoClient("mongodb+srv://Ankur037:Mango8076@cluster0.slkqhb3.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "ankur",
    "email" : "ankursingh037@gmail.com",
    "surname" : "singh"

}

db1= client['mongotest']
coll = db1['test']
coll.insert_one(d)