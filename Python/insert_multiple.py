import datetime
import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

new_accounts = [
    {
        "account_holder": "Linus Torvalds",
        "account_id": "MDB829001337",
        "account_type": "checking",
        "balance": 50352434,
        "last_updated": datetime.datetime.utcnow()
    },
    {
        "account_holder": "Ada Lovelace",
        "account_id": "MDB011235813",
        "account_type": "checking",
        "balance": 60218,
        "last_updated": datetime.datetime.utcnow()
    },
    {
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_id": "MDB829000001",
        "account_type": "savings",
        "balance": 267914296,
        "last_updated": datetime.datetime.utcnow()
    }
]


result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()
