def safe_divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return("Error: Cannot divide by zero!")
    else:
        return("Result: " + str(result))

def get_user_age():
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        return("Invalid age format")
    else:
        return(age)
    
safe_divide(50, 5)
safe_divide(50, 0)
print("Testing age input...")

user_age = get_user_age()
print("User age is: " + str(user_age))

    
  
   
        
        
    




























# def my_function():
#     secret = "I am hidden"
    
# company = "Innovempia"


# def show_company():
#     print("I work at " + company)
# show_company()

# score = 10

# def add_points():
    
#     global score
#     score = score + 5
    
#     add_points()
#     print(score)

# try:
#     age = int(input("Enter age: "))
#     print("You are " + str(age) + " years old. ")
    
# except:
#     print("Error: That was not a valid number!")

# try: 
#     number = int(input("Enter a number to divide 100 by: "))
#     result = 100 / number
#     print("Result is " + str(result))
# except ValueError:
#     print("You didn't enter a number!")
# except ZeroDivisionError:
#     print("You cannot divide by zero")

# try:
#     number = int(input("Enter number: "))
# except ValueError:
#     print("Invalid number!")
# else:
#     print("Success! Your number was " + str(number))
# finally:
#     print("Thank you for using the Innovempia calculator.")