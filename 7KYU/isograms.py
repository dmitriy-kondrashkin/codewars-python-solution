def is_isogram(string):
    return len(string) == len(set(string.lower()))

variab = "mosee"
print(is_isogram(variab))