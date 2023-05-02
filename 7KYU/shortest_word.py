def find_short(s):
    return len(min(s.split(), key=len))

s = "bitcoin take over the world maybe who knows perhaps"
print(find_short(s))