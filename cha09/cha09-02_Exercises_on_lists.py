# 1: Create a list called food with elements rice and beans:
food = ["rice", "beans"]

# 2: Append the string "broccoli" using .append() method:
food.append("broccoli")

# 3 Add the strings 'bread' and 'pizza' to food using .extend:
food.extend(["bread", "pizza"])

# 4: print the first 2 items in the list using print() and slice notation:
print(f"the first two items in the food list are: {food[0:2]}")

# 5: print the last item in the list using print() and index notation:
print(f"The last item in the food list is: {food[-1]}")

# 6: Create a list called breakfast from the string
# "eggs, fruit, orange juice" using .split method.
breakfast_list = "eggs, fruit, orange juice".split(", ")
print(f"Breakfast list: {breakfast_list}")

# 7: Verify that breakfast list has three items using len():
print(f"breakfast_list contains 3 items = {len(breakfast_list)}")

# 8: Create a new list called lengths using a list comprehension that
# contains the lengths of each string in the breakfast_list:
lengths = [len(delicious_item) for delicious_item in breakfast_list]
print(f"lengths list: {lengths}")

# Nesting Lists and Tuple:
""" Lists and tuples can contain values of any type. That means lists and tuple
can contain lists and tuples as values. A nested list or tuple is a list or
tuple that is contined as a value in another list or tuple. For example:"""
two_by_two = [[1, 2], [3, 4]]
print(f"two_by_two[0] --> [1, 2]: {two_by_two[0]} ")
print(f"two_by_two[1] --> [3, 4]: {two_by_two[1]} ")

# we can use the double index notation to access an element in the nested list:
print(f"two_by_two[1][0] --> 3 = {two_by_two[1][0]}")

""" First, Python evaluates two_by_two[1] and returns [3, 4]. Then Python
evaluate [3, 4][0] and return the first element, 3.
In very loose way, you can think of a list of lists or tuple of tuples as a
sort of a tablewith rows and column. This table analogy is only an informal way
of thinking about a list of lists, though. for example, there is no requirement
that all the lists in a list of lists have the same length, in which case this
table analogy starts to break down. Therefor, it is bettter seen it as first
described, this is Python evaluating the first list with the first index, and
then from there evaluating that first results with the second index"""

# practicing using double, triple index notation:
print("*** practicing using double, triple index notation ***:")
t1 = [[1, 10], [2, 20, 200, 2000], [3, 30, 300], [4, 345, 45]]
print(f"t1 --> {t1}")
print(f"t1[1][2] --> 200 = {t1[1][2]}")
print(f"t1[1][3] --> 2000 = {t1[1][3]}")
print(f"t1[3][1] --> 345 = {t1[3][1]}")
print(f"t1[3][0] --> 4 = {t1[3][0]}")

t2 = [[1, "hello", ["a", "b34tol", 3]], ["Hector", 25, [5, "last"]]]
print(f"t2 --> {t2}")
print(f" t2[1] --> ['Hector', 25, [5, 'last']] = {t2[1]}")
print(f"t2[1][2][1] --> 'last' = {t2[1][2][1]}")

print(f"t1 = {t1}")
# >>> t1[0][2][3]
# Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
#    t1[0][2][3]
# IndexError: list index out of range
# >>> t1[0][1][3]
# Traceback (most recent call last):
#  File "<pyshell#12>", line 1, in <module>
#    t1[0][1][3]
# TypeError: 'int' object is not subscriptable
print(f"t1[1][3] --> 2000 = {t1[1][3]}")
print(f"t1[3][1] --> 345 = {t1[3][1]}")
print(f"t2 --> {t2}")
t2.append("Hernandez")
print(f"** Executed: t2.append('Hernandez') **")
print(f"t2 --> {t2}")
print(f"t2[-1] --> 'Hernandez' = {t2[-1]}")
print(f"t2[2] --> 'Hernandez' = {t2[2]}")

