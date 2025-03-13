def check_elements_are_contained(container_to_test, allowed_elements):
    for A in container_to_test:
        if A not in allowed_elements:
            return False
        else:
          return True

valid_name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
units_allowed = ["MCD4710", "MCD4700", "MCD4740", "MCD1160"]

def is_valid_name(name):
    return all(char in valid_name for char in name)

def is_valid_units(units):
    unit_list = units.split(',')
    return check_elements_are_contained(unit_list, units_allowed)

def main():
    while True:
        name = input("Enter your name: ")
        if is_valid_name(name):
            break
        else:
            print("Invalid name. Please use only letters and spaces.")

    while True:
        units = input("Enter your units, separated by commas (no space): ")
        if is_valid_units(units):
            break
        else:
            print("Invalid units. Please enter valid units from the allowed list.")

    print("Data validated")

main()
