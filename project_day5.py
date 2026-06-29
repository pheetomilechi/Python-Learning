


correct_password = "admin1234"

is_locked = True

    

for i in range(3):
        
        if i == 2:
            attempt = 3
            
            
            user_input = input("Enter your password: " )
            user_input = user_input.strip()
            is_locked = False
            break
else:            
            
        if user_input == correct_password:
                print("Access Granted! Welcome to Innovempia. ")
                   

        else:
            if is_locked == False:
                print("Incorrect password. Attempts left: " + str(2 - i))
                
            
            if is_locked == True:
                print("ACCOUNT LOCKED. Too many failed attemmpts")
                
            
        































# count = 1

# while count <= 3:
#     print("This is loop number " + str(count))
#     count = count + 1
    
#     print("Loop finished!")

# count = 1
# while count <= 3:
#     print("Stuck forever!")


# for i in range(4):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(5):

#     if i == 3:
#         break

#     print(i)

# for i in range(5):
    
#     if i == 2:
#         continue
#     print(i)