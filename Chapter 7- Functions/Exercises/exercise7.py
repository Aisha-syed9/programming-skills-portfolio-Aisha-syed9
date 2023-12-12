#Exercise 1

def display_message():
    print("In this chapter, I am learning about Python functions and how to define and call them.")

#Calling the function to display the message
display_message()
 

#Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

#Calling the function and providing a book title as an argument
favorite_book("Alice in Wonderland")


#Exercise 3
def make_shirt(size, message):
    print(f"A {size} shirt will be created with the following message: '{message}'.")

#Calling the function using positional arguments
make_shirt("medium", "Catch Flights Not Feelings")  

#Calling the function using keyword arguments
make_shirt(size="large", message="Be Kind, Rewind")


#Exercise 4
def make_shirt(size='large', message='I love Python'):
    print(f"A {size} shirt will be created with the following message: '{message}'.")

#Creating a large shirt with default message
make_shirt()

#Creating a medium shirt with default message
make_shirt('medium')

#Creating a shirt of any size with a different message
make_shirt('small', 'Keep Calm and Code On')









