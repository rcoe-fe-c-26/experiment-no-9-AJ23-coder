# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Aayush Jha 
# Date: 30 january 2026

print("--- Factorial Finder ---\n")


# Write your code here
num=int(input("Enter the number:"))   
factorial=1
if(num>=0):
    for n in range(1,num+1):
        factorial=factorial*n
    print(f"Factorial of {num} is {factorial}")
else:
    print(f"Factorial of {num} is Not Defined")





