def find_smallest_triangular(num):
    n = 1
    triangular = 0
    while triangular < num:
        triangular = n * (n + 1) // 2
        n=n+1
    return triangular

user_input = int(input("Enter a positive integer: "))
result = find_smallest_triangular(user_input)
print("The smallest triangular number greater than or equal to", user_input, "is", result)

#To find the smallest triangular number that is greater than or equal to a given positive integer num,
# a while-loop is used.

#chat history with AI
# A triangular number is any number from the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued
# summation of the natural numbers 1, 2, 3, 4, 5, etc.1 Implement a program that takes an integer as an input
# and determines the smallest triangular number that is equal to or larger than the inputted number. The
# program must:
# • take one input: a positive integer, num
# • print the smallest triangular number that is greater than or equal to num
# • use a while-loop
# Example: if user input 25 then program prints 28 as the triangular number 21 (1+2+3+4+5+6 = 21) is smaller
# than 25, and so the next triangular number 28 (1 + 2 + 3 + 4 + 5 + 6 + 7 = 28), which is bigger than 25, is the
# next triangular number in the series.
# Here's a Python program that implements the task of finding the smallest triangular number
# that is equal to or larger than a given positive integer. The program uses a while loop as required:

#def find_smallest_triangular(num):
    # Initialize n to 1, representing the current natural number
   # n = 1
    # Initialize triangular to 0, which will hold the current triangular number
    #triangular = 0

    # Loop until the triangular number is at least the input number
   # while triangular < num:
        # Calculate the triangular number using the formula T(n) = n * (n + 1) // 2
        #triangular = n * (n + 1) // 2
        # Increment n to move to the next natural number
       # n += 1

    # Return the found triangular number
   # return triangular


# Prompt the user to enter a positive integer
#user_input = int(input("Enter a positive integer: "))
# Call the function with the user input and store the result
#result = find_smallest_triangular(user_input)
# Print the smallest triangular number greater than or equal to the user input
#print("The smallest triangular number greater than or equal to", user_input, "is", result)

# Explanation of the Code:
# 1. Function Definition: The function find_smallest_triangular(num) is defined to calculate the triangular number.
# 2. Variables:
#    - n starts at 1, representing the current natural number.
#    - triangular is initialized to 0 and will hold the current triangular number.
# 3. While Loop: The loop continues as long as the current triangular number is less than the input number:
#    - The triangular number is calculated using the formula T(n) = n(n + 1) / 2.
#    - n is incremented by 1 to compute the next triangular number.
# 4. User Input: The program prompts the user to enter a positive integer.
# 5. Output: Finally, it prints the smallest triangular number that is greater than or equal to the user input.

# Example Execution:
# If the user inputs 25, the program calculates:
# - T(1) = 1
# - T(2) = 3
# - T(3) = 6
# - T(4) = 10
# - T(5) = 15
# - T(6) = 21
# - T(7) = 28

# Since 28 is the first triangular number that is greater than or equal to 25, the output will be:
# The smallest triangular number greater than or equal to 25 is 28


