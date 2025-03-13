try:
    with open("school_prompt2.txt", "r") as file:
        file_content = file.read()
        num_char = len(file_content)
    print(f"The number of characters in the file is: {num_char}")

except FileNotFoundError:
    print("Error: The file 'school_prompt2.txt' was not found. Please check if the file path is correct.")

