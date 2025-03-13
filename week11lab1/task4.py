def all_passwords(password, password_length):

    if len(password) == password_length:
        print("".join(map(str, password)))
        return

    password.append(0)
    all_passwords(password, password_length)
    password.pop()

    password.append(1)
    all_passwords(password, password_length)
    password.pop()

all_passwords([], 3)
