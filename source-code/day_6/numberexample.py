def reverse(num):
    temp = num
    rev = 0
    while temp != 0:
        r = temp % 10
        rev = rev * 10 + r
        temp = temp // 10
    return rev

def is_palindrome(num):
    return reverse(num) == num

def sum_Of_digits(num):
    temp = num
    sum = 0
    while temp != 0:
        r = temp % 10
        sum = sum  + r
        temp = temp // 10
    return sum

def sum_Of_digits_until_single_digit_sum(num):
    while num > 9:
        num = num // 10 + num % 10
    return num


def is_amstrong(num):
    temp = num
    sum = 0
    while temp != 0:
        r = temp % 10
        sum = sum + r * r * r
        temp = temp // 10
    return num == sum

def is_prime(num):
    if num < 2:
        return False
    if num % 2==0 and num != 2:
        return False
    else:
        for i in range(2,num//2+1):
            if num % i == 0:
                return False
    return True

def count_prime(lb,ub):
    count = 0
    for i in range(lb, ub+1):
        if is_prime(i):
            count = count + 1
    return count
def generate_prime_in_range(lb,ub):
    lst = []
    for i in range(lb, ub+1):
            if is_prime(i):
                lst.append(i)
    return lst
def biggest(num1, num2, num3):
    big = None
    if num1 > num2 and num1 > num3:
        big = num1
    elif num2 > num3:
        big = num2
    else:
        big =  num3

    return big


res = generate_prime_in_range(1,10) # 2 3 5 7 
print(res)
