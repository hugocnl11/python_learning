from car import Car

car_1 = Car('Tesla', '3',2024, "Black")
car_2 = Car('Ferrari', 'Spyder',2018, "White")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()

print(car_1.wheels)