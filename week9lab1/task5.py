def add_matrices(matrix1, matrix2):
    assert len(matrix1) == len(matrix2), "Error: The matrices have different numbers of rows"
    assert len(matrix1[0]) == len(matrix2[0]), "Error: The matrices have different numbers of columns"

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]

try:
    sum_matrix = add_matrices(matrix1, matrix2)
    print("Matrix addition result:")
    for row in sum_matrix:
        print(row)
except AssertionError as e:
    print(e)
