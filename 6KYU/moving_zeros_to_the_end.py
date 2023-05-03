def move_zeros(lst):
    zeros = [x for x in lst if x == 0]
    numbers = [x for x in lst if x != 0]
    return numbers+zeros


lst = [1, 0, 1, 2, 0, 1, 3]
print(move_zeros(lst))