from collections import Counter


def count_most_frequent(container):
    if not container:
        return [None, 0]


    count_dict = Counter(container)

    most_frequent = max(count_dict.items(), key=lambda x: x[1])

    return most_frequent


test = "abcabca"
print(count_most_frequent(test))  # Output: ('a', 3)

#This task using the dict and Max Function and efficiently implements the required.
# chat history with AI
# We want to write a function count_most_frequent that takes as input a container that can be iterated over (e.g. a
# list or a string), and returns the most frequent element in the container, as well as the number of times it occurs in
# the container. For example, if the input is ['a', 'b', 'a', 'c'], the output should be the tuple ('a', 2).
# 4
# 5
# In the case of a tie, we should return the most frequent element that appears first in the container. For example, if
# the input is ['a', 'b', 'a', 'b'], the output should be ('a', 2).
# def count_most_frequent(container: object) -> (object, int):
#     """ Finds and counts the number of occurrences of the most frequent element (using == for comparing)
#         In case of a tie, the tied element that appears first is picked.
#           Parameters:
#                 container: a container
#            Returns:
#                 a list with (the most frequent element, the number of occurrences),
#                 and [None, 0] if the container is empty.
#     """
#     #TODO write the function
# test = "abcabca"
# print(count_most_frequent(test))
# #output  → [a, 3]
# from collections import Counter
#
#
# def count_most_frequent(container):
#     if not container:  # If the container is empty
#         return [None, 0]
#
#     # Count the occurrences of each element in the container
#     count_dict = Counter(container)
#
#     # Find the most frequent element. max returns the first most frequent element in case of a tie.
#     most_frequent = max(count_dict.items(), key=lambda x: x[1])
#
#     return most_frequent
#
#
# # Test cases
# test = "abcabca"
# print(count_most_frequent(test))  # Output: ('a', 3)
