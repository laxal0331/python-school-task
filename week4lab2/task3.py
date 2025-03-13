def check_palindrome():
    input_string = input("Please enter a string: ")
    start = 0
    end = len(input_string) - 1

    while start < end:
        if input_string[start] != input_string[end]:
            return False
        start += 1
        end -= 1
    return True

result = check_palindrome()
if result==True:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

