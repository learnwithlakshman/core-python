arr = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
]

for row in arr:
    for col in row:
        if col == 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

num = 19

for i in range(1,4):
    for j in range(1,4):
        if i == j:
            print(num,end=" ")
        else:
            print(0,end=" ")
    print()