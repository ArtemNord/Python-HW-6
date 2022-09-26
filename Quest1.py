# Таблица умножения и сложения


def print_operation_table(operation, num_rows, num_columns):
    rows = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    columns = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    array = [rows, columns]
    min = '-'
    plus = '+'
    dev = '/'
    mnoj = '*'
    stepen = '**'
    if operation == mnoj:
        i = 0
        while i != num_columns:
            i += 1
            print (array[rows(i) * i])

















print_operation_table('*', 2, 5 )

