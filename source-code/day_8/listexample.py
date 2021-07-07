import random

def getElements():
    lst = []
    for i in range(1,11):
        lst.append(random.randint(1,20))
    return lst

lst = getElements()
ele1 = int(input("Guess a number in range (1-20) :"))
ele2 = int(input("Guess a number in range (1-20) :"))
ele3 = int(input("Guess a number in range (1-20) :"))

if ele1 in lst and ele2 in lst and ele3 in lst:
    print(f"Success")
else:
    print(f"Fail")
    
print(lst)




