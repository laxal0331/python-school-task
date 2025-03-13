def count_ones(binary_string):
    count = 0
    for char in binary_string:
        if char == '1':
            count += 1
    return count

binary_string = input("Please enter a binary string: ")
number_of_ones = count_ones(binary_string)
print(f"Number of 1s in the input string is: {number_of_ones}")
