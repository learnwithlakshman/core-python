num = int(input("Enter the num: "))

isprime = True

if num % 2 == 0 and num != 2:
    isprime = False
else:
    for i in range(2, (num // 2 )+ 1):
        if num % i == 0:
            isprime = False
            break

if isprime:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")