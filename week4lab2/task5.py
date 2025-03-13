def max_abs_difference(numbers):
    max_diff = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

input_string = input("Please enter a list of numbers: ")

numbers = [float(num) for num in input_string.strip('[]').split(',')]

result = max_abs_difference(numbers)

print(f"The maximum absolute difference is: {result}")
