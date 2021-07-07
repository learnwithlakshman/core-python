
count = int(input("Enter the student count : "))
capacity = int(input("Enter the room capacity : "))

no_of_rooms = 0

if count % capacity == 0:
    no_of_rooms = count // capacity   
else:
    no_of_rooms = count // capacity + 1

print(f"Total {count} students with room capacity {capacity} required {no_of_rooms} rooms")

flag = 0
for i in range(1,no_of_rooms+1):
    print(f"\n\nRoom {i} :\n")
    for j in range(1,capacity+1):
        flag = flag + 1
        print(flag,end=" ")
        if flag == count:
            break
        
print("\n I am done...")

