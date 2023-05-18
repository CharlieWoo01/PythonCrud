from pymongo_get_database import get_database

dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

item_details = collection_name.find({"_id": "U1IT00001"}) # This will get by a specific ID (Would use to delete
# likely too)
for item in item_details:
    # This does not give a very readable output
    print(item)
