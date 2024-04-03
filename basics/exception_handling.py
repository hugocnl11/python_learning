#exception = event detected during execution that interript the flow of a program

#examples:
#ZeroDivisionError: Se produce cuando intentas dividir un número por cero.
#TypeError: Se produce cuando se utiliza un tipo de dato incorrecto en una operación.
#ValueError: Se produce cuando una función recibe un argumento con un valor incorrecto.
#NameError: Se produce cuando intentas acceder a una variable o función que no está definida.
#FileNotFoundError: Se produce cuando intentas acceder a un archivo que no existe.
#...

try:
    numerator = int(input("Enter a number to devide: "))
    denominator = int(input("Enter a number to deviide by:"))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
else:
    print(result)
finally:
    print("This will always execute")