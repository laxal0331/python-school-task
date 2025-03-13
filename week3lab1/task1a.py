number = int(input("Enter a number: "))
i = 0
total = 0

while i <= number:
    total=total+i
    i=i+2

print("Sum of even numbers from 0 to", number, "is:", total)
