# super() = Function used to give access to the methods of a parent class.
#           Return a temporary object of a parent class when used

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class Sqare(Rectangle):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        return self.lenght*self.width

class Cube(Rectangle):
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def volume(self):
        return self.lenght*self.width*self.height

square = Sqare(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())