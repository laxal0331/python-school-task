def reverse_concatenate(strings):
    result = ""
    while strings:
        result += strings.pop()
    return result

user_input = input("Enter strings separated by spaces: ")
string_list = user_input.split()

reversed_string = reverse_concatenate(string_list)

print(reversed_string)


