#kwargs = parameter that will pack all arguments into a dictionary
#         usefull so that function can accept a verying amount of keyword arguments

def hello (**kwargs):
    #print("Hello " +kwargs['fist']+ " "+kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title ="Mr." ,fist="Hugo", middle = "Gomez", last="Lopez")