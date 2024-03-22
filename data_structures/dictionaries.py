#dictionary = A changeable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to acces a value quickly

capitals = {'USA': 'Washington',
            'Spain': 'Madrid',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# adding news
capitals.update({'Germany':'Berlin'})
# updating an existing one
capitals.update({'USA':'Las Vegas'})
# to remove one we use .pop('Key')
capitals.pop('China')

#print(capitals['Germany'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

#to print a dictionary in python
print("\n-Dictionary: ")
for key,value in capitals.items():
    print(key,value)