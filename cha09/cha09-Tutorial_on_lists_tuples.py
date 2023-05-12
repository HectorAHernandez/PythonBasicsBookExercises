# Lists that have the same elements in a different order are not the same:
a = ["foo", "bar", "baz", "qux"]
print(a)
# ['foo', 'bar', 'baz', 'qux']

b = ["baz", "qux", "bar", "foo"]
print(f"{a == b} --> False")

print(f"{a is b} --> False")

x = [1, 2, 3, 4]
y = [4, 1, 2, 3]
print(f"{x == y} -- False")

# List with elements of varying types:
a = [21.42, "foobar", 3, 4, "bark", False, 3.14159]
print(f"A list with elements of different types: {a}")


# Lists can even contain complex objects, like functions, classes, and modules,
# which you will learn about in upcoming tutorials:

# >>> int
# <class 'int'>
# >>> len
# <built-in function len>


def foo():
    pass


print(f"foo --> {foo}")
# <function foo at 0x035B9030>

import math

print(f"imported function 'math' --> {math}")
# <module 'math' (built-in)>

a = [int, len, foo, math]
print(f"The list 'a' with functions, classes.. {a}")
# [<class 'int'>, <built-in function len>, <function foo at 0x02CA2618>,
# <module 'math' (built-in)>]

# A list can contain any number of objects, from zero to as many as your
# computer's memory will allow:
list_a = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
]

# (A list with a single object is sometimes referred to as a singleton list.)

# List objects needn't be unique. A given object can appear in a list
# multiple times:
list_a = ["bark", "meow", "woof", "bark", "cheep", "bark"]
print(f"List_a with repeating element 'bark': {list_a}")

""" List Elements Can Be Accessed by Index
Individual elements in a list can be accessed using an index in square
brackets. This is exactly analogous to accessing individual characters in a
string. List indexing is zero-based as it is with strings.
Consider the following list:"""
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"list a --> {a}")
print(f"a[0] --> 'foo' = {a[0]}")
print(f"a[5] --> corge = {a[5]}")

# Virtually everything about string indexing works similarly for lists. For
# example, a negative list index counts from the end of the list:
print(f"a[-1] --> last element --> corge = {a[-1]}")
print(f"a[-2] --> 'quux' --> {a[-2]}")

# Slicing also works. If a is a list, the expression a[m:n] returns the
# portion of a from index m to, but not including, index n:
print(f"a[2:5] --> 'baz', 'qux', 'quux' --> {a[2:5]} ")

# Other features of string slicing work analogously for list slicing as well:
# Both positive and negative indices can be specified:
print(f"a[-5:-2] --> 'baz', 'qux', 'quux' --> {a[-5:-2]} ")

# Omitting the first index starts the slice at the beginning of the list, and
# omitting the second index extends the slice to the end of the list:
print(f"a[:4], a[0:4] --> {a[:4], a[0:4]}")
print(f"a[2:], a[2:len(a)] --> {a[2:], a[2:len(a)]}")
print(f"a[:4] + a[4:] --> {a[:4] + a[4:]}")
print(f"a[:4] + a[4:] == a --> True = {a[:4] + a[4:] == a}")


# ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# You can specify a stride (the third parameter stride means steps to jump, for
# example a[0:5:2] --> start on 0 until 5 selecting every 2 elements)—either
# positive or negative, this is if the stride/step is + then from left to right
# if it is negative then from right to left:
print(f"a[0:5:2] --> ['foo', 'baz', 'quux'] = {a[0:5:2]}")
# ['foo', 'baz', 'quux']
print(f"a[1:6:2] --> ['bar', 'qux', 'corge'] = {a[1:6:2]}")
print(f"a[6:0:-2] --> ['corge', 'qux', 'bar'] = {a[6:0:-2]}")

# The syntax for reversing a list works the same way it does for strings:
print(f"a[::-1] --> ['corge', 'quux', 'qux', 'baz', 'bar', 'foo'] = {a[::-1]}")

# Now reversing and striding/steping every 2 elements:
print(f"a[::-2] --> ['corge', 'qux', 'bar'] = {a[::-2]}")

