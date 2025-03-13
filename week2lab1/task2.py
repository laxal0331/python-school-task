#part a
x, y, n=2, 3, 5
if x == n or y == n:
    print(True)
elif x+y == n:
    print(True)
elif x-y == n or y-x == n:
    print(True)
else:
    print(False)
    print('none of the condition met')

#part b
n=input("enter a number")
remainder = n%10
num = n-remainder
if remainder < 5:                      # If the remainder is less than 5
    print(num)                         # Round down, print the lower multiple of 10
elif remainder > 5:                    # If the remainder is greater than 5
    print(num + 10)                   # Round up, print the next multiple of 10
else:                                   # If the remainder is exactly 5
    if num // 10 % 2 == 0:            # Check if the ten's column is even
        print(num)                     # If even, round down (print num)
    else:
        print(num + 10)



