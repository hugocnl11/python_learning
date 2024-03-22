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

# how to format numbers:

number = 3.141159
number2 = 1000
print("The number pi is {:.3f}".format(number)) #hace que muestres el numero de decimales que pongas en la x (.xf)
print("The number is {:,}".format(number2)) # How to add a comma
print("The number is {:b}".format(number2)) # Bimnary number
print("The number is {:o}".format(number2)) # Octal number
print("The number is {:x}".format(number2)) # Hexadecimal lowercase
print("The number is {:X}".format(number2)) # Hexadecimal uppercase
print("The number is {:E}".format(number2)) # Sientific notation
