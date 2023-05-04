# Solution 1

def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f'{h:0>2}:{m:0>2}:{s:0>2}'


# Solution 2

def make_readable(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds//3600, seconds//60 % 60, seconds % 60)


# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59

seconds_1 = 5                   #     --> "00:00:05"
seconds_2 = 60                  #     --> "00:01:00"
seconds_3 = 86399               #     --> "23:59:59"
print(make_readable(seconds_2))