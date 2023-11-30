#Exercise 1
names = ["Hiba", "Tania", "Rio", "Noah", "Sophia"]

for name in names:
    print(name)








#Exercise 2:
names = ["Hiba", "Tania", "Rio", "Noah", "Sophia"]

message_template = "Hello, {name}! I hope you're having a great day."

for name in names:
    personalized_message = message_template.format(name=name)
    print(personalized_message)








#Exercise 3

#List of favorite modes of transportation (motorcycles and cars)
favorite_transportation = ['Honda motorcycle', 'Kawasaki ninja motorcycle', 'Fortuner car', 'Toyota Yaris car']

#Printing statements about these transportation items
for transport in favorite_transportation:
    print(f"I would like to own a {transport}.")










#Excercise 4

guests = ['vincent van Gogh', 'Johannes Vermeer', 'Leonardo da Vinc']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")











#Excersice 5
#Invite some people to dinner.
guests = ['vincent van Gogh', 'Johannes Vermeer', 'Leonardo da Vinc']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")


name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

#Johannes can't make it! Let's invite Rembrandt instead.
del(guests[1])
guests.insert(1, 'Rembrandt')

#Print the invitations again.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")












#Excercise 6
#Invite some people to dinner.
guests = ['vincent van Gogh', 'Johannes Vermeer', 'Leonardo da Vinc']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")


name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

#Johannes can't make it! Let's invite Rembrandt instead.
del(guests[1])
guests.insert(1, 'Rembrandt')

#Print the invitations again.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)










#Excercise 7
locations = ['japan', ' italy', 'turkey', 'switzerland', 'greece']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)



























