

### Initial Setup From Scratch:
Please Note: You must have MongoDB Compass and Pip installed for this to work.

- Open your CLI (GitBash preferably) and run `cd ~/Projects/PythonCrud` - Or whatever path you have it set as. You may need to use the absolute path if it is another CLI e.g. `cd C:/Users/Username/Projects/ProkectName`
- Run the following command: `python -m venv env`. This should generate an env package
- Then run `source env/Scripts/activate` if you are using Git Bash. If not then the following command may work:`source env/bin/activate`. Otherwise either ask me or search it.
- Once you have run those commands successfully run the following command `python -m pip install "pymongo[srv]"`
- If you are using PyCharm (Maybe other IDE's, I am unsure) then you may need to go to `File > Settings > Type Project In The Search > Python Interpreter`. Then click on the small + icon above the table and search for `pymongo` then click install and check after completion if it is within that table

### Examples:
Please see some of the examples below of how to get this to work (These all work for me so should be good starting point)

In your CLI directory as above:
- Post/create: `python pymongo_test_insert.py`
- Get/read: `python pymongo_test_query.py` (Works but looks shocking)
- Get/read specific ID: `python pymongo_check_specific.py`

Follow documentation on MongoDB comments as they look similar to here, using the ID as above would be used to update and delete I would imagine but I can look further into this if you have had a go and can't figure it out as it is a pain.

### Important:
I haven't done this but further down the line and more complex there may be some issues where there are undefined columns and all that. You may need to install panda which will fix this. See below:

In your CLI directory as above:
- Run the following: `python -m pip install pandas`
- In the GET file import the following: `from pandas import DataFrame`
- Then add the following code (pymongo_test_query) - Sorry I haven't tested this but it may be in a loop or outside it - Happy to help if issues if it is needed:
```python
# Use the import and the variable name of the find method
items_df = DataFrame(item_details)

# Should print without the errors if there were any stating "NaN" or "NaT"
print(items_df)
```

