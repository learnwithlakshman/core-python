# Write a program to accept two numbers from the user, swap their values and display the result.

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
print(f'num1 ={num1} and num2 = {num2}')

num1 = num1 * num2
num2 = num1 // num2
num1 = num1 // num2

print(f'num1 = {num1} and num2 = {num2}')