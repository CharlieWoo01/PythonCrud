# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database

dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

item_details = collection_name.find()
for item in item_details:
    # This does not give a very readable output
    print(item)

# THE IDEA OF THIS ESSENTIALLY IS A GET REQUEST AS IT RETURNS THE COLLECTION RESULTS MATCHING THE DB NAME ABOVE
# It may make sense to do as pymongo_get_database.py does with get_database() for collection_name in here so that
# You can reuse it in several places again for efficiency and better maintainability
