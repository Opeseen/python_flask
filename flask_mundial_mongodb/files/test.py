from pymongo import MongoClient, errors;
from bson.objectid import ObjectId;
client = MongoClient('localhost',27017)
db = client.bookstore
invoice = db.invoice


# result = invoice.find_one({"_id":ObjectId("6496c7f1b81cd0626554bfa9")})
result = invoice.find()