# The [:] syntax works for lists. However, there is an important difference
# between how this operation works with a list and how it works with a string:
s = "foobar"
print(f"s --> 'foobar' = {s} AND s[:] --> 'foobar' = {s[:]}")
# In string s and s[:] make reference to the same object or same address,
# this is:
print(f"s is s[:] --> True = {s is s[:]}")
# or:
print(f"id(s) == id(s[:]) --> True = {id(s) == id(s[:])}")
# or:
print(f"s == s[:] --> True = {s == s[:]}")

# Conversely, if 'a' is a list, a[:] returns a new object that is a copy of
# the content of 'a' but in a different memory address/location. This is why
# in previous chapter we saw that in order to copy one object into another one
# in a way that their content be independent, not impacted when we change one
# of them; then we have to use the [:] notation.
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
b = a[:]
print(f"a is b --> False = {a is b}")
# or:
print(f"a is a[:] --> False = {a is a[:]}")
# or:
print(f" id(a[:]) --> {id(a[:])}")
print(f"id(a) == id(a[:]) --> False = {id(a) == id(a[:]) }")
print(f"id(a) == id(b) --> False = {id(a) == id(b)}")

# Several Python operators ('in' and 'not in') and built-in functions can
# also be used with lists in ways that are analogous to strings:
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"a --> {a}")
# the 'in' operaator:
print(f"'qux' in a --> True = {'qux' in a}")
# the 'not in' operator:
print(f"'thud' not in a --> True = {'thud' not in a}")

# Concatanating (+) two lists:
print(
    f"list concatation: a + ['grault', 'garply'] --> \
{a + ['grault', 'garply']}"
)

# Replication (*) of a list: this create a new list x times:
print(f"a * 3 --> {a * 3}")

# the len(), min() and max() functions:
print(f"len(a) --> 6 = {len(a)}")
print(f"min(a) --> 'bar' = {min(a)}")
print(f"max(a) --> 'qux' = {max(a)}")

# lists and strings have similar behavior because they their parent class is
# the general iterable class.
# the examples above were using a list assigned to a variable; but we can make
# them on a "list literal" as follow:
print(f"list literal: {['foo', 'bar', 'baz', 'qux', 'quux', 'corge']}")
print(
    f"index [2] in literal list --> 'baz' =  \
{['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][2]}"
)
print(
    f"reversed literal list--> \
{['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][::-1]} "
)
print(
    f"quux in literal list? --> True = \
{'quux' in ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']}"
)
print(
    f"len of reversed literal list --> 6 =  \
{len(['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][::-1])} "
)

# now reversing an string:
print("If Comrade Napoleon says it, it must be right."[::-1])

# Lists can be Nested:
# Elements i a list can be any type of object. This include another list. A
# list can contain sublists, which in turn can contain sublists themselves, and
# so on to arbitrary depth.

x = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]
print(f"list x --> {x}")
print(f"(x[0], x[2], x[4]) --> ('a', 'g', 'j') = {x[0], x[2], x[4]} ")
tuple_1 = x[0], x[2], x[4]
print(f"tuple_1 --> {tuple_1}")
list_1 = list(tuple_1)
print(f"list_1 --> {list_1}")
print(f"x[0], x[2], x[4] --> a, g, j = {x[0]}, {x[2]}, {x[4]} ")
# sublists:
print(f"sublists x[1] and x[3] --> {x[1]} and {x[3]}")
# to access elements in a sublist only append an additional index:
print(f"x[1][0] --> 'bb' = {x[1][0]}")
print(f"x[1][1] --> ['ccc', 'ddd'] = {x[1][1]}")
print(f"sublist x[3] --> ['hh', 'ii'] = {x[3]}")
print(f"the second element in x[3] sublist: x[3][1] --> 'ii' = x[3][1]")

# for acessing the elements of another sublist inside of a sublist, we just
# need to add another index x[][][].

# There is no limit, only the computer memory, to the depth or complexity with
# which lists can be nested in this way.

