def insert_missing_numbers(sorted_list):
    start = sorted_list[0]
    end = sorted_list[2]

    i = 0
    for num in range(start, end + 1):
        if num != sorted_list[i]:
            sorted_list.insert(i, num)
        i =i+ 1

    return sorted_list

original_list = [12, 15, 19]
print(original_list)
updated_list = insert_missing_numbers(original_list)
print(updated_list)
