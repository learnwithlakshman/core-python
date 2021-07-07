import random



lst = [random.randint(1,20) for i in range(1,11)]
num = int(input("Enter the num to search: "))


if num in lst:
    print(f"{num} is present  {lst} ",)
else:
    print(f"{num} is not present  {lst}")

