def adder_substractor(num1, num2):
    return (num1 + num2, num1 - num2)


result1 = adder_substractor(5, 3)
print(f"result: {result1}")
print(f"adding result: {result1[0]} and substracting result: {result1[1]}")

cardinal_numbers = ("first", "second", "third")
print(f"cardinal_numbers[1]: {cardinal_numbers[1]}")

position1, position2, position3 = cardinal_numbers
print(f"position1: {position1}")
print(f"position2: {position2}")
print(f"position3: {position3}")

name = "Hector"
my_name = tuple(name)

print(f"Does the letter 'x' in my name? {'x' in my_name}")
new_name = my_name[1:]
print(f"The new tuple for my name with first character is: {new_name}")

groceries = "Eggs, plantain, sugar, salt, pepper, bread"
groceries_list_1 = groceries.split(", ")  # ", " comma and space
type(groceries_list_1)
print(f"groceries_list_1: ", groceries_list_1)

groceries_list_2 = groceries.split(",")  # "," ONLY comma, will include the space
print(f"groceries_list_2: ", groceries_list_2)
# output: ['Eggs', ' plantain', ' sugar', ' salt', ' pepper', ' bread']
# To elminate the space in front of some elements:
i = 0
for grocery in groceries_list_2:
    groceries_list_2[i] = grocery.lstrip()
    i += 1
print(f"New groceries_list_2: ", groceries_list_2)

letters = "a;b;c;d;e"
letters_list = letters.split(";")  # splitting on ";"
print(f"string letters: {letters}")
print(f"list letters_list: {letters_list}")

# splitting on space ' ':
phrase = "The quick brown fox"
words_list = phrase.split(" ")
print(f"words_list: {words_list}")

# split on multple characters "ab"
new_list = "abbaabba".split("ab")
print(f"new_list: {new_list}")

# split on multple characters "ba"
new_list = "abbaabba".split("ba")
print(f"new_list: {new_list}")

# another list with no found separator will return a list with the whole string:
list_1 = "abbaabba".split("c")
print(f"whole list not found separator: {list_1}")

numbers = [1, 2, 3, 4]
print(f"numbers[1]: {numbers[1]}")
print(f"numbers[1:3]: 2, 3 = {numbers[1:3]} ")
print(f"'Bod' is in numbers?: {'Bod' in numbers}")

# list data structures are iterable, therefore we can use for.. loop:
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is Multiple of 2")

# Changing elements in a list:
colors = ["red", "yellow", "green", "blue"]
print(f"colors list: {colors}")
colors[0] = "burgundy"
print(f"colors list: {colors}")

# Changing several values in a list at once with a slice assignment:
colors[1:3] = ["orange", "magenta"]
print(f"colors list: {colors}")

# the list assigned to a slice does NOT need to have the same length as the slice
# for example we can assign a list of three elements to a slice of two elements,
# this will create an insert of the new element in between the others:
colors = ["red", "yellow", "green", "blue"]
print(f"colors list: {colors}")
colors[1:3] = ["orange", "magenta", "aqua"]
print(f"colors list: {colors}")

# if the length of the list assigned to the slice is less than the length of the
# slice, then the overall length of the original list is reduced:
colors = ["red", "orange", "magenta", "aqua", "blue"]
print(f"colors list: {colors}")
colors[1:4] = ["yellow", "green"]
print(f"colors list: {colors}")

# The above examples show how to change, or mutate, lists using index and slice
# notation. There are also several list methods that we can use to mutate a list.
# list methods provide a more natural and readable way to mutate a list.

# list.insert(index, value): the insert method is used to insert a single new
# value into a list. It takes two parameterss, an index i and a value x, and
# inserts the value x at index i in the list:
colors = ["red", "yellow", "green", "blue"]
# to insert "orange" into the second index:
colors.insert(1, "orange")
print(f"insert 'orange' at index 1 colors list: {colors}")

# if the value for the index parameter of .insert() method is larger than the
# greatest index in the list, then the value is inserted at the end of the list
colors.insert(22, "violet")
print(f"insert 'violet' at index beyond the list length: {colors}")

# We can use a negative index to insert from the last element in the list.
# Example to insert in the position of the current last element of the list and
# move the last element to the right:
colors.insert(-1, "indigo")
print(f"insert 'indigo' at index where the last element -1 is : {colors}")

# if we can insert an element at a specific index, then it makes sense that we
# can also remove an element at a specific index using the list.pop method.
# list.pop() method:
# takes on parameter, an index i, and removes the value from the list at that
# index. The value that is removed is returned by the method:
# colors: ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
removed_color = colors.pop(3)  # removes color green and returned into the variable
print(f"pop(3) removes 'green' at index 3: {colors}")

# Unlike .insert(), Python raises an IndexError if we pass an argument to
# .pop() that is larger than the last index:
# removed = colors.pop(99)

""" Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    colors.pop(20)
IndexError: pop index out of range"""

