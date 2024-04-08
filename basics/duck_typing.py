#   duck typing =   concept where the class an object is less important than the methods/attributes
#                   that class type is not checked if minum methods/attributes are present
#                   "If itn walks like a duck, and it quacks like a duck, then it must be a duck"
#

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:

    def catch(self, duck):
            duck.walk()
            duck.talk()
            print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

#duck.talk()
#duck.walk()
#chicken.walk()
#chicken.talk()

person.catch(duck)