# >>> t2.insert[1:2] = "inserted"
# Traceback (most recent call last):
#  File "<pyshell#19>", line 1, in <module>
#    t2.insert[1:2] = "inserted"
# TypeError: 'builtin_function_or_method' object does not support item assignment
# >>> t2.insert[1:2] = ["inserted"]
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#    t2.insert[1:2] = ["inserted"]
# TypeError: 'builtin_function_or_method' object does not support item assignment

# now fixing the error with .insert(index, value):
t2.insert(2, "inserted")
print(f"** Executed t2.insert(2, 'inserted')")
print(f"t2 --> {t2}")

# removing the inserted value:
t2.pop(2)
print(f"** Executed t2.pop(2) **")
# remove and displayed --> 'inserted'
print(f"t2 --> {t2}")

# inserting now in index # 1:
t2.insert(1, "inserted")
print(f'** Executed t2.insert(1, "inserted")')
print(f"t2 --> {t2}")

print(f"t2[2] --> ['Hector', 25, [5, 'last']] = {t2[2]}")
print(f"t2[1] --> 'inserted' = {t2[1]}")
print(f"t2[2][2][1] --> 'last' = {t2[2][2][1]}")
print(f"t2[2][1] --> 25 = {t2[2][1]}")

# using List Comprehension and double, triple index notation:
print(f"t2 --> {t2}")
print(f"[item for item in t2] --> {[item for item in t2]}")
# displays: [[1, 'hello', ['a', 'b34tol', 3]], 'inserted', ['Hector', 25, [5, 'last']], 'Hernandez']
print(f"[item2 for item2 in t2[1]] --> {[item2 for item2 in t2[1]]}")
# displays: ['i', 'n', 's', 'e', 'r', 't', 'e', 'd']
print(
    f"[item for item in t2[2]] --> ['Hector', 25, [5, 'last']] = \
{[item for item in t2[2]]}"
)
# item for item in t2[2][2]    # missing the [] to create the list.
# SyntaxError: invalid syntax
# another one with error:
# item for item in t2    # missing the [] to create the list.
# SyntaxError: invalid syntax
print(f"[item for item in t2[2][2]] --> [5, 'last'] = {[item for item in t2[2][2]]}")

print()
print()
# Copying a List:
# sometime we need to copy one list into another list. However, we can not just
# reassign one list object to another list object because we will get a
# surprising result:
animals = ["lion", "tiger", "Cheeta"]
print(f"orignal animals list: {animals}")
large_cats = animals
large_cats.append("Tigger")  # change to the copied list will affect the original
print(f"large_cats list: {large_cats}")
print(
    f"original animals list: {animals} was affected by the change in \
large_cats"
)
print(f"animals and large_cats reference the same object?? {animals is large_cats}")
print(f"animals and large_cats have the same content?? {animals == large_cats}")
# the above is a quirk of object-oriented programming, but it is by design. when
# we say "large_cats = animals", the large_cats and animals variables both refer
# to the memory address of the same object. A variable name is really just a
# reference to a specific location in computer memory. Instead of copying all
# the contents of the list object and creating a new list, "large_cats = animals"
# assigns the momory location referenced by "animals" to "large_cats". That is,
# now both variables now refer to the same object in memory, and any changes
# made to one will affect the other.

# To get an independent copy of teh animals list, we can use slice notation to
# return a new list with the same values:
animals = ["lion", "tiger", "Cheeta"]
large_cats_2 = animals[:]  # [:] slice from index 0 to -1 (the last)
print(
    f"animals and large_cats_2 reference the same object?? \
{animals is large_cats_2}"
)
large_cats_2.append("leopard")
print(
    f"animals and large_cats_2 have the same content?? \
{animals == large_cats_2}"
)
""" Since no index numbers are specified in the [:] slice, every element of the
list is returned from the beginning to end. The large_cats_2 list now has the
same elements as animals, and in the same order, but we can .append() items to
it without changing the list assigned to animals"""

