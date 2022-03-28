import motor.motor_asyncio
import dns
import pymongo
from datetime import datetime
import os




DB_URI = os.environ["DB_URI"]

client = pymongo.MongoClient(DB_URI)
# client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
now = datetime.now()
timestamp = now.strftime("%d/%m/%Y %H:%M:%S")

base= client.crud
db = base.todo
class Database:
    def  add(self, data, key):
        document = {"note": data,
        "_id":key,
        "timestamp":timestamp}
        result =  db.insert_one(document)
        return {"added"}


    def show(self):

        result =  [data for data in db.find()]
        print(result)
        return result
    def search(self, data):
        result =  db.find_one({"_id":data})
        return result
        
    def update(self, id ,data):
        db.update_one({"_id":id},{"$set":{"note":data}})
        return {"updated"}
    def delete(self, data):
        db.delete_one({"_id":data})
        return {"deleted"}
    