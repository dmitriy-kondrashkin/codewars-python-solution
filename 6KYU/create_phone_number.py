def create_phone_number(n):
    n_string = ''.join([str(i) for i in n])
    return f'({n_string[:3]}) {n_string[3:6]}-{n_string[6:]}'

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(n))