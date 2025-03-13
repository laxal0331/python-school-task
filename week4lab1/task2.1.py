import random

my_list = [2,3,5,4,1]
random_element_list = random.choice(my_list)
print(f"Random element from list: {random_element_list}")

my_dict = {'a':20,'c':10,'b':30}
random_element_dict = random.choice(list(my_dict.values()))
print(f"Random element from dictionary: {random_element_dict}")
