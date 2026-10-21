
# User Defined Function to calculate grade

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "FAIL"


name = input("Enter student name: ")
marks = float(input("Enter marks: "))

grade = calculate_grade(marks)


print("\n----- Student Result -----")
print("Name  :", name)
print("Marks :", marks)
print("Grade :", grade)
