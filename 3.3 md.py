def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['hi', False , 4]
values_list_2 = [54.32, 'Строка']

print_params()

print_params(4, 5, 78)

print_params('stroka', False)

print_params(b = 25)

print_params( c = [1, 2, 3])

print_params(*values_list)

print_params(*values_list_2, 42) # работает проверила


def print_params(**kwargs):
    print(kwargs)


values_dict = {'a': 2, 'b': 78, 'c': 5}

print_params(**values_dict)