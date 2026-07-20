# 1. A local variable is a variable created inside a function while a global variable is a variable created outside a function.
# 2. Yes, a function can read a global variable and if it tries to modify it, it works only if you use a global keyword.
# 3. Global keyword is used inside a function to modify a global variable.
# 4. Unhandled error handling is dangerous in backend development because it crashes the processes and corrupts data.
# 5. The two keywords in error handling is "try" and "except".
# 6. try:
#       int("hello")
#     except ValueError:
#       print("Conversion failed")
# 7. Except block tends to catch the error from the risky code and runs it without killing the program while else block runs only if the try block succeeds.
# 8. The finally block runs cleanup code (like closing a file) no matter what happened in the try block.
# 9. try:
#       x = 10 / 0
#    except ZeroDivisionError:
#       print("A")
#     else:
#       print("B")
#     finally:
#       print("C"): Output = A & C
# 10. False