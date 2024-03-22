#while loop = a statement that will execute it's block of code,
#             as log as it's condition remains true

name = ""

while len(name)==0:
    name = input("Enter your name: ")

print("Hello "+name)


# another way to do:

#name = None
#
#while not name:
#    name = input("Enter your name: ")
#
#print("Hello "+name)
