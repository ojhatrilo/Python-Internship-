
from pymongo import MongoClient

# MongoDB connection string (replace "username", "password", "mycluster" accordingly)
uri = "mongodb://localhost:27017"

# Establish connection
client = MongoClient(uri)
# Access database
db = client.mydatabase

# Access collection
collection = db.mycollection

# # Insert document
document = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}
collection.insert_one(document)

# Find documents
documents = collection.find({"age": {"$gt": 25}})
for doc in documents:
    print(doc)

# Update document
filter = {"name": "John Doe"}
update = {"$set": {"age": 35}}
collection.update_one(filter, update)

# Delete document
filter = {"name": "John Doe"}
collection.delete_one(filter)

client.close()


