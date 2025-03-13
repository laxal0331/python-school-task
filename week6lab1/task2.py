def modify_table(table):
    for sublist in table:
        if sum(sublist) == 0:
            sublist.append('zero')

table = [[9, -7, -2], [7, 3, 1, 3], [-34, 3, 22], [0], [-1, 1]]
modify_table(table)
print(table)

#The task requires directly modifying the input parameter table,
# which is an operation on mutable data types in Python.

#chat history with AI
# Write a function named modify_table that takes a list of lists of numbers (i.e., a table) as a parameter and modifies
# the input table such that each inner list is extended with the string 'zero' if the numbers in that list add up to 0. The
# implemented function should not have a return statement.
# For example:
# table = [[9,-7,-2], [7,3,1,3], [-34,3,22], [0], [-1,1]]
# print(modify_table(table))
# output: [[9, -7, -2, 'zero'], [7, 3, 1, 3], [-34, 3, 22], [0, 'zero'], [-1, 1, 'zero']]
# def modify_table(table):
#     # Loop through each sublist in the table
#     for sublist in table:
#         # Check if the sum of elements in the sublist is zero
#         if sum(sublist) == 0:
#             # Append 'zero' if the sum is zero
#             sublist.append('zero')
#
# # Example table
# table = [[9, -7, -2], [7, 3, 1, 3], [-34, 3, 22], [0], [-1, 1]]
# modify_table(table)
# print(table)

