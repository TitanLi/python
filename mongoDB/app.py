from pymongo import MongoClient
import datetime

post = {"author": "Mike", "text": "My first blog post!", "tags": [
    "mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

# mongo mongodb://b1cccb38-7abe-4511-8800-e5275780a19f:QTLxUraQXnubu4qCgoviSwObQ@mongodb-single-949df24b-9261-4be0-8978-d47e432bf25d-001.eastasia.cloudapp.azure.com:27017/e973cd66-c49a-4c4e-8d85-330ceb44b7db

client = MongoClient(
    'mongodb://mongodb-single-949df24b-9261-4be0-8978-d47e432bf25d-001.eastasia.cloudapp.azure.com:27017/')

db = client['e973cd66-c49a-4c4e-8d85-330ceb44b7db']
db.authenticate('b1cccb38-7abe-4511-8800-e5275780a19f',
                'QTLxUraQXnubu4qCgoviSwObQ')
collection = db['test']

test = collection.insert_one(post).inserted_id
print(test)

# Drop collection
# db.drop_collection('collection-name')
