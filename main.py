# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Aayush Jha 
# Date:

print("--- Factorial Finder ---\n")


# Write your code here
 
num = int(input("Enter the number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for x in range(1, num + 1):
        factorial *= x
    print(factorial)





