def rec_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return rec_palindrome(string[1:-1])


print(rec_palindrome("racecar"))
print(rec_palindrome("level"))
print(rec_palindrome("hello"))
print(rec_palindrome("madam"))
print(rec_palindrome("a"))
print(rec_palindrome(""))

#this task follows the recursion principles
#chat history with gen AI
# Write a recursive function rec_palindrome(string) that
# checks whether the input string is a palindrome string (i.e.,
# return True) or not (i.e., return False). A palindrome string
# is a string that reads the same from either direction.
# def rec_palindrome(string):
#     """Recursively checks if a string is a palindrome."""
#     # Base case: If the string is empty or has only one character, it is a palindrome
#     if len(string) <= 1:
#         return True
#
#     # Compare first and last characters
#     if string[0] != string[-1]:
#         return False  # If they are not equal, it's not a palindrome
#
#     # Recursive call: Check the substring excluding the first and last characters
#     return rec_palindrome(string[1:-1])
#
#
# # Test cases
# print(rec_palindrome("racecar"))  # True
# print(rec_palindrome("level"))  # True
# print(rec_palindrome("hello"))  # False
# print(rec_palindrome("madam"))  # True
# print(rec_palindrome("a"))  # True
# print(rec_palindrome(""))  # True
