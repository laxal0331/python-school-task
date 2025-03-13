def calculate_average_marks(marks_list):
    average_marks = []

    for marks in marks_list:
        average = sum(marks) / len(marks)
        average_marks.append(average)
    return average_marks

marks_list = [
    [80, 75, 90, 85],
    [65, 70, 75, 80],
    [85, 90, 92, 88]
]

average_marks = calculate_average_marks(marks_list)
print("Average marks of all students:", average_marks)
