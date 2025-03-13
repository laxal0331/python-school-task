def stable_insertion_sort(student_dataset):
    for i in range(1, len(student_dataset)):
        key = student_dataset[i]
        j = i - 1
        while j >= 0 and student_dataset[j][2] > key[2]:
            student_dataset[j + 1] = student_dataset[j]
            j -= 1
        student_dataset[j + 1] = key
    return student_dataset

student_dataset = [
    [102, 'Alice', 67],
    [100, 'Ben', 78],
    [104, 'Kevin', 89],
    [103, 'Judi', 54],
    [105, 'Gary', 92]
]

sorted_students = stable_insertion_sort(student_dataset)
print(sorted_students)

# The task requires sorting student records by their grades
# in ascending order. Both insertion sort and merge sort
# are stable sorting algorithms that can be applied here.

# chat history with genAI
# You're given a dataset containing student records with attributes such as student ID, course name, and grades
# obtained in their courses. Sort the student records based on their grades in ascending order using a stable sorting
# algorithm.
# # Student dataset
# student_dataset = [
# [102, 'Alice', 67],
# [100, 'Ben', 78],
# [104, 'Kevin', 89],
# [103, 'Judi', 54],
# [105, 'Gary', 92]
# def stable_insertion_sort(student_dataset):
#     for i in range(1, len(student_dataset)):
#         key = student_dataset[i]
#         j = i - 1
#         # Move elements with greater grades to the right
#         while j >= 0 and student_dataset[j][2] > key[2]:
#             student_dataset[j + 1] = student_dataset[j]
#             j -= 1
#         # Insert the current element
#         student_dataset[j + 1] = key
#     return student_dataset
#
# # Input dataset
# student_dataset = [
#     [102, 'Alice', 67],
#     [100, 'Ben', 78],
#     [104, 'Kevin', 89],
#     [103, 'Judi', 54],
#     [105, 'Gary', 92]
# ]
#
# # Sort the dataset
# sorted_students = stable_insertion_sort(student_dataset)
# print(sorted_students)
