# A list and documentation on all Python exceptions can be found at:
#           https://docs.python.org/3/library/exceptions.html

# this program is for handling exception errors by anticipating the an error type
# for possible occurance and using the Try...except blocks to catch the error,
# avoiding the program to crash, and taking some actions.
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print(f"That was not an integer")


# handling multiple exception types by separating the exception names with commas
# and putting the list of names in parentheses:
def divide_1(num1, num2):
    try:
        print(f" divide_1 result {num1 / num2}")
    except (TypeError, ZeroDivisionError):
        print("Encountered a problem")


divide_1(40, 2)
divide_1("lsls", 4)
divide_1(40, 0)


def divide_2(num1, num2):
    try:
        print(f"divide_2 result: {num1 / num2}")
    except TypeError:
        print(f"divide_2: Both arguments must be numbers")
    except ZeroDivisionError:
        print(f"divide_2: second argument must NOT be zero")


divide_2(424, 4)
divide_2(44, "rse")
divide_2(65, 0)

# the Bare "except" clause:
# we can use the except keyword by itself without naming specific exception:
try:
    print("this replace a lot of hazardous code lines that may break execution")
except:
    print("Something bad happened")
# if any exception is rased while executing the code in the try block, then the
# except block will run and the message "Something bad happened" will displayed.
# This might sound lke a great way to ensure our program never crashes, but this
# is actually a bad idea and the pattern is generally frowned upon!!!
# There are a couple of reasons for this, but the most important reason for new
# programmers is that catching every exception could hide bugs in your code,
# giving you a false sense of confidence that your code works as expected.
# If you catch only specific exceptions, then unexpected errors are encountered,
# Python will print the traceback and error details, giving you more information
# to work with when debugging your code.

# Exercises:
# 1:
while True:
    try:
        int_number = int(input("Enter an integer number: "))
        print(f"You entered integer number: {int_number}")
        break
    except ValueError:
        print("Please, try again")

# 2:
string1 = input("Enter a string: ")
while True:
    try:
        index_1 = int(input("Enter the location of the letter to display: "))
        print(f"The character at index[{index_1}] is '{string1[index_1]}'")
        break
    except ValueError:
        print("The location must be an integer number, Try again...")
    except IndexError:
        print("The location you provided is beyond of the string length")
