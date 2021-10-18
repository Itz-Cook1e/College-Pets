# Assignment:
# Build a list of tuples, where each tuple has info about one pet - type, name, and color. For example, 
# animals = [('dog','Fort','brown'),('cat','Tiger','tabby')] This is a list (notice it is in square brackets) containing 2 items. 
# Each item is a tuple (notice the parentheses) containing that pet's information. Put at least 5 animals (of your choice) in your list. 
# Loop through your list and print it out in this format: Fort is a brown dog Tiger is a tabby cat
# Also, prompt me to enter one of those colors, and print out all of the pets that are that color.
# Finally, prompt me to enter one of the pet types, and print out all of the pets of that type. 

# Note: I did not do the "Finally, prompt me to enter one of the pet types, and print out all of the pets of that type." as I ran out of time. 

pets = [('dog', 'Fort', 'brown'), ('dog', 'Nutmeg', 'brown'), ('cat', 'Oreo', 'black'),
('dog', 'Taco', 'white'), ('cat', 'Menolly', 'calico'), 
('snake', 'Python', 'green'), ('penguin', 'Linux', 'black'), ('bat', 'Riley', 'yellow'), 
('giraph', 'Apache', 'yellow'), ('duck', 'Greg', 'white'), ('goat', 'Asher', 'tan'),
('bunny', 'Violet', 'purple'), ('dolphin', 'Lou', 'grey'), ('sponge', 'Margaret', 'tan'),
('bird', 'Derik', 'purple'), ]

print('PETS')
for pet in pets:
    print(f'{pet[1]} is a {pet[2]} {pet[0]}')

colors = ['Brown', 'Black', 'White', 'Calico', 'Green', 'Yellow', 'Purple', 'Grey', 'Tan']

animal_dict = {'Brown':('Fort', 'Nutmeg'), 'Black':('Linux', 'Oreo'), 'White':('Taco', 'Greg'), 'Calico':('Menolly'), 'Green':('Python'), 'Yellow':('Riley', 'Apache'), 'Purple':('Violet', 'Derik'), 'Grey':('Lou'), 'Tan':('Asher', 'Margaret')}

print( )

requested_color1 = input('Please choose one of the above colors: ')
requested_color2 = requested_color1.title()

dont_join = ['Calico', 'Green', 'Gray']

if requested_color2 in animal_dict:
    if requested_color2 in dont_join:
        print(f'{animal_dict[requested_color2]} is {requested_color2.lowBrowner()}.')
    else:
        print(" and ".join(animal_dict[requested_color2]) + ' are ' + requested_color2.lower() + '.')
else:
    print(f'{requested_color2} is not one of the colors!')
    
 # Comment with name, date, and assignment name redacted
