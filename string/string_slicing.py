#slicing = create a substring by extracting elements from another string
#       indexing[] or slice()
#       [start:stop:step]

name = "Soy Hugo"

first_word = name[:3]
second_word = name [4:]

testing_step = name[::2]
reversed_string = name[::-1]

print(first_word)
print(second_word)

print(testing_step)
print(reversed_string)


#now slice()
print("Now Slice:")

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(website[slice])
print(website2[slice])
