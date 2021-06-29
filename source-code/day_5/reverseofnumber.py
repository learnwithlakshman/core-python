num = int(input("Enter the num :"))
temp = num

rev = 0
sum = 0
s = 0
while temp != 0:
    r = temp % 10
    rev = rev * 10 + r
    temp = temp // 10
    s = s + r * r * r
    sum += r

print(f"Reverse of {num} is {rev}")
print(f"Sum of digits of {num} is {sum}")
if num == rev:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

if num == s:
    print(f"{num} is a Amstrong")
else:
    print(f"{num} is not a Amstrong")