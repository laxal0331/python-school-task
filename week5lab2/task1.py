# Task 1
# Team: 14
# Name: Kaifeng Li - 35278285
# Name: Hang Yin - 34616535
# Name: Dongshi Xie - 35009977
import sys  # Import sys module for exiting the program
import random  # Import random module for generating random numbers

count = 0  # Initialize the gold coin count to 0

# Task 1

def start():
    # Start the adventure by going to the lobby
    go_to_lobby()

def go_to_lobby():
    # Enter the lobby
    global count  # Use the global variable count
    print("Now, you are in the lobby")  # Print the current location
    print_gold_amount()  # Print the current amount of gold coins
    x = input("1. Examine lobby"  # Prompt the user to choose an action
              "\n2. Go to throne hall"
              "\n3. Leave"
              "\nYour choice: ")
    if x == "1":
        examine_lobby()  # If the user chooses 1, examine the lobby
    if x == "2":
        go_to_throne_hall()  # If the user chooses 2, go to the throne hall
    if x == "3":
        leave()  # If the user chooses 3, leave the dungeon
    return

def examine_lobby():
    # Examine the lobby
    global count  # Use the global variable count
    print("Examining...")  # Print examining message
    count += random.randint(-5, 6)  # Randomly increase or decrease the gold coin count
    print_gold_amount()  # Print the current amount of gold coins
    go_to_lobby()  # Return to the lobby
    return

def leave():
    # Leave the dungeon
    sys.exit()  # Exit the program
def go_to_throne_hall():
    # Enter the throne hall
    global count  # Use the global variable count
    print("Now, you are in the hall")  # Print the current location
    print_gold_amount()  # Print the current amount of gold coins
    x = input("1. Examine throne hall"  # Prompt the user to choose an action
              "\n2. Go to lobby"
              "\nYour choice: ")
    if x == "1":
        examine_throne_hall()  # If the user chooses 1, examine the throne hall
    if x == "2":
        go_to_lobby()  # If the user chooses 2, return to the lobby
    return

def examine_throne_hall():
    # Examine the throne hall
    global count  # Use the global variable count
    print("Examining...")  # Print examining message
    count += random.randint(-5, 6)  # Randomly increase or decrease the gold coin count
    print_gold_amount()  # Print the current amount of gold coins
    go_to_throne_hall()  # Return to the throne hall
    return

def print_gold_amount():
    # Print the current amount of gold coins
    global count  # Use the global variable count
    print("You have", count, "coin")  # Print the gold coin count
    return
start()

# File header comments present: Yes
# Comments: The file header includes the task name and team members' names.

# Function header comments present: Yes
# Comments: Each function has a header comment explaining its purpose.

# Doc strings present: Yes
# Comments: Doc strings exist.

# Proper indentation: Yes
# Comments: The code it is easy to read.

# Proper spacing: Yes
# Comments: The code has proper spacing between functions and within the code blocks.

# Meaningful function and variable names: Yes
# Comments: The function and variable names are meaningful and descriptive.

# Magic numbers not used: No
# Comments: The code uses magic numbers in the random.

# Redundant code present: No
# Comments: The code does not contain redundant code.

# Modular programming approach used: Yes
# Comments: The code uses a modular programmin