# To remove that last element in the lis we can use negative index (-1):
# ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']
removed_last_element = colors.pop(-1)
print(f"pop(-1) removes last element 'violet': {colors}")

# if we don't pass a value to the .pop() method, it removes the last item in
# the list, 'indigo' in this case:
# ['red', 'orange', 'yellow', 'blue', 'indigo']
remove_indigo = colors.pop()
print(f"pop() removes the last element 'indigo': {colors}")

# Removing the last element by calling .pop() with no specified index is
# generally considered the most Pythonic approach.

# list.append(): the .append() method is used to append a new element to the
# end of a list:
colors.append("indigo")
print(f".append('indigo') append 'indigo' to the end of the list: {colors}")
# calling .append() increase the length of the list by one an inserts the value
# 'indigo' into the final slot. Note that .append() alter the list in place,
# just like .insert()
# Using .append() is equivalent to inserting an element at an index greater
# than or equal to the length of the list. The above example could also have
# been written as follows
colors.insert(len(colors), "indigo")
print(f".append('indigo') append 'indigo' again using insert()t: {colors}")
# Using .append() is both shorter and more descriptive than using .insert() and
# it is considered the more Pythonic way of adding an element at the end of a
# list.

colors.pop()
print(f".pop() to delete 'indigo' again from end of the list: {colors}")

# list.extend(): method is used to add several new elements to the end of a list
colors.extend(["violet", "ultraviolet"])
# .extend() takes a single parameter that must be an iterable type. The elements
# of the iterable are appended to the end of the list in the same order that
# they  appear in the argument passed to .extend()
print(f".extend() to add several items [in a list] to the end of a list: {colors}")

colors.extend(("tuple_1", "tuple_2", "tuple_3"))
print(f".extend() to add several items (in a tuple) to the end of a list: {colors}")

# just like .insert() and .append(), the .extend() method alters the list in
# place. Tipically, the argument passed to .extend is another [list], but it
# could be a (tuple) like indicated above.

# Python has three useful built-in functions for working with lists of numbers:
# List of Numbers:
# On very common operation with list of numbers is to ADD UP all the values to
# get the total. Normally we can get this by using a for...loop, but Python has
# the sum() built-in function:
# with for ... loop:
nums = [1, 2, 3, 4, 5]
total = 0
for number in nums:
    total += number
print(f"numeric list: {nums}")
print(f"Calculated Total: {total}")

# now using the Python sum() built-in function
total = sum(nums)
print(f"Using sum() built-in function --> Total: {total}")
# The built-in sum() function takes a list as an argument and returns the
# total of all the values in the list:
# mixed_list = [1  , "ss", 2, "av",  3, 4, 5]  # this will generate "TypeError:
# unsupported operand type(s) for +: 'int' and 'str'" when using sum() function
# because the list contains values that are not numeric.
# sum(mixed_list)

# Beside sum(), Python has two other useful bullt-in functions for working with
# lists of numbers: min() and max(). These functions return the minimum and
# maximum values in the numeric list:
nums = [1, 2, 3, 4, 5]
print(f"Minimum in list: {min(nums)}")
print(f"Maximum in list: {max(nums)}")

# sum(), min() and max() also work with tuples:
nums_tuple = (1, 2, 3, 4, 5)
print(f"Tuple sum(nums_tuple): {sum(nums_tuple)}")
print(f"Tuple min(nums_tuple): {min(nums_tuple)}")
print(f"Tuple max(nums_tuple): {max(nums_tuple)}")

# List Comprehensions:
""" Yet another way to create a list from an existing iterable is with a
cha09-01_Exercises.py: """
numbers = (1, 2, 3, 4, 5)
squares_list = [num**2 for num in numbers]
print(f"squares_list: {squares_list}")
"""A list Comprehension is a shorthand for a 'for... loop' In the example
above , a tuple literal containing five numbers is created and assigned to the
numbers variable. On the second line, a List Comprehension loops over each number
in numbers tuple, square each number, and add/append it to a new list called
squares_list.
Creating the squares_list using a traditional for...loop involves creating an
empty list, looping over the numbers in the tuple numbers, and appending the
square of each numbr to the list: """
numbers = (1, 2, 3, 4, 5)
square_list = []
for num in numbers:
    square_list.append(num**2)
print(f"old way created square_list: {square_list}")

# List Comprehensions are commonly used to convert values in a list to a
# different type. For instance, suppose you needed  to convert a list of
# strings contaning floating-point values to a list of float objects. The
# following List Comprehension achieve this:
string_numbers = ["1.5", "2.3", "5.25"]
float_numbers_list = [float(value) for value in string_numbers]
print(f"Float_numbers_list: {float_numbers_list}")

"""List Comprehensions are not unique to Python, but they are one of its many
beloved features. if you find yourself creating an empty list, looping over
some other iterable, and appending new items to the empty list, then chances
are you can replace your code witha List Comprehension"""
