def reverse(lst):

    if len(lst) <= 1:
        return lst

    return reverse(lst[1:]) + [lst[0]]
# The concept of base case and list slicing operation was used.
# chat history with gen AI
# Write a recursive function reverse(lst) that computes the reversion of lst.
# For example:
# >>> r e v e r s e ( [ 1 , 2 , 3 , 4 ] )
# [ 4 , 3 , 2 , 1 ]
# >>> r e v e r s e ( [ 1 0 , 1 1 , 1 2 , 1 3 , 1 4 ] )
# [ 1 4 , 1 3 , 1 2 , 1 1 , 1 0]
# >>> r e v e r s e ( [ 1 ] )
# [ 1 ]
# >>> r e v e r s e ( [ ] )
# [ ]
# def reverse(lst):
#     # Base case: if the list is empty or has one element, return it as is
#     if len(lst) <= 1:
#         return lst
#     # Recursive case: reverse the rest of the list and add the first element at the end
#     return reverse(lst[1:]) + [lst[0]]
