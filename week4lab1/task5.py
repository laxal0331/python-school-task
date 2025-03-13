def is_magic(table):
    n = len(table)
    magic_sum = sum(table[0])

    for row in table:
        if sum(row) != magic_sum:
            return False

    for col in range(n):
        if sum(table[row][col] for row in range(n)) != magic_sum:
            return False

    if sum(table[i][i] for i in range(n)) != magic_sum:
        return False

    if sum(table[i][n-1-i] for i in range(n)) != magic_sum:
        return False

    return True

table = [
    [17, 24, 1, 8, 15],
    [23, 5, 7, 14, 16],
    [4, 6, 13, 20, 22],
    [10, 12, 19, 21, 3],
    [11, 18, 25, 2, 9]
]

print(is_magic(table))
