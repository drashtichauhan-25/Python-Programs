import makrs_model as mark

name=input("enter name of student:")
roll =int(input("Enter roll no."))

m1=float(input("enter dbms marks:"))
m2=float(input("enter ds marks:"))
m3=float(input("enter os marks:"))

total=mark.marks(m1,m2,m3)
per= mark.percentage(total)


print("\n----- STUDENT RESULT -----")
print("Name       :", name)
print("Total Marks:", total)
print("roll no:",roll)
print("Percentage :", per)
