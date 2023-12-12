#Excercise 1 
topping = ''
while topping != 'quit':
    topping = input("Enter a pizza topping (or 'quit' to exit): ")
    if topping.lower() != "quit":
        print(f"I'll add {topping} to your pizza.")



#Excercise 2
while True:
    age = input("Please enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")




#Exercise 3
while True:
    print("This loop will run nonstopquit!")





#Excercise 4
sandwich_orders = ['Chicken and Cheese', 'Turkey Club', 'Tuna', 'Vegetarian']

finished_sandwiches = []

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#Excercise 5
# List of sandwich orders
sandwich_orders = [
    'Chicken and Cheese', 'Pastrami', 'Turkey Club', 'Pastrami', 
    'Tuna', 'Vegetarian', 'Pastrami', 'Pastrami'
]

# Empty list for finished sandwiches
finished_sandwiches = []

# Informing the deli has run out of pastrami
print("We're sorry, the deli has run out of pastrami.")

# Removing all occurrences of 'pastrami' from sandwich_orders
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Making sandwiches (excluding pastrami) and moving them to finished_sandwiches
for order in sandwich_orders:
    if order != 'Pastrami':  # Ensuring no pastrami sandwiches end up in finished_sandwiches
        print(f"I made your {order} sandwich.")
        finished_sandwiches.append(order)

# Displaying the finished sandwiches
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)





