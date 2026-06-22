name = input("Enter name: ")
name = name.strip().title()

age = int(input("Enter age: "))
age = age.__float__()

total_purchase = float(input("Enter total purchase: "))

if age < 13:
    print("Sorry " + name +", you must be 13 or older to shop here.")
else:
    print("Welcome " + name + "! Your total purchase is $" + str(total_purchase) + ".")
if total_purchase >= 100:
    print("Congratulations " + name + "! You have earned a 20% discount on your purchase.")
    total_purchase = total_purchase * 0.8
    print("Your updated total is $" + str(total_purchase) + ".")
elif total_purchase >= 50:
    print("Congratulations " + name + "! You have earned a 10% discount on your purchase.")
    total_purchase = total_purchase * 0.9
    print("Your updated total is $" + str(total_purchase) + ".")