# All the ususal syntax regardding indices and slicing applies to sublists
# as well:
print(
    f"To get the last element in a sublist x[1][1][-1] --> 'ddd' = \
{x[1][1][-1]}"
)
print(
    f"To slice elements 1 and 2 from sublist x[1]: x[1][1:3] \
--> [['ccc', 'ddd'], 'ee'] = {x[1][1:3]}"
)

print(
    f"To slice elements 1 and 2 in REVERSE ORDER from sublist x[1] we have \
to append this [::-1] after the slice x[1][1:3][::-1] --> \
['ee', ['ccc', 'ddd']] = {x[1][1:3][::-1]}"
)
# The above can be obtained as follow:
sublist_1 = x[1][1:3]  # slice the sublist
reversed_sublist_1 = sublist_1[::-1]  # now reverse it.
print(f"reversed_sublist_1 = {reversed_sublist_1}")

print(f"Reversing the x[3] sublist: x[3][::-1] --> ['ii', 'hh'] = {x[3][::-1]}")

# however, be aware that operators and functions apply to only the list at the
# level we specify and are not recursive. Consider what happens when we query
# the length of x using len() built-in function:
print(f"len(x) --> 5 = {len(x)}")
# This does not count the elements in any of the sublists in 'x' list.
# x has only five elements - 3 strings and 2 sublists. the individual elements
# in the sublists don't count toward x's length.
# We will encounter a similar situation when using the 'in' operator:
print(f"'ddd' in x? --> False = {'ddd' in x}")
print(f"'ddd' in x[1]? --> False = {'ddd' in x[1]}")
print(f"'ddd' in x[1][1]? --> True = {'ddd' in x[1][1]}")
# 'ddd' is not one of the elements in x or x[1]. It is only directly an element
# in the sublist x[1][1]. An indivial element in a sublist DOES NOT count as an
# element in the parent list(s).

""" Lists Are Mutable
Most of the data types you have encountered so far have been atomic types.
Integer or float objects, for example, are primitive units that can't be further
broken down. These types are immutable, meaning that they can't be changed once
they have been assigned. It doesn't make much sense to think of changing the
value of an integer. If you want a different integer, you just assign a
different one.

By contrast, the string type is a composite type. Strings are reducible to
smaller parts—the component characters. It might make sense to think of
changing the characters in a string. But you can't. In Python, strings are
also immutable.

The list is the first mutable data type you have encountered. Once a list has
been created, elements can be added, deleted, shifted, and moved around at will.
Python provides a wide range of ways to modify lists.

Modifying a Single List Value
A single value in a list can be replaced by indexing and simple assignment:"""
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"List a: {a}")
a[2] = 10
a[-1] = 20
print(f"List a with 2 and last element mofidifed: {a}")

# In a string object we cannot make item assignment:
s = "foobarbaz"
# s[2] = "x"  # this will trigger a typeError
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# A list item can be deleted with the del command:
del a[3]
print(f"List a with item [3]='qux' deleted: {a}")

# Modifying Multiple List elements/items values:
# What if you want to change the valaue of several contiguous elements in a list
# at one time? Python allows this with slice assignment, which has this syntax:
# a[m:n] = <iterable>.
# Again, for the moment, think of an iterable as a list. This assignment
# replaces the specified slice of the list 'a' with <iterable>
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"List a: {a}")
print(f"Print elements from index 1 to 3 [1:4] --> {a[1:4]}")
print(f"List a: {a}")
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(
    f"modified a with an iterable longer than the slice \
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5 ], insert the additonal 4.4 and 5.5: {a}"
)
print(f"a[1:6] --> {a[1:6]}")

a[1:6] = ["Bark!"]
print(
    f"modified 'a' with an iterable smaller than the slice \
a[1:6] = ['Bark!'], removes the not changed items 2.2, 3.3, 4.4, 5.5 \
--> {a}"
)

# The number of elements changed need to be equal to te number of elements in
# iterable. Python will grow or shrink the list as need depending on if the
# number of elements in the iterable is greater or less than the slice[x:y].
# Based on the above, we can insert multipl elements in place of a single
# element by using a slice that specifies only one element:
a = [1, 2, 3]
print(f"list a: {a}")
a[1:2] = [2.1, 2.2, 2.3]
print(f"using slice[:] to modify 'a' after a[1:2] = [2.1, 2.2, 2.3] --> {a}")

