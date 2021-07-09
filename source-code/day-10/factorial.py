
# 1 + 1 / 2! + 1 / 3! + 1 / 4! +...... 1/n!

def factorial(num):
    res = 1
    for i in range(2,num+1):
        res *= i
    return res

def sum_of_series(n):
    sum = 1
    for i in range(2, n + 1):
        sum += 1/factorial(i)
    return sum

num = 5

res = factorial(num)
sum = sum_of_series(num)

print(f"The factorial of {num} is :{res} and sum of series :{sum}")