# if we want to make a copy of a list of list, then we can do so using the [:]
# notation we saw earlier:
matrix1 = [[1, 2], [3, 4]]
matrix2 = matrix1[:]  # copy content of matrix1 and create a new object.
print(f" matrix1 and matrix2 are the same object?? False = {matrix1 is matrix2}")
print(
    f"Does the first list in matrix1 is the same object in matrix2?? \
True {matrix1[0] is matrix2[0]}"
)
print(
    f"Does the second list in matrix1 is the same object in matrix2?? \
True {matrix1[1] is matrix2[1]}"
)
matrix2[0] = [5, 6]  # changing the whole list's element in matrix2 does not
# affect the first element (whole list) in matrix1
print(f"changed matrix2 --> [[5, 6], [3, 4]] = {matrix2}")
print(f"Not changed matrix1 --> [[1, 2], [3, 4]] = {matrix1}")

# let's see what happen when we change the first element of the second list
# in matrix2:
matrix2[1][0] = 1
print(f"matrix2 --> [[5, 6], [1, 4]] = {matrix2}")
print(f"matrix1 --> [[1, 2], [1, 4]] = {matrix1}")
# notice that the second list in matrix1 was also changed/altered!!!
# This happens because a list doesn't really contain objects themselves, but
# references to those objects in memory, the [:] returns a nw list containing
# the same references as the original list. In programming jargon, this method
# of copying a list is called a "shallow copy"

# To copy a list and all its elements, we must make what is known as a
# "deep copy". A deep copy is a truly indempendent copy of an object. To make
# a deep copy of a list, we can use the deepcopy() built-in function from the
# Python's copy module:
import copy

matrix3 = copy.deepcopy(matrix1)
matrix3[1][0] = 3  # changing the first element in second list, now only
# affect matrix3.
print(
    f"After changing second list's  first element in matrix3 {matrix3} \
[[1, 2], [3, 4]] = "
)
print(f"And matrix1 did not change [[1, 2], [1, 4]] = {matrix1}")
print(
    f"Does matrix3 second list is the same object than matrix1??? \
False = {matrix3[1] is matrix1[1]}"
)
print(f"object number of matrix3 second list: {id(matrix3[1])}")
print(f"object number of matrix1 second list: {id(matrix1[1])}")

# matrix3 is created as a "deep copy" of matrix1. Therefore, When we change
# an element of matrix3, the corresponding element of matrix1 doesn't change.

print()
print("**** S O R T *****")
# Sorting Lists:
""" Lists have a .sort() method that sorts all of the items in ascending
order. By default, the list is sorted in alphabeical or numerical order
depending on the type of the elements in the list"""
# Lists of strings are sorted alphabetically:
colors = ["red", "yellow", "green", "blue"]
colors.sort()
print(f"colors list: {colors}")

# Lists of numbers are sorted numerically:
numbers = [1, 10, 5, 3]
numbers.sort()
print(f"numbers list: {numbers}")

# Notice that .sort() sorts the list in place, so no need to assign its result
# to anything.
""" .sort() has an optional parameter called 'key' that can be used to adjust
how the list gets sorted. The 'key' parameter accepts a function, and the list
is sorted based on the return value of that function.

For example, to sort a list of strings by the length of each string element,
we can pass the 'len' function to 'key': """
colors = ["red", "yellow", "green", "blue"]
colors.sort(key=len)
print(f"colors sorted by length of each element: {colors}")

# We don't need to call the function when you pass it to key. Pass the
# function's name without any parameters. For instance, in the previous
# example the name 'len' is passed to 'key', not len().
# *** very important: The function that gets passed to 'key' must accepts only
# a single argument (which can be a list, tuple, dictionary)
""" We can also pass user-defined functions to 'key'. in the following example
a function called get_second_element() is used to sort a list of tuples by
their second elements: """


def get_second_element(item):
    print(f"item: {item} and item[1]: {item[1]}")
    return item[1]


items = [(4, 1), (1, 2), (-9, 0)]
print(f"items original: {items}")
items.sort(key=get_second_element)
print(f"item sorted by second element: {items}")


def get_first_element(tuple_item):
    print(f"tuple_item: {tuple_item} and first element: {tuple_item[0]}")
    return tuple_item[0]


items_2 = [(4, 1), (1, 2), (-9, 0)]
print(f"items_2 original: {items_2}")
items_2.sort(key=get_first_element)
print(f"items_2 sorted by first element: {items_2}")
