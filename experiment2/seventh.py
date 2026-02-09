
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
sap_id = input("Enter SAP ID: ")
print("Enter marks of 5 subjects:")
marks = []

for i in range(5):
    m = float(input(f"Subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100
cgpa = percentage / 10

if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"
print("\n----- Grade Sheet -----")
print(f"Name       : {name}")
print(f"Roll Number: {roll_no}\t\tSAP ID: {sap_id}")
print(f"Total Marks: {total:.2f} / 500")
print(f"Percentage : {percentage:.2f}%")
print(f"CGPA       : {cgpa:.2f}")
print(f"Grade      : {grade}")
