#scope = The region that a variable is recognized
#        A variable is only avilable from inside the region it is created
#        A global and locally scoped versions of a variable can be created


name = "Pepe" # global scope (avileable inside & outside function)

def display_name():
    name = "Code" # local scope (avileable only inside the function)
    print(name)

display_name()
print(name)