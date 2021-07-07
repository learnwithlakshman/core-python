import random 
lst = [random.randint(1,10) for i in range(1,26)]
num = 5
count = lst.count(num)
print(f"{lst}")
print(f"Occurance of {num} is {count}")
