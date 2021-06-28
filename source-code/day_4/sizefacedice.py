import random

num = random.randint(1,6)

for i in range(1,4):
    gnum = int(input("Guess a number 1-6 :"))
    if num == gnum:
        print(f"Good you guessed number in {i} attempts")
        break
    else:
        print(f"Sorry wrong guess")
        if i == 3:
            print("You have reached max attempts, try again")
        
            
