marks=int(input("Enter marks = "))
name = input("Student Name: ")
name_marks={name:marks}
if marks>=90:
    grade="A+"
elif marks in range(85,89):
    grade="A"
elif marks in range(80,84):
    grade="A-"
elif marks in range(75,79):
    grade="B+"
elif marks in range(70,74):
   grade="B"
else:
    grade="failed"
print(name_marks, name, "Grade is", grade)
