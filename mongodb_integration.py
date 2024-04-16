from pymongo import MongoClient

mongo_host = "localhost"
mongo_port = 27017
mongo_db = "iot_db"
mongo_collection = "iot_data"

# Initialize mongodb client
mongo_client = MongoClient(mongo_host, mongo_port)
db = mongo_client[mongo_db]
collection = db[mongo_collection]

# Function to save message to mongodb
def save_to_mongodb(message):
    collection.insert_one(message)
    print("Message saved to MongoDB.")