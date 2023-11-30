#Write a Python program to print the following string in a specific format.
print('Twinkle, twinkle, little star,'+
	   'How I wonder what you are!'+
	   'Up above the world so high,'+ 		
	   'Like a diamond in the sky.'+ 
       'Twinkle, twinkle, little star,'+ 
	   'How I wonder what you are')


#Write three strings in different variables and print the output as one string.
a = "Hello"
b = "Big"
c = "World"
print('a + b + c + "!"')


#Write a Python program to display the current date and time.
import datetime 
now = datetime.datetime.now()
print ("Current date and time : , current_datetime")


#Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi 
r = float(input ("input the radius of the circle :"))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


#Write a Python program to get the Python version you are using.
import sys
print("System version")
print(sys.version)
print("version info")
print(sys.version_info)