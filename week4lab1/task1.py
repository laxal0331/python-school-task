def find_min_index(numbers):
    min_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
    return min_index

def main():
    input_str = input("Please enter a list of numbers: ")
    numbers = list(map(float, input_str.strip('[]').split(',')))
    min_index = find_min_index(numbers)
    print(f"The min index is: {min_index}")

if __name__ == "__main__":
    main()
