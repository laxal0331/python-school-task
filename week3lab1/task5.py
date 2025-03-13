def multiplication_table(x):
    table = []
    for i in range(1, x + 1):
        row = []
        for j in range(1, x + 1):
            row.append(i * j)
        table.append(row)
    return table
x = int(input("Enter the size of the multiplication table: "))

result = multiplication_table(x)

for row in result:
    print(row)
#The task has been completed using about loops and list

#Chat History with Gen AI

#Write a program that takes an integer, x, as an input, and prints an x by x
# Multiplication table. For example: if x =3 then sample output [[1,2,3], [2,4,6],[3,6,9]].
# While implementing the program, you should consider the following:
# • the appropriate range pf your loop
# • how to nest your loops
# • how to construct a table in a manner that is ‘safe’ for Python.
#     Multiplication
#     Table
#     Program
#     Here’s
#     a
#     Python
#     program
#     that
#     takes
#     an
#     integer
#     x as input and prints
#     an
#     x
#     by
#     x
#     multiplication
#     table:
#
#     Python
#
#
#     def multiplication_table(x):
#         # 创建一个空的乘法表
#         table = []
#
#         # 外层循环遍历行
#         for i in range(1, x + 1):
#             # 创建一个空的行
#             row = []
#             # 内层循环遍历列
#             for j in range(1, x + 1):
#                 # 计算乘积并添加到行中
#                 row.append(i * j)
#             # 将行添加到乘法表中
#             table.append(row)
#
#         return table
#
#
#     # 获取用户输入
#     x = int(input("Enter the size of the multiplication table: "))
#
#     # 生成乘法表
#     result = multiplication_table(x)
#
#     # 打印乘法表
#     for row in result:
#         print(row)
#     Explanation
#     Define
#     Function: multiplication_table(x)
#     function
#     creates and returns
#     an
#     x
#     by
#     x
#     multiplication
#     table.
#     Initialize
#     Table: An
#     empty
#     list
#     table is created
#     to
#     store
#     the
#     rows
#     of
#     the
#     multiplication
#     table.
#     Outer
#     Loop: The
#     outer
#     for loop iterates over the range from 1 to x (inclusive) to create each row.
#     Inner
#     Loop: The
#     inner
#     for loop iterates over the range from 1 to x (inclusive) to calculate the products and fill each row.
#     Append
#     Rows: Each
#     row is appended
#     to
#     the
#     table
#     list.
#     User
#     Input: The
#     program
#     takes
#     an
#     integer
#     input
#     x
#     from the user.
#     Generate
#     Table: The
#     multiplication_table
#     function is called
#     with the input x to generate the table.
#     Print
#     Table: The
#     resulting
#     multiplication
#     table is printed
#     row
#     by
#     row.
#     Example
#     Output
#     If
#     the
#     user
#     inputs
#     3, the
#     output
#     will
#     be:
#
#     [1, 2, 3]
#     [2, 4, 6]
#     [3, 6, 9]
#
#     This
#     program
#     ensures
#     that
#     the
#     multiplication
#     table is constructed
#     safely and efficiently
#     using
#     nested
#     loops and list
#     operations.If
#     you
#     have
#     any
#     further
#     questions or need
#     additional
#     assistance, feel
#     free
#     to
#     ask!


