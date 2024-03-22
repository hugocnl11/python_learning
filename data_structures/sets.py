# set = colletion wich is unsortered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()


#you can update the set ustensiles adding all the disher
#utensils.update(dishes)
print("\n- Utensils:")
for x in utensils:
    print(x)

print("\n-Dishes:")
for x in dishes:
    print(x)

#you can make the same using a new set+ using the union of another 2 sets
dinner_table = utensils.union(dishes)
print("\n- Dinner table:")
for x in dinner_table:
    print(x)

print("\n-Diferences of dishes tan utensils:")
print(dishes.difference(utensils))

print("\n-Duplicated items in this lists (dishes, utensils):")
print(dishes.intersection(utensils))


