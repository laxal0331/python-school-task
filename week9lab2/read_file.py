def read_file(student_file, class_file):
    forbidden_names = []

    with open(class_file, 'r') as class_csv_file:
        for line in class_csv_file:
            columns = line.strip().split(',')
            if len(columns) >= 1:
                forbidden_names.append(columns[0].strip())

    valid_rows = []

    with open(student_file, 'r') as student_csv_file:
        for line in student_csv_file:
            line = line.strip()

            line = line.replace('"', '').strip()

            columns = line.split(',')

            if len(columns) != 3:
                print(f'Missing or have extra column(s) "{line}" is ignored!')
                continue

            name, age_str, campus = columns
            name = name.strip()
            campus = campus.strip()

            if name in forbidden_names:
                print(f'Name is in the forbidden list of names. "{line}" is ignored!')
                continue

            try:
                age = int(age_str.strip())
            except ValueError:
                print(f'Age has to be an integer number. "{line}" is ignored!')
                continue

            campuses = ['Australia', 'Malaysia']
            if campus not in campuses:
                print(f'Incorrect campus. "{line}" is ignored!')
                continue

            valid_rows.append((name, age, campus))

    return valid_rows

valid_students = read_file('student.csv', 'Class.csv')
print(valid_students)