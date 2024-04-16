# Function to process incoming messages
def process_message(message):
    print("Received message:", message)
    save_to_mongodb(message)

# Function to save message to mongodb
def save_to_mongodb(message):
    print("Saving message to MonoDB..")