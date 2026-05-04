class Student:
    def __init__(self, name, sap, marks):
        self.name = name
        self.sap = sap
        self.marks = marks

    def display(self):
        print(self.name, self.sap, self.marks)

    def percentage(self):
        return sum(self.marks)/3

    def result(self):
        if all(m > 40 for m in self.marks):
            return "Pass"
        return "Fail"

students = []

for i in range(3):
    name = input("Name: ")
    sap = input("SAP: ")
    marks = list(map(int, input("Marks: ").split()))
    students.append(Student(name, sap, marks))

for s in students:
    s.display()
    print("Percentage:", s.percentage())
    print("Result:", s.result())