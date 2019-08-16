"""
This program will ask the user to input a temperature in celcius.
Then, it will convert that number into fahrenheit and print back
out the fahrenheit value
"""
# Tung Hoang - 08/16/19

# Asking user to input a number
celcius = input("C: ")

# Using a while loop to keep asking the user value until it is valid (numeric)
# The try and except function will test if the input is a float.
while True:
    try:
        temperature = float(celcius)
        """
        The str() will covert the float into string so that it can be printed
        along with other strings.
        The "{0:.2f}".format() round float to 2 decimal to avoid precision error
        """
        fahrenheit = str("{0:.2f}".format(temperature * 9/5 + 32))
        print ("F: " + fahrenheit)
        break
    except ValueError:
        print("That input is not numeric. Please try again")
        celcius = input("C: ")
