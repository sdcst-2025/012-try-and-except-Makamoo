#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with  a try...except 
# block so that the user will allow them to enter an integer,
# or display an error message if they enter in something else.

try:
    number = input("Please enter in an integer value")
    number = int(number)
    print(number)
except:
    print("somehing went wrong, honestly, you probably didn't listen to the intructions")