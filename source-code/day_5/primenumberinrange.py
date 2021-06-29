lb = int(input("Enter the lb : "))
ub = int(input("Enter the ub : "))

count = 0
for num in range(lb,ub+1):
    isprime = True
    if num % 2 == 0 and num != 2:
        isprime = False
    else:
        for i in range(2,(num//2)+1):
            if num % i == 0:
                isprime = False
                break
    if isprime and num > 1:
        count += 1
        print(num)
print(f"Prime count in range {lb} and {ub} is {count}")
