try:

    with open('text.txt') as file:
        print(file.read())

    #we can check if the file is open or closed
    print(file.closed)

except FileNotFoundError as e:
    print(e)
    print("That file was not found :(")