# Note that this is not the same as replacing a single element with a list:
a = [1, 2, 3]
print(f"list a: {a}")
a[1] = [2.1, 2.2, 2.3]
print(f"modifying single element a[1] = [2.1, 2.2, 2.3] --> {a}")

# We can also insert elements into a list without removing anything. Simply
# specify a slice of the form[x:x] (a zero-length slice) at the desired index:
b = [1, 2, 7, 8]
print(f"list b --> {b}")
b[2:2] = [3, 4, 5, 6]
print(f"inserting a zero-length slice: b[2:2] = [3, 4, 5, 6] --> {b}")
# Write a Python statement using slice assignment that will fill in the missing
# values so that a equals [1, 2, 3, 4, 5, 6, 7, 8].
a[2:2] = [3, 4, 5, 6]


# We can delete multiple elements out of the middle of a list by assigning to
# the appropiate slice an empty list. We can also use the 'del' function with
# the same slice:
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"list a: {a}")
a[1:5] = []
print(f"a after deleting using an empty iterable a[1:5] = [] --> {a}")

a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"list a: {a}")
del a[1:5]
print(f"deleting with 'del' funct with the same slice 'del a[1:5]' --> {a} ")

# Prepending and Appending items to a List:
# Additional items can e added to the start or end of a list using the '+'
# concatanation operator or the += augmented operator:
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"list a: {a}")
# augmenting to append (at the end) '+=':
a += ["grault", "garply"]
print(
    f"a after appending (with augmentation +=) list ['grault', 'garply'] \
--> {a} "
)
a.append(["hector", "amparo"])  # appends the list ['hec.', 'amparo'] as a whole
print(f"a after a.append(['hector', 'amparo']) --> {a} ")

del a[-1]
a.append("hector")  # append just one element.
print(f"list a: {a}")

del a[-1]
print(f"list a: {a}")

# preapending with concatenation of a list:
a = [10, 20] + a
print(f"after preapending with concatenation a = [10, 20] + a --> {a} ")

# Note that a list must be concatenated with another list, so if we want to
# add only one element, we need to specify it as a singleton list:
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
a += [20]
print(f"a appended on element a += [20] (singleton) --> {a}")

# without the [] (for list) then generate TypeError:
# a += 99
# Traceback (most recent call last):
#   File "<pyshell#58>", line 1, in <module>
#     a += 99
# TypeError: 'int' object is not iterable

""" Technically, it is not quite correct to say a list must be concatenated
with another list. More precisely, a list must be concatenated with an object
that is iterable. Of course, lists are iterable, so it works to concatenate a
list with another list.

String are iterable also, But watch what happens when you concatenate a string
onto a list:"""
a = ["foo", "bar", "baz", "qux", "quux"]
a += "corge"
print(f"a after concatenate a string object a += 'corge' --> {a}")
# ['foo', 'bar', 'baz', 'qux', 'quux', 'c', 'o', 'r', 'g', 'e']
# If we really want to concatane the single string 'corge' we have to specify
# it with a singleton list:
a = ["foo", "bar", "baz", "qux", "quux"]
a += ["corge"]
print(f"a concatenated with a += ['corge'] --> {a}")

# Methods That Modify a List:
# Python supplies several built-in methods that can be used to MODIFY lists.
# The other strings methods that we saw previous tutorial DO NO MODIFY the
# target string directly. That is because the strings are immutable. Instead,
# the string methods RETURN a new string object that is modified as directed by
# the method. They leave the original target string UNCHANGED.
s = "footbar"
t = s.upper()
print(f"original string: {s} and after t = s.upper(), target string: {t}")

# List methods are different. Because lists are mutable, the list methods shwon
# here modify the target list in place.

# a.append(<object)  This method appends an object to THE END OF a list.
a = ["a", "b"]
a.append(123)
print(f"a, after a.append(123) --> {a}")
# Remember, list methods MODIFY the target ist in place. They do not return a
# new list:
a = ["a", "b"]
x = a.append(123)
print(f"x, after x = a.append(123) --> None = {x} and a modified in place: {a}")

