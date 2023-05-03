def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f"{' '.join(names)} likes this"
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) - len(names[:2])} others like this'


names_1 = []                                            # -->  "no one likes this"
names_2 = ["Peter"]                                     # -->  "Peter likes this"
names_3 = ["Jacob", "Alex"]                             # -->  "Jacob and Alex like this"
names_4 = ["Max", "John", "Mark"]                       # -->  "Max, John and Mark like this"
names_5 = ["Alex", "Jacob", "Mark", "Max"]              # -->  "Alex, Jacob and 2 others like this"


print(likes(names_1))
print(likes(names_2))
print(likes(names_3))
print(likes(names_4))
print(likes(names_5))