
# === YEAR 3000 SCI-FI STORY ===
print("In the bustling metropolis of [city], a legend was born")
print("His name was [hero], and he carried the mighty [weapon]")
print("At his young ag of [age], he discovered a secret code: [code].")
print("Was it a real numeric code [True/False].")
print("Exactly 100 years later, at age [future_age], [hero] saved the universe.")
print("The name [hero] appears 2 times in this tale!")

hero = input("Enter name: ")
print(hero.strip())
print(hero.title())

city = input("Enter city: ")
print(city.strip())
print(city.title())

age = int(input("Enter age: "))
future_age = age + 100

weapon = input("Enter a weapon: ")
print(weapon.upper())

secret_code = input("Enter a 4 digit code: ")
is_valid = secret_code.isdigit()
print("Game has Started")

