from . import note;
from bson.objectid import ObjectId

def deleteNote(id):
    try:
        note.delete_one({"_id": ObjectId(id)})
        return True
    except Exception as e:
        return False
