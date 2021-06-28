# Program to find sum of two number

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))


sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
fdiv = num1 / num2
idiv = num1 // num2
mod = num1 % num2

print(f'{num1}  + {num2} = {sum}')
print(f'{num1}  - {num2} = {sub}')
print(f'{num1}  * {num2} = {mul}')
print(f'{num1}  / {num2} = {fdiv}')
print(f'{num1}  // {num2} = {idiv}')
print(f'{num1}  % {num2} = {mod}')