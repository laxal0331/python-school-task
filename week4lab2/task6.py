def remove_redundant_keys(d):

    unique_values = {}

    for key, value in d.items():

        if value not in unique_values:
            unique_values[value] = key

    result = {key: value for value, key in unique_values.items()}
    return result

d1 = {"one": "eleven", "2": 2, "three": 3, "11": "eleven", "four": 44, "two": 2}
d2 = remove_redundant_keys(d1)
print(d2)

# This task using Python dictionaries to
# chat history with AI
# Write a Python program to remove keys with same values in a dictionary.
# For example:
# Input: d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
# Output d2= {'three': 3, 'four': 44}
# def remove_duplicate_values(d):
#     # Step 1: Create a dictionary to count the occurrences of each value
#     value_count = {}
#
#     # Count the occurrences of each value in the dictionary
#     for value in d.values():
#         value_count[value] = value_count.get(value, 0) + 1
#
#     # Step 2: Build a new dictionary excluding values that occur more than once
#     result = {key: value for key, value in d.items() if value_count[value] == 1}
#
#     return result
#
#
# # Example input dictionary
# d1 = {"one": "eleven", "2": 2, "three": 3, "11": "eleven", "four": 44, "two": 2}
#
# # Call the function and print the output
# d2 = remove_duplicate_values(d1)
# print(d2)

