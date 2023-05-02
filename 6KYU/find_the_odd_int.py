def find_it(seq):
    return [num for num in seq if list(seq).count(num) % 2 != 0][0]

seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]
print(find_it(seq))