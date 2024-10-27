from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['journal_db']
entries_collection = db['entries']

def create_entry(title, content):
    entry = {
        "title": title,
        "content": content,
        "date": datetime.datetime.now()
    }
    result = entries_collection.insert_one(entry)
    return result.inserted_id

def get_entries():
    return list(entries_collection.find().sort("date", -1))

def get_entry_by_id(entry_id):
    return entries_collection.find_one({"_id": ObjectId(entry_id)})

def update_entry(entry_id, title, content):
    entries_collection.update_one(
        {"_id": ObjectId(entry_id)},
        {"$set": {"title": title, "content": content}}
    )
