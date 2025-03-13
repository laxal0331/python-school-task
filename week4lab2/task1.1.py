def sum_of_squares():
    total = 0
    i = 1
    while i <= 5:
        total += i ** 2
        i += 1
    return total

result = sum_of_squares()
print("Sum of squares of the first five natural numbers:", result)
