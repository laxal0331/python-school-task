def add(lst):
    total = 0
    i = 1
    while i < len(lst):
        total = total+lst[i]
        i = i+2
    return total

print(add([2, -3, 5, 8, 10, 1]))
