

hero = input("Enter name: ")
hero = hero.strip().title()


city = input("Enter city: ")
city = city.strip().capitalize()

age = int(input("Enter age: "))
future_age = age + 100

weapon = input("Enter a weapon: ")
weapon = weapon.upper()

secret_code = input("Enter a 4 digit code: ")
is_valid = secret_code.isdigit()


print("=== YEAR 3000 SCI-FI STORY ===")
print("In the bustling metropolis of " + city + ", a legend was born")
print("His name was " + hero + ", and he carried the mighty " + weapon + ".")
print("At his young age of " + str(age) + ", he discovered a secret code: " + secret_code + ".")
print("Was it a real numeric code " + str(is_valid) + ".")
print("Exactly 100 years later, at age " + str(future_age) + ", " + hero + " saved the universe.")
print("The name " + hero + " appears 2 times in this tale!")


