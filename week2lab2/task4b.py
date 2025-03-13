def flip(binary_string):
    flipped = " "
    i = 0
    while i < len(binary_string):
        flipped += "1" if binary_string[i] == "0" else "0"
        i =i+1
    return flipped

result = flip('001011')
print(result)
