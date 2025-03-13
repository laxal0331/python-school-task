students = [['John', 75, 67, 77], ['Cen', 66, 71, 59], ['Bryan', 81, 72, 85]]
highest_total = 0
top_student = ""
for student in students:
    total_marks = student[1] + student[2] + student[3]
    if total_marks > highest_total:
        highest_total = total_marks
        top_student = student[0]

print(f"The student with the highest marks is: {top_student}")
