class Car:

    color = None

class Motorcycle:

    color = None

def change_color(car, color):
    car.color = color
    print("Your vehicle is "+color)

car_1=Car()
car_2=Car()
car_3=Car()

bike_1 = Motorcycle()

change_color(car_1, "Red")
change_color(car_2, "Blue")
change_color(car_3, "White")

change_color(bike_1, "Aluminium")


