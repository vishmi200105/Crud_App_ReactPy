from pymongo import MongoClient

#Replace <url> with your mongodb atlas connection string
uri = "mongodb+srv://Vishmi19A:vishmi200163503006@cluster1.0rmvjhe.mongodb.net/"
client = MongoClient(uri)

#Replace <database-name> with the name of your database
db = client["DataBase3"]

#Replace <collection-name> with the name of your collection
collection = db["Collection3"]

#check the connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to Mongodb")
except Exception as e:
    print(e)

document = {"name": "Danial","age":36}

#Insert the document into the collection
insert_result = collection.insert_one(document)

#print the ID of the inserted document
print("Inserted Document ID:", insert_result.inserted_id)

client.close()