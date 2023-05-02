def filter_list(l):
    return [i for i in l if type(i) == int]
    

filt = [1, 2, 'a', 'b']
print(filter_list(filt))