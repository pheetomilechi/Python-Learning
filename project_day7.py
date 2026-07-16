profile = [
    "first_name": "Jude",
    "last_name": "Dering",
    "role": "Backend Developer",
    "company": "Innovempia"
]

profile["skills"] = "Python", "Git", "Dictionaries"

profile["role"] = "Senior Backend Developer"

print(profile.get("email", "Email not found"))


del profile ["company"]
print(profile)

print("=== API USER PROFILE RESPONSE === ")

for key, value in profile.items():
    print("key: " + key + " value: " + str(value))






























# user = {
#     "name": "Moses",
#     "age": 25,
#     "is_admin": False
# }

# print(user["name"])
# print(user.get("email"))

# user["city"] = "Lagos"
# user["age"] = 26


# del user["city"]
# print(user)

# for key in user:
#     print(key)
    
# for value in user.values():
#     print(value)
    
# for key, value in user.items():
    # print("The key is "+ key + " and the value is " + str(value))