# def my_function():
#     secret = "I am hidden"
    
# company = "Innovempia"


# def show_company():
#     print("I work at " + company)
# show_company()

score = 10

def add_points():
    
    global score
    
    score = score + 5
    
    add_points()
    
    print(score)