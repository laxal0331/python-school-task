def print_pattern(n):
    def recursive_helper(x):
        if x == 1:
            print(x, end=" ")
        else:
            print(x, end=" ")
            recursive_helper(x - 1)
        print(x, end=" ")

    recursive_helper(n)

print_pattern(5)
