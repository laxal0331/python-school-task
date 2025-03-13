def create_table(numbers):
    table = []
    for i in range(1, 4):
        row = [num + i for num in numbers]
        table.append(row)
    return table

numbers = list(map(int, input().split()))
table = create_table(numbers)

for row in table:
    print(row)
