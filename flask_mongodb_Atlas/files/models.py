from . import note;
from bson.objectid import ObjectId

def deleteNote(id):
    try:
        note.delete_one({"_id": ObjectId(id)})
        return True
    except Exception as e:
        return False

def updateNote(id,notes,status):
    try:
        note.update_one(
            {
                "_id":ObjectId(id)
            },
            {
                "$set":{
                    "note":notes,
                    "status":status
                }
            },
            upsert=False
        )
        return True
    except Exception as e:
        print(e)
        return False