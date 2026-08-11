#Write a program to demonstrate the use of break continue and pass statements. 

students = int(input("Enter number of students: "))

for i in range(students):

    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        print("Invalid Marks")
        continue

    if marks == -1:
        break

    if marks >= 35:
        print("Pass")
    else:
        print("Fail")
