# function = a block of code witch is executed only when it is called

def hello(first_name, last_name, age):
    for i in range(0, 5+1):
        print("Hello")
        print("My name is " + first_name + last_name)
        print("I am "+ str(age) +" years old.")

my_name = "Hugo "
my_last_name= "Gómez"
my_age = 20

hello(my_name, my_last_name, my_age)