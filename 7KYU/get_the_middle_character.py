def get_middle(s):
    if 0 < len(s) < 1000:
        if len(s) % 2 == 0:
            middle = int(len(s) / 2)
            result = f'{s[middle-1]}{s[middle]}'
        elif len(s) % 2 != 0:
            middle = int(len(s) / 2)
            result = f'{s[middle]}'
    return result


some_str = 'testing'

print(get_middle(some_str))