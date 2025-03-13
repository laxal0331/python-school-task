def double_characters(input_string):
    updated_string = ""
    for char in input_string:
        updated_string += char * 2
    return updated_string

initial_string = "hello"
updated = double_characters(initial_string)
print("Updated String:", updated)
