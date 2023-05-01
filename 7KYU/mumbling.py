def accum(s):
    result = []
    count = 0
    for letter in s:
        count += 1
        output = str(letter*count).capitalize()
        result.append(output)
    return '-'.join(result)


some_string = 'RqaEzty'
print(accum(some_string))
