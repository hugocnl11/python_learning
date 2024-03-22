#lists = used to store multiple items in a single variable
# The methods we will use:
#   food.append("ice cream")
#   food.remove("hotdog")
#   food.pop()
#   food.insert(0,"cake")
#   food.sort()
#   food.clear()

food = ["pizza", "hamburguers", "hotdog", "spaghetti", "pudding"]

print("\n-First List:-")
for i in food:
    print(i)

# fact: you can update the lists
food[0] = "sushi"

# fact: you can add new items with the append()
food.append("ice cream")

# fact: you can delete items with delete()
food.remove("hotdog")

# fact: .pop() can delete the last item (in this case ice cream)
food.pop()

# fact: .insert() can insert a item in the position of the index:
food.insert(0,"cake")

#fact: .sort() can sort the list in ascending order / alphabetical order
food.sort()

#fact: .clear() remove all the elemets of the list
food.clear()

print("\n-Final List:-")
for i in food:
    print(i)



