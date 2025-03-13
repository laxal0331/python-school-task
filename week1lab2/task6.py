input_bits = int(input("Enter the number of bits: "))

total_bytes = input_bits // 8

total_kilobytes = total_bytes // 1024

total_megabytes = total_kilobytes // 1024

print(f"Total Bytes: {total_bytes}")
print(f"Total Kilobytes: {total_kilobytes}")
print(f"Total Megabytes: {total_megabytes}")



