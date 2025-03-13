#Concept Used: While Loop
def sum_numbers(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

try:
    n = int(input("Enter a positive integer: "))
    if n > 0:
        result = sum_numbers(n)
        print(f"The sum of numbers from {n} to 1 is: {result}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter an integer.")


#chat history with AI

#Write a program that takes an integer n (a positive number)
# as input and calculates the sum of all

#the numbers using a while loop between the number and 1.
# And prints the sum
# Function to calculate the sum of numbers from n to 1
#def sum_numbers(n):
# Initialize total to 0
# total = 0
#While n is greater than 0
#while n > 0:
# Add n to total
#total += n
# Decrease n by 1
#n -= 1
# Return the total sum
#return total

# Input from the user
#try:
 # Get user input
#n = int(input("Enter a positive integer: "))
# Check if the input i
    # else:
        # Handle invalid input
#        print("Please enter a positive integer.")
#except ValueError:
    # Handle non-integer input
#    print("Invalid input. Please enter an integer.")

# How It Works
# 1. The program prompts the user to input a positive integer.
# 2. It checks if the input is valid and greater than 0.
# 3. It uses a while loop to sum all integers from n down to 1.
# 4. Finally, it prints the total sum.

# You can run this program in any Python environment.
# If you have any questions or need further assistance, feel free to ask!

