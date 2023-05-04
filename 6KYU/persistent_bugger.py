def persistence(n):
    counter = 0
    while n > 9:
        counter+=1
        res = 1
        for i in str(n):
            res = res * int(i)
        n = res
    return counter    

n_1 = 39      # --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
n_2 = 999     # --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
n_3 = 4       # --> 0 (because 4 is already a one-digit number)

# print(persistence(n_1))
print(persistence(n_2))