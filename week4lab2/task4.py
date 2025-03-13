def top_students(scores):
    students_list = list(scores.items())
    for i in range(len(students_list)):
        for j in range(0, len(students_list) - i - 1):
            if students_list[j][1] < students_list[j + 1][1]:
                students_list[j], students_list[j + 1] = students_list[j + 1], students_list[j]
    top_three = [student[0] for student in students_list[:3]]
    return top_three
scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Emma': 88
}

top_three_students = top_students(scores)
print("Top Three Students:", top_three_students)
