# 1. The curly braces {} is used for dictionaries while parantheses () is used for tuples.
# 2. A Key is the label (the left side). A Value is the data (the right side). You always query using the label.
# 3. data = {"status": "active"}
#               print(data["status"])
# 4. The main danger of accessing dictionary data using bracket notation , data["email"] is that if the key does not exist, it will raise a KeyError. 
# 5. The .get() method is used to retrieve the value associated with a key in a dictionary. It allows you to specify a default value to return if the key does not exist, preventing a KeyError from being raised.
# 6. With user["age"] = 30, if the age already exist in the dictionary, it will modify the dictionary by overwritting the existing one.
# 7. When you write user["age"] = 30 and it does not exist, it will update the dictionary by adding the new value and key.
# 8. The dictionary method i use to loop through keys and values is the .items()
# 9. Immutable mean the ability for an object not to be changed after creation such as add, update or delete.
# 10. A backend developer uses Tuple instead of List to store user's Date of Birth so as to keep data safe from accidental updates elsewhere in your system runtime. 