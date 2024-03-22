# srt.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item)) #positional argument
print("The {animal} jumped over ther {item}".format(animal = "cow", item="moon")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))


#to add padding
name = "Hugo"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10} Nice to meet you".format(name))
print("Hello, my name is {:<10} Nice to meet you".format(name))
print("Hello, my name is {:>10} Nice to meet you".format(name))
print("Hello, my name is {:^10} Nice to meet you".format(name))