# The .append() method uses an object to add it at the end of the list, and
# if the object is an iterable, it will append the whole object [],(), dict; not
# each element of the iterable object.
a = ["a", "b"]
a.append([1, 2, 3])  # appending an iterable list.
print(f"The whole iterable is appended to a in a.append([1, 2, 3]) --> {a}")
# This is why with .append(), we can append a string as a single entity
a = ["a", "b"]
a.append("foobar")
print(f"a string added as a single entity with a.append('foobar') --> {a}")

# if we want to append the objects in an iterable to an existing list, then we
# need to use the .extend() list method.
# a.extend(<iterable>)   Extends a list with the objects in an iterable.
a = ["a", "b"]
a.extend([1, 2, 3])
print(f"a list extended from an iterable: a.extend([1, 2, 3]) --> {a}")
# In other words, .extend() behaves like the + operator. More precisely, since
# it modifies the list in place, it behaves like the += operator:
a = ["a", "b"]
a += [1, 2, 3]
print(f"a list augmented from an iterable: a += [1, 2, 3] --> {a}")


# Insert an object into a list. at expecific index location:
# a.insert(<index>, <obj>)
# This insert object <obj> into list 'a' at the specified index <index>.
# After execution of the method call, the index <index> indicate contains the
# object <obj> and the remaining list elements are pushed to the right:
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"list a: {a}")
a.insert(3, 3.14159)  # a[3] now has the value 3.14159 and the others moved
# to the right.
print(f"a[3] now has the value 3.14159 = {a[3]}")
print(f"list a: {a}")
# ist a: ['foo', 'bar', 'baz', 3.14159, 'qux', 'quux', 'corge']


# Remove an object from a list:
# a.remove(<obj>) removes object <obj> from list 'a'.
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
a.remove("baz")
print(f"a after removing 'baz' with a.remove('baz') --> {a} ")
print(f"list a: {a}")

# if the object is NOT in list 'a', then an exception is raised:
# a.remove("bark!")
# Traceback (most recent call last):
#   File "C:\PythonBasicsBookExercises\cha09\cha09-Tutorial_on_lists_tuples.py", line 444, in <module>
#     a.remove("bark!")
# ValueError: list.remove(x): x not in list

# Removing object from a list using .pop() method:
# a.pop(index=-1)  # remover an element from a list.
# The .pop() method differs from .remove() in two ways:
# 1- We specify the index of the object to be removed, rather than the object
# itself.
# 2- The .pop() method returns a value: the value of the object that was removed
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"list a: {a}")
a.pop()  # no index, removes the last item in the list.
print(f"removing last element: a.pop() --> 'corge' = {a}")
a.pop()
print(f"removing last element: a.pop() --> 'quux' = {a}")

# If the optional index parameter is specified, the item at the index is
# removed and returned
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"a --> {a}")
print(f"Removing item at index=1: a.pop(1) --> bar = {a.pop(1)}")
# Index can be negative, as with string and list indexing:
print(f"a --> {a}")
print(
    f"Removing item at index=-2 from the right: a.pop(-2) --> \
quux = {a.pop(-2)}"
)
print(f"a --> {a}")

# <index> defaults to -1, so a.pop(-1) is equivalent to a.pop()

# Lists Are Dynamic:
""" This totorial bega with a list of sixs defining characteristics of Python
lists. The last one is that lists are dynamic. We have seen many examples of
this in the sections above. This is, when items are added ot a list, it grows as
needed:"""
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"a --> {a}")
a[2:2] = [1, 2, 3]
a += [3.14159]
print(f"a --> {a}")
# a --> ['foo', 'bar', 1, 2, 3, 'baz', 'qux', 'quux', 'corge', 3.14159]

# Similarly, a list shrinks to accommodate the removal of items:
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(f"a --> {a}")
a[2:3] = []  # delete item at index 2
del a[0]
print(f"a, after deleting a[2:3] and a[0] --> {a}")
# a, after deleting a[2:3] and a[0] --> ['bar', 'qux', 'quux', 'corge']


