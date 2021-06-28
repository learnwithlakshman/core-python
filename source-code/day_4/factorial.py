# program to find factorial of the given number

num = int(input("Enter the num: "))

r = 1
for i in range(num,1,-1):
    print(i)
    r = r * i

print(f"Factoiral of {num} is {r}")

