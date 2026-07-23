# file = open("sample.txt","r")
# content = file.read()
# print(content)
# file.close()

# file = open("sample.txt", "r")
# line1 = file.readline()
# print(line1)
# file.close()

# file = open("sample.txt", "r")
# lines_list = file.readlines()
# print(lines_list)
# file.close()

# file = open("output.txt", "w")
# file.write("This is the first line. \n")
# file.write("This is the second line.")
# file.close()

file = open("output.txt", "a")
file.write("\nThis is a new line added at the end.")
file.close()