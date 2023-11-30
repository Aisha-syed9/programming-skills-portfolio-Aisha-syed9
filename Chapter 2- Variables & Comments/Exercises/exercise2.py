#Exercise 1:
message = "Hello, World!"
print("initial message:", message)
message = "welcome to Python Programming!"
print("New message:", message)


#Exercise 2:
quote = 'To live is the rarest thing in the world. Most people exist, that is all.' 
author = 'Oscar Wilde'

print(f'{author} once said, "{quote}"')

#Exercise 3:
name = "\t Aisha Ali\n"
print("Name with Whitespace:")
print(name)
print("After Strpping:")
print("Using lstrip():", name.lstrip())  # Left strip
print("Using rstrip():", name.rstrip())  # Right strip
print("Using strip():", name.strip())    # Strip from both sides

#Exercise 4:
favorite_number = 7 
message = f"My favorite number is {favorite_number}."
print(message)


#Exercise 5:
usb_price = 6
budget = 50
num_usb_sticks = budget // usb_price
remaining_budget = budget % usb_price
print("The girl can buy", num_usb_sticks, "USB sticks.")
print("She will have £", remaining_budget, "left.")
