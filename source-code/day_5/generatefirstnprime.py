N = int(input("Enter the N value:"))

num = 2
count = 0
while True:
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
        print(num,end=" ")
    
    if count == N:
        break
    num += 1