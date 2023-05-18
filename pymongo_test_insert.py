# Creating a collection in the MongoDB database
from pymongo_get_database import get_database  # The idea of this is the main db config, so you can reuse the connection

dbname = get_database()
collection_name = dbname["user_1_items"]  # Collection name you will change

# Insert the data into the database
item_1 = {
    "_id": "U1IT00001",
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance"
}

item_2 = {
    "_id": "U1IT00002",
    "item_name": "Egg",
    "category": "food",
    "quantity": 12,
    "price": 36,
    "item_description": "brown country eggs"
}
collection_name.insert_many([item_1, item_2])
