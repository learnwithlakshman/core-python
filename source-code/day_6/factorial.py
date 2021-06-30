
def factorial(num):
    res = 1
    if num == 0 or num == 1:
        return res
    else:
        for i in range(2,num+1):
            res *= i
    return res


N = int(input("Enter the value of N : "))
res = factorial(N)
print(f"Factorial of {N} is :{res}")