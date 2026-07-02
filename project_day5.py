
correct_password = "admin1234"
is_locked = True
attempt = 3

for attempt in range(attempt):
    user_input = input("Enter your password: ").strip()
    if user_input == correct_password:
        print("Access Granted! Welcome to Innovempia.")
        break
    else:
        remaining = 2 - attempt 
        if remaining > 0:
            print("Incorrect password. Attempts left: " + str(remaining))
        else:
            print("ACCOUNT LOCKED. Too many failed attempts")































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