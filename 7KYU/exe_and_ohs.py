def xo(s):
    return s.lower().count('x') == s.lower().count('o')

s = "ooxx"
print(xo(s))