# 1:
def cube(number):
    """Returns the value of the number parameter raised to the third power"""
    return number**3


print("cube of number 5 is: ", cube(5))
print(f"cube of number 100 is {cube(100)}")
print(f"cube of number 6 is {cube(6)}")
print(f"cube of number 4 is {cube(4)}")


# 2:
def greet(name):
    """print a greet using the parameter name ."""
    print(f"Hello, {name}!!!!!!")


greet("Hector")
greet("Leopoldo")
greet("Aldo")


# challenge exercises:
def convert_celcius_to_far():
    """ Prompt to enter a temperature in Celcius degrees and converts it to \
Fahrenheit degrees """
    degrees_cel = float(input("Enter a temperature in digrees Celcius: "))
    far = degrees_cel * 9 / 5 + 32
    print(f"{degrees_cel} degrees Celcius = {far: .2f} degrees Fahrenheit")


def convert_fahrenheit_to_celcius():
    """ Prompt to ente a temperature in Fahrenheit and converts it to \
Celcius degrees"""
    degrees_far = float(input("Enter a temperature in Fahrenheit degrees: "))
    celcius = (degrees_far - 32) * 5 / 9
    print(f"{degrees_far} degrees Fahrenheit = {celcius: .2f} degrees Celcius")


convert_celcius_to_far()
convert_fahrenheit_to_celcius()