# Defining a Tuple:
""" Tuples are identical to lists in all respects, except for the following
properties:
1- Tuples are defined by enclosing the elements in parentheses () instead of
square brackets [].
2- Tuples are immutable.
Here is a short example showing a tuple definition, indexing, and slicing:
"""
t = ("foo", "bar", "baz", "qux", "quux", "corge")
print(f"Tuple t --> {t}")
print(f"element at index=0 --> foo = {t[0]}")
print(f"last element in the tuple t[-1] --> corge = {t[-1]}")
print(
    f"a slice starting at index=1 till end striding every 2 elements \
t[1::2] --> ('bar', 'qux', 'corge') = {t[1::2]}"
)
# Never dear! Our favorite string and list reversal mechanism works for tuples
# as well:
print(f"Reverse striding every 1: t[::-1] --> {t[::-1]}")
# --> ('corge', 'quux', 'qux', 'baz', 'bar', 'foo')
print(f"Reverse striding every 2: t[::-2] --> {t[::-2]}")
# --> ('corge', 'qux', 'bar')
print(f"Reverse striding every 3: t[::-3] --> {t[::-3]}")
# ('corge', 'baz')

# Note: Even though tuples are defined using parentheses, we still index and
# slice tuples using square brackets, like in strings and lists.

# Everything we've learned about lists - they can be ordered, they can contain
# arbitrary objects, they can be indexed and sliced, they can be nested - is
# true for tuples as well. But they can NOT be modified, because tupls are
# immutable:
t = ("foo", "bar", "baz", "qux", "quux", "corge")
# t[2] = "Bark!"
# Traceback (most recent call last):
#   File "C:\PythonBasicsBookExercises\cha09\cha09-Tutorial_on_lists_tuples.py", line 529, in <module>
#     t[2] = "Bark!"
# TypeError: 'tuple' object does not support item assignment


# Why to use a tuple instead of a list????
# 1- Program execution is faster when manipulating a tuple than it is for the
#    equivalent list. (This probably not going to be noticeable when the list
#    or tuple is small)
# 2- Sometimes we don't want data to be modified. If the values in the
#    collection are meant to remain constant for the life of the program, then
#    using tuple instead of a list guards against acidental modification.
# 3- There is another Python data type, the dictionary, which requires as one
#    of its components a value that is of an immutable type. A tuple can be
#    used for this purpose, wheraas a list cannot be.

# In a Python REPL session, we can display the values of several objects
# simultaneously by entering them directly at the >>> prompt, separated by
# commas:
# >>> a = "foo"
# >>> b = 42
# >>> a, 3.14159, 42
# displays: ('foo', 3.14159, 42)

# Python displays the respose in parentheses because it is implicitly
# interpreting the input as a tuple.


# There is one peculiarity regarding tuple definition that we should be aware
# of. There is no ambiguity when defining an empty tuple, nor one with two or
# more elements. Python knows that we are defining a tuple:
# >>> t = ()
# >>> type(t)
# <class 'tuple'>

# >>> t = (1, 2)
# >>> type(t)
# <class 'tuple'>

# >>> t = (1, 2, 3, 4, 5)
# >>> type(t)
# <class 'tuple'>

# But what happen when we try to define a tuple with one item:
# >>> t = (2)
# >>> type(t)
# <class 'int'>

# Doh!!! Since parentheses are also used to define operator precedence in
# expressions, Python evaluates the expression (2) as simple the integer 2 and
# creates an integer object. To tell Python that we really want to define a
# singleton tuple, we have to include a trailing comma (,) just before the
# closing parenthesis:
# >>> t = (2,)
# >>> type(t)
# <class 'tuple'>

# >>> t[0]
# 2

# >>> t[-1]
# 2

# We probably won't need to define a singleton tuple often, but there has to
# be a way. When we display a singleton tuple, Python includes the comma, to
# remind us that it's a tuple:
t = (2,)
print(f"The singleton tuple t = (2,) is printed with ',' --> {t}")


# Tuple Assignment, Packing, and Unpacking:
# As we already have seen above, a 'literal' tuple containing several items can
# be assigned to a single object:
t = ("foo", "bar", "baz", "quz")
print(
    f"a literal tuple assigned to an object 't' -->\
t = ('foo', 'bar', 'baz', 'quz')"
)
# When this occurs, it is as if the items in the tuple have been 'packed' into
# the object 't' and we can say that  't' is a 'packed' object:
print(f"t -- > {t}")
print(f"f[0] --> {t[0]}")
print(f"f[-1] --> {t[-1]}")

