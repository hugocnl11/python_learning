#2D lists = list of lists

drinks = ["coffe", "soda", "tea"]
dinner = ["pizza", "hamburguer", "hotdog"]
dessert = ["cake", "ice cream"]

menu = [drinks, dinner, dessert]

#to print the menu
print("\n- Menu:")
for i in menu:
    print(i)


#to print a sigle item of an a selected list
print("\n- Item selected:")
print(menu[0][1])
print(menu[1][0])
print(menu[2][1])


