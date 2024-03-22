# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "hugo Gómez"

if (name[0].islower()):
    name = name.capitalize()

fist_name = name[:4].upper()
last_name = name[5:].lower()

last_character = name[-1]

print(name)

print(fist_name)
print(last_name)
print(last_character)
