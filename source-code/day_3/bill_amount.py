# Program to calculate discount amount 

bill_amount = float(input("Enter the Bill amount: "))
discount = 0

if bill_amount > 10000:
    discount = bill_amount * 0.1
else:
    discount = bill_amount * 0.05
   
net_amount = bill_amount - discount
print(f"Bill Amount: {bill_amount}\nDisount Amount: {discount}\nNet Amount: {net_amount}")


