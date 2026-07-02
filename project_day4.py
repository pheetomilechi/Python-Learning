name = input("Enter name: ")
name = name.strip().title()

age = age = float(input("Enter age: "))
age = float(age)
original_total = float(input("Enter total purchase: "))

total_purchase = original_total

discount_applied = "20%"

if age < 13:
    print("Sorry " + name + ", you must be 13 or older to shop here.")
else:
    if total_purchase >= 100:
        discount_applied = "20%"
        total_purchase *= 0.8
    elif total_purchase >= 50:
        discount_applied = "10%"
        total_purchase *= 0.9
    
    print("INNOVEMPIA STORE RECEIPT")
    print("Customer Name: " + name)
    print("Original Total: $" + str(original_total))
    print("Discount Applied: " + discount_applied)
    print("Final Total: $" + str(total_purchase))
    print("Thank you for shopping with us!")
