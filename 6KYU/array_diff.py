def array_diff(a, b):
    return [x for x in a if x not in b]

a = [1, 2]
b = [1]
print(array_diff(a, b))