# Team:14
# Name:Kaifeng Li - 35278285
# Name:Hang Yin -  34616535
# Name:Dongshi Xie - 35009977
# Step 1:
# name: Dongshi Xie - 35009977
# purpose: Turns the input into a list of all numbers

# Get the user's input as a list of numbers in string format
l1 = input("Please enter a list of numbers:")[1:-1].split(',')

def num_list(l1):
    # Converts a list of strings to a list of integers
    ln = []
    for i in l1:
        # Convert each string to an integer and add to the list
        ln.append(int(i))
    return ln

# input [1,2,3,4,6,7,8,9,5,2,1,0]
# output [1,2,3,4,6,7,8,9,5,2,1,0]




# Step 2:
# name: Hang Yin - 34616535
# purpose: Calculate the average

def calculate_average(numbers):
    # Calculates the average of a list of numbers
    if len(numbers) == 0:
        # If the list is empty, return 0
        return 0
    # Calculate and return the average of the numbers in the list
    return sum(numbers) / len(numbers)

# Convert the string list to an integer list
numbers = num_list(l1)
# Calculate the average of the numbers
average = calculate_average(numbers)
print("The average is:", average)
# input [1,2,3,4,6,7,8,9,5,2,1,0]
# output 4




# Step 3:
# name: Kaifeng Li - 35278285
# purpose: Calculate the variance

def calculate_variance(lst, average):
    # Calculates the variance of a list of numbers
    variance_sum = 0
    for num in lst:
        # Calculate the squared difference from the average and add to the variance sum
        variance_sum += (num - average) ** 2
    # Calculate and return the variance
    variance = variance_sum / len(lst)
    return variance

# Calculate the variance of the numbers
variance = calculate_variance(numbers, average)
print("The variance is:", variance)

# File header comments present:Yes
# Function header comments present:Yes
# Doc strings present:Yes
# Proper indentation:Yes
# Proper spacing:Yes
# Meaningful function and variable names:Yes
# Magic numbers not used:Yes
# Redundant code present:No
# Modular programming approach used:Yes