# if the 'packed' object is subsequently assigned to a new tuple, the individual
# items are 'unpacked' into the objects in the new tuple:
(s1, s2, s3, s4) = t
print("(s1, s2, s3, s4) = t")
print(f"s1 --> {s1}")
print(f"s2 --> {s2}")
print(f"s3 --> {s3}")
print(f"s4 --> {s4}")

# When unpacking a tuple, the number of variables on the left must match the
# number of values/items in the tuple. If they do not match, then below errors:
""" >>> (s1, s2, s3) = t
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    (s1, s2, s3) = t
ValueError: too many values to unpack (expected 3)

>>> (s1, s2, s3, s4, s5) = t
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    (s1, s2, s3, s4, s5) = t
ValueError: not enough values to unpack (expected 5, got 4)"""

# Packing and unpacking can be combined into one statement to make a compound
# assignment (of a literal tuple to a new tuple with packed variables)
(s1, s2, s3, s4) = ("foo", "bar", "baz", "qux")
print("packing and unpacking = (s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')")
print(f"s1 --> {s1}")
print(f"s2 --> {s2}")
print(f"s3 --> {s3}")
print(f"s4 --> {s4}")
# Again, the number of elements in the tuple on the left of the assignment must
# equal the number on the right.
""" >>> (s1, s2, s3, s4, s5) = ('foo', 'bar', 'baz', 'qux')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    (s1, s2, s3, s4, s5) = ('foo', 'bar', 'baz', 'qux')
ValueError: not enough values to unpack (expected 5, got 4)"""

# In assignment like this and a small handful of other situations, Python
# allows the parentheses that are usually used for denoting a tuple to be
# left out:

t = 1, 2, 3
print("t = 1, 2, 3")
print(f"t --> {t}")

x1, x2, x3 = t
print("x1, x2, x3 = t")
print(f"x1, x2, x3 --> (1, 2, 3) = {x1, x2, x3}")

x1, x2, x3 = 4, 5, 6
print("x1, x2, x3 = 4, 5, 6")
print(f"x1, x2, x3 --> (4, 5, 6) = {x1, x2, x3}")

t = (2,)
print("t = 2,")
print(f"t --> (2,) = {t}")
# It works the same whether the parentheses are included or not, so if we have
# any doubt as to wheter they're needed, go ahead and include them.

# Tuple assignment allows for a curious bit of idiomatic Python. Frequently
# when programming, we have two variables whose values we need to swap. In most
# programming languages, it is necessary to store one of the value in a
# temporary variable while the swap occurs like this:
a = "foo"
b = "bar"
print(f"a, b --> ('foo', 'bar') = {a, b}")
# we need to define a temp variable to accomplish the swap:
temp = a
a = b
b = temp
print(f"after the swap: a, b --> ('bar', 'foo') = {a, b}")
# In Python, the swap can be done with a single tuple assignment:
a = "foo"
b = "bar"
print(f"a, b --> ('foo', 'bar') = {a, b}")
# Now applying the Magic of Python tuple assignment:
a, b = b, a  # Python pack the tuple(b, a) and unpack it in tuple (a, b)
print(
    f"after the pack-unpack: a, b = b, a, the tuple (a, b) is \
swapped to ('bar', 'foo') = {a, b}"
)

# As anyone who has ever had to swap values using a temporary variable knows,
# being able to do it this way in Python is the pinnacle of modern
# technological achievement. It will never get better than this.


""" Conclusion
This tutorial covered the basic properties of Python lists and tuples, and how
to manipulate them. You will use these extensively in your Python programming.

One of the chief characteristics of a list is that it is ordered. The order of
the elements in a list is an intrinsic property of that list and does not
change, unless the list itself is modified. (The same is true of tuples,
except of course they can't be modified.)

The next tutorial will introduce you to the Python dictionary: a composite
data type that is unordered. Read on!"""
