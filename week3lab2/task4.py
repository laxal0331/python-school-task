def remove_outliers(table):
    max_value = max(max(row) for row in table)
    min_value = min(min(row) for row in table)

    mid_value = (max_value + min_value) / 2

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == max_value or table[i][j] == min_value:
                table[i][j] = mid_value

    return table

lst = [[0, 4], [2, 4], [-1, 3]]
updated_lst = remove_outliers(lst)
print(updated_lst)
