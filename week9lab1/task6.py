import os
def copy_file(source_file, destination_file):
    try:
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Error: The source file '{source_file}' does not exist.")
        if not os.path.exists(destination_file):
            raise FileNotFoundError(f"Error: The destination file '{destination_file}' does not exist.")

        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Content successfully copied from '{source_file}' to '{destination_file}'.")

    except FileNotFoundError as fnf_error:
        print(f"FileNotFoundError: {fnf_error}")
    except PermissionError as perm_error:
        print(f"PermissionError: {perm_error}")
    except Exception as e:
        print(f"An error occurred: {e}")


# TEST
source_file = 'source.txt'
destination_file = 'destination.txt'

with open(source_file, 'w') as file:
    file.write("TSET")


copy_file(source_file, destination_file)

# Test for files that are not readable or writable.
nonexistent_source = 'nonexistent_source.txt'
nonexistent_dest = 'nonexistent_dest.txt'
# Test for the case where the file does not exist.
copy_file(nonexistent_source, destination_file)
# Test for the case where the destination file is not writable, ensuring that exceptions are caught.
copy_file(source_file, '/restricted_folder/destination.txt')
