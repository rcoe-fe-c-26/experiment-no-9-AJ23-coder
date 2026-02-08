# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Aayush Jha 
# Date:

print("--- Factorial Finder ---\n")


# Write your code here
factorial = 1 
 
num=int(input("Enter the number:"))   

for x in range(1,(num+1)):
    factorial=factorial*x
    
print(factorial)
    
