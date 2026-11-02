# Multi-Stage Scholarship Shortlisting
students = []
n = int(input("Enter number of students: "))
quota = int(input("Enter scholarship quota: "))
for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")
    marks = float(input("Enter academic marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))
    if marks >= 75 and attendance >= 75 and income <= 250000:
        students.append((name, marks))
# Rank students based on marks
students.sort(key=lambda x: x[1], reverse=True)
# Select candidates according to quota
selected = students[:quota]
print("\n--- Scholarship Selected Students ---")
if selected:
    for rank, student in enumerate(selected, start=1):
        print(rank, student[0], "- Marks:", student[1])
else:
    print("No eligible students found.")
print("\nTotal Eligible Students:", len(students))
print("Total Selected Students:", len(selected))

