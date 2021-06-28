# Profit or loose example

b_price = int(input("Enter the Buying price: "))
s_price = int(input("Enter the selling price: "))

res = s_price - b_price

if res < 0:
    print(f"You made a loose of {res}")
elif res > 0:
    print(f"You made a profit of {res}")
else:
    print("No profit No loose")