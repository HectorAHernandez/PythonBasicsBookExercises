def multiply(x, y):
    """ Returns the product of two numbers x and y. This is a simple \
one so that you can practice the Docstring"""
    product = x * y
    print("product:", product)
    return product
    print("you can't see me because print is after the return")


multiply(4, 6)


def greet(name):
    print("Hello,", name)


greet("Thompson")


# Error when calling the user defined function before it is defined:
# num = add(4, 5)
# print("num:", num)


def add(a, b):
    return a + b
