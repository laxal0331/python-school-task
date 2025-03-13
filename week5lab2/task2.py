# Task 2
# Team: 14
# Name: Kaifeng Li - 35278285
# Name: Hang Yin - 34616535
# Name: Dongshi Xie - 35009977
import sys  # Import sys module for exiting the program
import random  # Import random module for generating random numbers


count = 0  # Initialize the gold coin count to 0


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
    elif x == "2":
        go_to_throne_hall()  # If the user chooses 2, go to the throne hall
    elif x == "3":
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
    global count  # Use the global variable count
    print(f"Gold count before leaving: {count}")  # Debugging line to check the value of count
    if count < 0:  # If the user's gold is negative, go to the kitchen
        print("You don't have enough gold to leave the dungeon...")
        go_to_kitchen()  # Send the user to the kitchen
    else:
        sys.exit()  # Exit the program if gold is not negative

def go_to_throne_hall():
    # Enter the throne hall
    global count  # Use the global variable count
    print("Now, you are in the throne hall")  # Print the current location
    print_gold_amount()  # Print the current amount of gold coins
    x = input("1. Examine throne hall"  # Prompt the user to choose an action
              "\n2. Go to lobby"
              "\nYour choice: ")
    if x == "1":
        examine_throne_hall()  # If the user chooses 1, examine the throne hall
    elif x == "2":
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

def go_to_kitchen():
    # Go to the kitchen to wash dishes
    global count  # Use the global variable count
    print("You are now in the kitchen.")
    print_gold_amount()  # Print the current amount of gold coins
    x = input("1. Wash the dishes"  # Prompt the user to choose an action
              "\n2. Go back to lobby"
              "\nYour choice: ")
    if x == "1":
        wash_dishes()  # If the user chooses to wash dishes
    elif x == "2":
        go_back_to_lobby()  # If the user chooses to go back to the lobby
    return

def wash_dishes():
    # Wash the dishes (this increases the user's gold by 1)
    global count  # Use the global variable count
    print("You wash the dishes and earn 1 gold coin.")
    count += 1  # Increase the gold coin count by 1
    print_gold_amount()  # Print the current amount of gold coins
    go_to_kitchen()  # Return to the kitchen after washing dishes

def go_back_to_lobby():
    # Go back to the lobby (this decreases the user's gold by 10 if negative)
    global count  # Use the global variable count
    if count < 0:
        count -= 10  # Decrease gold by 10 if negative
        print("You return to the lobby, but your gold decreases by 10.")
    else:
        print("You return to the lobby.")
    go_to_lobby()  # Return to the lobby after going back




start()
