num_1 = 4320
num_2 = 3260

while num_2 != 0:
    print(f"Number 1 = {num_1} and Number 2 = {num_2}")
    remainder = num_1 % num_2
    num_1 = num_2
    num_2 = remainder
if num_2 == 0:
 print(f"Number 1 = {num_1} and Number 2 = {num_2}")
print(f"The greatest common divisor is: {num_1}")

