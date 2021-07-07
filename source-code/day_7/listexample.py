
lst = [1,2,4,5,6,7,8,9,10]
print(lst[2:5])
print(lst[:5])
print(lst[-4:])

for i in range(0,len(lst)):
    print(lst[i],end=" ")
print()
for i in lst:
    print(i,end=" ")

lst.insert(2,3)
print(lst)

