# Import necessary module(s)
from copy import deepcopy


# Function to create a new copy of the table
def create_new_copy(table):
    return deepcopy(table)


# Function to add a new row to the table
def add_row(row, table):
    table.append(row)


# Function to delete a row at a given index
def delete_row(index, table):
        table.pop(index)



# Function to insert a row at a specific index
def insert_row(index, row, table):
        table.insert(index, row)



# Function to edit a row at a given index
def edit_row(index, row, table):
        table[index] = row



# Function to add a column to the table
def add_column(column, table):
    if len(column) == len(table):
        for i in range(len(table)):
            table[i].append(column[i])
    else:
        print(
            "Error: The number of rows in the input table do not match with the number of rows in the new input column.")


# Testing the functions
if __name__ == "__main__":
    small_table = [['A', 'B'], ['C', 'D'], ['E', 'F']]

    # Create a new copy of the table
    new_table = create_new_copy(small_table)
    print(new_table)
    # [['A', 'B'], ['C', 'D'], ['E', 'F']]

    # Add a new row
    add_row(['G', 'H'], new_table)
    print(new_table)
    # [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']]

    # Delete a row at index 1
    delete_row(1, new_table)
    print(new_table)
    # [['A', 'B'], ['E', 'F'], ['G', 'H']]

    # Insert a row at index 1
    insert_row(1, ['c', 'd'], new_table)
    print(new_table)
    # [['A', 'B'], ['c', 'd'], ['E', 'F'], ['G', 'H']]

    # Edit a row at index 2
    edit_row(2, ['e', 'f'], new_table)
    print(new_table)
    # [['A', 'B'], ['c', 'd'], ['e', 'f'], ['G', 'H']]

    # Try adding a column with incorrect number of rows
    add_column(['*', '!'], new_table)
    # Error: The number of rows in the input table do not match with the number of rows in the new input column.

    # Add a column with the correct number of rows
    add_column(['*', '!', '?', '.'], new_table)
    print(new_table)
    # [['A', 'B', '*'], ['c', 'd', '!'], ['e', 'f', '?'], ['G', 'H', '.']]
