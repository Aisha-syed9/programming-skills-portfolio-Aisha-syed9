#Excercise 1
person = {
    'first_name': 'Mike',
    'last_name': 'sweden',
    'age': 30,
    'city': 'New York'
}

print("First Name:", person['first_name'])
print("Last Name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])


#Exercise 2
glossary = {
    'variable': 'A named location in memory used to store data.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code until a specified condition is met.',
    'conditional': 'A statement that performs different actions based on whether a condition is true or false.',
    'list': 'A collection of items, stored in a specific order.'
}

for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(f"{meaning}\n")


#Excercise 3
glossary = {
    'variable': 'A named location in memory used to store data.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code until a specified condition is met.',
    'conditional': 'A statement that performs different actions based on whether a condition is true or false.',
    'list': 'A collection of items, stored in a specific order.'
}

for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(f"{meaning}\n")

glossary['dictionary'] = 'A collection of key-value pairs.'
glossary['tuple'] = 'An ordered, immutable collection of elements.'
glossary['set'] = 'An unordered collection of unique elements.'
glossary['module'] = 'A file containing Python code.'
glossary['method'] = 'A function that belongs to an object.'

print("Updated Glossary:")
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(f"{meaning}\n")


#excercise 4
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nNames of rivers included in the dictionary:")
for river in rivers:
    print(river)

print("\nNames of countries included in the dictionary:")
for country in rivers.values():
    print(country)


#Exercise 5
pet1 = {'animal': 'Dog', 'owner': 'Winter'}
pet2 = {'animal': 'Cat', 'owner': 'Aisha'}
pet3 = {'animal': 'Rabbit', 'owner': 'Tania'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()  # Empty line for better readability













