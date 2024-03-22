# tuple =   collection with is ordered and unchangeable
#           used to group together related data

student = ("Hugo", 20, "Male")

#print(student.count("Hugo"))
#print(student.index("Male"))

for x in student:
    print(x)

if "Hugo" in student:
    print("\nHis name is Hugo")