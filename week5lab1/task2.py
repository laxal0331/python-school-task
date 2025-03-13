def perfect(number: int) -> bool:
    if number < 2:
        return False
    sum_of_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_factors += i
    return sum_of_factors == number

for num in range(1, 1001):
    if perfect(num):
        print(num)

#This task uses the concepts of loops and conditional statements.

#chat history with AI
# Write a function perfect() that determines if parameter number is a perfect number. Use this function in a program that
# Determines and prints all the perfect numbers between 1 and 1000.
# Note: An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the
# number. E.g., 6 is a perfect number because 6=1+2+3].
# def perfect(number: int) -> bool:
#     """
#     Determines if a number is a perfect number.
#
#     Parameters:
#     number (int): The number to check.
#
#     Returns:
#     bool: True if the number is a perfect number, otherwise False.
#     """
#     if number < 2:
#         return False
#     sum_of_factors = 0
#     for i in range(1, number):
#         if number % i == 0:
#             sum_of_factors += i
#     return sum_of_factors == number
#
#
# # 使用该函数打印 1 到 1000 之间的所有完美数
# for num in range(1, 1001):
#     if perfect(num):
#         print(num)

