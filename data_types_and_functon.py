# # integers (init)
# users_online = 450
# temperature = -10
# year_founded = 2024

# # Floats (float)
# product_price = 49.99
# pi_value = 3.14159
# tax_rate = 0.05

# # Strings (str)
# first_name = "Moses"
# email_address = "'moses@innovempia.com"
# phone_string = "08012345678" # This is a text, not a math

# # Booleans (bool)
# is_Admin = True
# payment_successful = False

# # Inspecting Data with type()
# age = 25
# print(type(age)) # Output. <class 'init'>
# is_active = True
# print(type(is_active)) # Output <class 'bool'>

# # To string str()
# score = 100
# print("You scored " + str(score))

# # To integer int()
# user_age = "25"
# new_age = int(user_age) + 5
# print(new_age)

# # To Float float()
# whole_num = 10
# decimal_num = float(whole_num)
# print(decimal_num) 

# # To Boolean bool()
# print(bool("Hello"))
# print(bool(""))
# print(bool(0))

# Case Methods
# name = "mOsEsjOhNsOn"
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# The variable 'name' is STILL "mOsEsjOhNsON!"

# Whitespace Methods
# messy = " hello world "
# print(messy.strip()) 
# print(messy.lstrip())

# Search & Modify Methods
# story = "I like cats. My friend likes cats too."
# print(story.replace("cats", "dogs"))
# print(story.find("friend"))
# print(story.count("cats"))

# Validation Methods
# email = "moses@innovempia.com"
# print(email.startswith("moses"))
# print(email.endswith(".com"))

# user_input = "12345"
# print(user_input.isdigit())

# username = "Moses123"
# print(username.isalpha())

# Length Function
# word = "innovempia"
# print(len(word))

# Input function and Casting Trap
age = input("Enter age: ") # This is a string
next_year = age + 1 
age = int(input("Enter age: "))
next_year = age + 1

