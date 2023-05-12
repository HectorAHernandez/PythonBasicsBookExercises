# contains exercises for chapter 5.5
# 1:
num = float(input("Enter a Floating-point number: "))
print(f"{num} rounded to 2 decimal places is {round(num, 2)}")

# 2:
number = float(input("Enter a number: "))
print(f"the absolute value of {int(number)} is {abs(number)}")

# 3:
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
print(f"The difference between {number1} and {number2} is an integer? {(number1 - number2).is_integer()}!")
