import helpers
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/2")

data = response.json()

company_name = data["company"]["name"]
clean_name = helpers.text(data("name"))
print("===LIVE API DATA===")
print("User: " + str(clean_name))
print("Company: " + str(company_name))

















# import math
# print(math.sqrt(16))

# from random import randint
# print(randint(1, 10))

# import datetime as dt
# print(dt.datetime.now())

# import datetime

# right_now = datetime.datetime.now()
# print("Year: " + str(right_now.year))
# print("Month: " + str(right_now.month))

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# user_data = response.json()

# name = user_data["name"]
# email = user_data["email"]

# print("Name: " + name)
# print("Email: " + email)
