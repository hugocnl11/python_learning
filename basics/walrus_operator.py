# walrus operator :=

# new to Python 3.8
# assignament expression aka walrus operator
# assigns values to variable as part of a larger expression

# happy = True
# print (happy)

#print(happy := True)


#foods = list()
#while True:
#    food = input("What food do y like?")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

for i in foods:
    print(i)








