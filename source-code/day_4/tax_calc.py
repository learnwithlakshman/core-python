# Grade calculation 

# 0 - 5 Grade D
# 6 - 7 Grade C
# 8 - 9 Grade B
# 9 - 10 Grade A


score = int(input("Enter the score (0-10) : "))
grade = None

if score < 0 or score >10:
    print("Invalid score please enter score between 0-10")
elif score >=0 and score <= 5:
    grade = "D"
elif score >=6 and score <=7:
    grade = "C"
elif score >=8 and score <=9:
    grade = "B"
elif score >=9 and score <=10:
    grade = "A"

if grade:
    print(f"Grade : {grade}")  


