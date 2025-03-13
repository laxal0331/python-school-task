def some_passwords(password, password_length):

    max_ones = password_length // 2

    if len(password) == password_length:
        print("".join(map(str, password)))
        return

    password.append(0)
    some_passwords(password, password_length)
    password.pop()

    if password.count(1) < max_ones:
        password.append(1)
        some_passwords(password, password_length)
        password.pop()

some_passwords([], 4)
