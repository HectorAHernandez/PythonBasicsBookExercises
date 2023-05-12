""" Python provides another composite data type called a dictionary, which is
similar to a list in that it is a collection of objects.

Here's what you'll learn in this tutorial: You'll cover the basic
characteristics of Python dictionaries and learn how to access and manage
dictionary data. Once you have finished this tutorial, you should have a good
sense of when a dictionary is the appropriate data type to use, and how to do
so.

Dictionaries and lists share the following characteristics:

Both are mutable.
Both are dynamic. They can grow and shrink as needed.
Both can be nested. A list can contain another list. A dictionary can contain
   another dictionary. A dictionary can also contain a list, and vice versa.
Dictionaries differ from lists primarily in how elements are accessed:
List elements are accessed by their position in the list, via indexing.
Dictionary elements are accessed via keys.


Defining a Dictionary
Dictionaries are Python's implementation of a data structure that is more
generally known as an associative array. A dictionary consists of a collection
of key-value pairs. Each key-value pair maps the key to its associated value.

You can define a dictionary by enclosing a comma-separated list of key-value
pairs in curly braces ({}). A colon (:) separates each key from its associated
value:

d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
The following defines a dictionary that maps a location to the name of its
corresponding Major League Baseball team:
"""

MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

""" You can also construct a dictionary with the built-in dict() function. The
argument to dict() should be a sequence of key-value pairs. A list[] of
tuples() works well for this:

d = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])
MLB_team can then also be defined this way:"""

MLB_team = dict(
    [  # Using a list '[]'
        ("Colorado", "Rockies"),
        ("Boston", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Milwaukee", "Brewers"),
        ("Seattle", "Mariners"),
    ]
)
# OR
MLB_team = dict(
    (  # Using a tuple '()'
        ("Colorado", "Rockies"),
        ("Boston", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Milwaukee", "Brewers"),
        ("Seattle", "Mariners"),
    )
)

# If the key-values are simple strings, they can be specified as keyword
# arguments. So here is yet another way to define MLB_team:
MLB_team = dict(
    Colorado="Rockies",
    Boston="Red Sox",
    Minnesota="Twins",
    Milwaukee="Brewers",
    Seattle="Mariners",
)

# Once you've defined a dictionary, you can display its contents, the same as
# you can do for a list. All three of the definitions shown above appear as
# follows when displayed:
# >>> type(MLB_team)
# <class 'dict'>

print(f"MLB_team --> {MLB_team}")

# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
# 'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}

# The entries in the dictionary display in the order they were defined. But that
# is irrelevant when it comes to retrieving them. Because dictionary elements
# are not accessed by numerical index or order.
# >>> MLB_team[1]
# Traceback (most recent call last):
#  File "<pyshell#13>", line 1, in <module>
#    MLB_team[1]
# KeyError: 1

""" Accessing Dictionary Values
Of course, dictionary elements must be accessible somehow. If you don't get
them by index, then how do you get them?

A value is retrieved from a dictionary by specifying its corresponding key in
square brackets ([]):"""
print(f"MLB_team['Minnesota'] --> Twins = {MLB_team['Minnesota']} ")
print(MLB_team["Colorado"])

# If you refer to a key that is not in the dictionary, Python raises an
# exception:
# >>> MLB_team['Toronto']
# Traceback (most recent call last):
#   File "<pyshell#19>", line 1, in <module>
#     MLB_team['Toronto']
# KeyError: 'Toronto'

# Adding an entry to an existing dictionary is simply a matter of assigning a
# new key and value:
MLB_team["Kansas City"] = "Royals"
print(f"After adding 'Kansas City' MLB_team --> {MLB_team}")

# if you want to update an entry, you can just assign a new value to the
# existing key:
MLB_team["Seattle"] = "Seahawks"
print(f"After updating 'Seattle' MLB_team --> {MLB_team}")

# To delete an entry, use the 'del' statement, specifying the key to delete:
del MLB_team["Seattle"]
print(f"After DELETING 'Seattle' MLB_team --> {MLB_team}")

""" Dictionary Keys vs. List Indices
You may have noticed that the interpreter raises the same exception, KeyError,
when a dictionary is accessed with either an undefined key or by a numeric
index:

>>> MLB_team['Toronto']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    MLB_team['Toronto']
KeyError: 'Toronto'

>>> MLB_team[1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    MLB_team[1]
KeyError: 1
In fact, it's the same error. In the latter case, [1] looks like a numerical
index, but it isn't.

You will see later in this tutorial that an object of any immutable type can
be used as a dictionary key. Accordingly, there is no reason you can't use
integers: """
d = {0: "a", 1: "b", 2: "c", 3: "d"}
print(f"d --> {d}")
print(f"d[0] --> a = {d[0]}")
print(f"d[2] --> c = {d[2]}")

# In the expressions MLB_team[1], d[0], and d[2], the numbers in square
# brackets appear as though they might be indices. But they have nothing to do
# with the order of the items in the dictionary. Python is interpreting them
# as dictionary keys. If you define this same dictionary in reverse order, you
# still get the same values using the same keys:
d = {3: "d", 2: "c", 1: "b", 0: "a"}
print(f"inversed defined d --> {d}")
print(f"Same value for same key: d[0] --> a = {d[0]}")
print(f"Same value for same key: d[2] --> c = {d[2]}")

# The syntax may look similar, but you can't treat a dictionary like a list:
# >>> type(d)
# <class 'dict'>

# >>> d[-1]
# Traceback (most recent call last):
#  File "<pyshell#30>", line 1, in <module>
#    d[-1]
# KeyError: -1

# >>> d[0:2]
# Traceback (most recent call last):
#   File "<pyshell#31>", line 1, in <module>
#    d[0:2]
# TypeError: unhashable type: 'slice'

# >>> d.append('e')
# Traceback (most recent call last):
#  File "<pyshell#32>", line 1, in <module>
#    d.append('e')
# AttributeError: 'dict' object has no attribute 'append'

""" Note: Although access to items in a dictionary does not depend on order,
Python does guarantee that the order of items in a dictionary is preserved.
When displayed, items will appear in the order they were defined, and iteration
through the keys will occur in that order as well. Items added to a dictionary
are added at the end. If items are deleted, the order of the remaining items
is retained.

You can only count on this preservation of order very recently. It was added
as a part of the Python language specification in version 3.7. However, it was
true as of version 3.6 as well—by happenstance as a result of the
implementation but not guaranteed by the language specification."""

# Building a Dictionary Incrementally
# Defining a dictionary using curly braces and a list of key-value pairs, as
# shown above, is fine if you know all the keys and values in advance. But
# what if you want to build a dictionary on the fly?
# You can start by creating an empty dictionary, which is specified by empty
# curly braces. Then you can add new keys and values one at a time:

person = {}
# >>> type(person)
# <class 'dict'>
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}
# Once the dictionary is created in this way, its values are accessed the same
# way as any other dictionary:
print(f"person dict --> {person}")
print(f"person['fname'] --> Joe = {person['fname']}")
print(f"person['age'] --> 51 = {person['age']}")
print(f"person['children'] --> ['Ralph', 'Betty', 'Joey'] = {person['children']}")

# Retrieving the values in the sublist or subdirectory requires an additional
# index or key:
print(f"person['children'][-1] --> Joey = {person['children'][-1]}")
print(f"person['pets']['cat'] --> Sox = {person['pets']['cat']}")

# This example exhibits another feature of dictionaries: the values contained
# in the dictionary don't need to be the same type. In person, some of the
# values are strings, one is an integer, one is a list, and one is another
# dictionary.
# Just as the values in a dictionary don't need to be of the same type, the
# keys don't either:
foo = {42: "aaa", 2.78: "bbb", True: "ccc"}
print(f"dict foo --> {foo}")
print(f"foo[42] --> 'aaa' = {foo[42]}")
print(f"foo[2.78] --> 'bbb' = {foo[2.78]}")
print(f"foo[True] --> 'ccc' = {foo[True]}")

""" Here, one of the keys is an integer, one is a float, and one is a Boolean.
It's not obvious how this would be useful, but you never know.

Notice how versatile Python dictionaries are. In MLB_team, the same piece of
information (the baseball team name) is kept for each of several different
geographical locations. person, on the other hand, stores varying types of
data for a single person.

You can use dictionaries for a wide range of purposes because there are so
few limitations on the keys and values that are allowed. But there are
some. Read on!"""

# Restrictions on Dictionary Keys:
# Almost any type of value can be used as a dictionary key in Python. We saw
# this example, where integer, float, adn Boolean objects are used as key:
foo = {42: "aaa", 2.78: "bbb", True: "ccc"}
print(f"foo --> {foo}")
# We can even use built-in objects like types and functions:
d = {int: 17, float: 2.2, bool: 3}
print(f"dictionary d, using object types as key --> {d}")
# dictionary d, using object types as key --> {<class 'int'>: 17,
# <class 'float'>: 2.2, <class 'bool'>: 3}
print(
    f"key with object type 'float' d[float] has the value --> \
2.2 = {d[float]}"
)
print(f"key with object type 'int' d[int] has the value --> 17 = {d[int]}")
print(f"key with object type 'bool' d[bool] has the value --> 3 = {d[bool]}")

# now using built-in functions as key: binary(bin), hexadecimal(hex) and octal:
num_dict = {bin: 12, hex: 17, oct: 3}
print(f"num_dict, using built-in functions as key --> {num_dict}")
# num_dict, using built-in functions as key --> {<built-in function bin>: 12,
# <built-in function hex>: 17, <built-in function oct>: 3}
print(f"key with built-in function bin: num_dict[bin] --> 12 = {num_dict[bin]}")
# key with built-in function bin: num_dict[bin] --> 12 = 12
q_value = num_dict[hex]
print(f"q_value --> 17 = {q_value}")
print(f"key with built-in function oct: num_dict[oct] --> 3 = {num_dict[oct]}")

# However, there are a copple of restrictions that dictionary keys must
# abide by:
# First, a given key can appear in a dictionary only once. Duplicate keys are
# not allowed. A dictionary maps each key to a corresponding value, so it
# doesn't make sense to map a particualr key more than onnce.
# We saw above that when we assign a value to an already existing dictionary
# key, it does not add the key a second time, but replace the existing value:
MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}
print(f"MLB_team --> {MLB_team}")
MLB_team["Minnesota"] = "Timberwolves"
print(
    f"After intending to add, again, key 'Minnesota' the previous value is \
updated or replaced: MLB_team --> {MLB_team}"
)
# Similarly, if we specify a key a second time during the initial creation of
# the dictionary, the second occurrence will override the first:
MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Timberwolves",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
    "Minnesota": "Twins",
}
print(f"Timberwolves is not included MLB_Team --> {MLB_team}")


# Secondly, a dictionary key must be of a type that is immutable. You have
# already seen examples where several of the immutable types you are familiar
# with—integer, float, string, and Boolean—have served as dictionary keys.

# A tuple can also be a dictionary key, because tuples are immutable:
d = {(1, 1): "aa", (1, 2): "bb", (2, 1): "cc", (2, 2): "dd"}
print(f"using tuple as dictionary keys: d --> {d}")
print(f"using tuple (1, 1) as a key: d[(1, 1)] --> aa = {d[(1, 1)]}")
print(f"using tuple (2, 1) as a key: d[(2, 1)] --> cc = {d[(2,1)]}")

# (Recall from the discussion on tuples that one rationale for using a tuple
# instead of a list is that there are circumstances where an immutable type
# is required. This is one of them.)

# However, neither a list nor another dictionary can serve as a dictionary
# key, because lists and dictionaries are mutable:
# d = {[1, 1]: 'a',
#      [1, 2]: 'b',
#      [2, 1]: 'c',
#      [2, 2]: 'd'
#      }
# Traceback (most recent call last):
#  File "C:\PythonBasicsBookExercises\cha09\cha09-Tutorial_on_Dictionares.py",
# line 346, in <module>
#    d = {[1, 1]: 'a',
# TypeError: unhashable type: 'list'

""" Technical Note: Why does the error message say “unhashable”?
Technically, it is not quite correct to say an object must be immutable to be
used as a dictionary key. More precisely, an object must be hashable, which
means it can be passed to a hash function. A hash function takes data of
arbitrary size and maps it to a relatively simpler fixed-size value called a
hash value (or simply hash), which is used for table lookup and comparison.

Python's built-in hash() function returns the hash value for an object which
is hashable, and raises an exception for an object which isn't:
>>> hash('foo')
11132615637596761

>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
All of the built-in immutable types you have learned about so far are hashable,
and the mutable container types (lists and dictionaries) are not. So for
present purposes, you can think of hashable and immutable as more or less
synonymous.
In future tutorials, you will encounter mutable objects which are also hashable.
"""

# Restrictions on dictionary Values:
# By contrast, there are no restrictions on dictionary values. Literally non at
# all. A dictionary value can be any type of object Python can supports,
# including mutable types like lists and dictionaries, and user-defined
# objects, which we will learn about in upcoming tutorials.

# There is also no restriction again a particular value appearing in a
# dictionary multiple times:
d = {0: "a", 1: "a", 2: "a", 3: "a"}
print(f"dict with same value multiple times: {d}")
print(f"d[0] == d[1] == d[2]??? --> True = {d[0] == d[1] == d[2]}")

# Operators and Built-in functions:
# We have already become familiar with many of the operators and built-in
# functions that can be used in strings, lists, and tuples. Some of these work
# with dictionaries as well.
# For example, the 'in' and 'not in' operators return True or False according
# to whether the specified operand occurs as a key in the dictionary:
MLB_team = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}
print(f"is 'Milwaukee' in MLB_team?? --> True = {'Milwaukee' in MLB_team}")
print(f"is 'Toronto' in MLB_team?? --> False = {'Toronto' in MLB_team}")
print(f"is 'Toronto' not in MLB_team?? --> True = {'Toronto' not in MLB_team}")

# We can use the in operator together with short-circuit evaluation to avoid
# raising an error when trying to access a key that is not in the dictionary:
# print(f"MLB_team['Toronto'] -->{MLB_team['Toronto']}")
# Traceback (most recent call last):
#  File "C:\PythonBasicsBookExercises\cha09\cha09-Tutorial_on_Dictionares.py", line 416, in <module>
#    print(f"MLB_team['Toronto'] -->{MLB_team['Toronto']}")
# KeyError: 'Toronto'
print(
    f"'Toronto' in MLB_team and MLB_team['Toronto'] --> False = \
{'Toronto' in MLB_team and MLB_team['Toronto']}"
)  # displays False, not keyError
print(
    f"'Seattle' in MLB_team and MLB_team['Seattle'] --> Mariners = \
{'Seattle' in MLB_team and MLB_team['Seattle']}"
)  # displys Mariners

# In the second case, due to short-circuit evaluation, the expression
# MLB_team['Toronto'] is not evaluated, so the keyError exception does not
# occurs


# The len() function returns the number of key-value pairs in a dictionary:
print(f"len(MLB_tema) --> 5 = {len(MLB_team)}")


# Built-in Dictionary Methods:
""" As with strings and lists, there are several built-in methods that can be
invoked on dictionaries. In fact, in some cases, the list and dictionary
methods share the same name. (In the discussion on object-oriented
programming, you will see that it is perfectly acceptable for different types
to have methods with the same name.)

The following is an overview of methods that apply to dictionaries:"""

# d.clear(): Clears a dictionary. this is empty the dict of all key-value pairs
d = {"a": 10, "b": 20, "c": 30}
print(f"dict d --> {d}")
d.clear()
print(f"dict d after d.clear() --> {d}")


# get(<key> [, <default>]): returns the value for a key if it exist in the dict.
# The Python dictionary .get() method provides a convenient way of getting the
# value from a dictionary without checking ahead of time whether the key
# exists, and without raising an error.
# d.get(<key>) searches dictionary 'd' for <key> and returns the associated
# value if it is found. If <key> is NOT found, it returns the value 'None':
d = {"a": 10, "b": 20, "c": 30}
print(f"dict d --> {d}")
print(f"d.get('b') --> 20 = {d.get('b')}")
print(f"d.get('z') -- None = {d.get('z')}")


# d.items(): Returns a list of tuples of key-value pairs in a dictionary.
# d.items() returns a list of tuples containing the key-value pairs in the
# dictionary. The first item in each tuple is the key, and the second item
# is the key's value:
print(f"dict d --> {d}")
print(f"d.items() --> {d.items()}")
# d.items() --> dict_items([('a', 10), ('b', 20), ('c', 30)])
print(f"list(d.items()) --> {list(d.items())}")  # print only the list, not
# or excluding the 'dict_items() in front of the list', see below:
# list(d.items()) --> [('a', 10), ('b', 20), ('c', 30)]
# the above indicate that when using the dictionary .items() built-in method,
# we have to use the list() function to access the key-value pairs using
# the index:
second_pair_value = list(d.items())[1][1]
print(f"second_pair_value --> 20 = {second_pair_value}")
third_pair_key = list(d.items())[2][0]
print(f"third_pair_key --> c = {third_pair_key}")

# if we don't use the list() function, then TypeError is generated:
# second_pair_value = d.items()[1][1]
# Traceback (most recent call last):
#  File "<pyshell#22>", line 1, in <module>
#    d.items()[1][1]
# TypeError: 'dict_items' object is not subscriptable


# d.keys(): Returns a list of keys in a dictionary. A list of all the keys:
print(f"d.keys() --> {d.keys()}")
# d.keys() --> dict_keys(['a', 'b', 'c'])
print(f"list(d.keys()) --> {list(d.keys())}")  # print only the list, not
# or excluding the 'dict_keys() in front of the list', see below:
# list(d.keys()) --> ['a', 'b', 'c']
# the above indicate that when using the dictionary .keys() built-in method,
# we have to use the list() function to access the keys in the key-value pairs
# using the index:
second_key = list(d.keys())[1]
print(f"second_key --> b = {second_key}")
third_key = list(d.keys())[2]
print(f"third_key --> c = {third_key}")

# if we don't use the list() function, then TypeError is generated:
# second_key = d.key()[1]
# Traceback (most recent call last):
#  File "<pyshell#25>", line 1, in <module>
#    d.keys()[1]
# TypeError: 'dict_keys' object is not subscriptable


# d.values(): Returns a list of values in a dictionary
print(f"d.values() --> {d.values()}")
# d.values() --> dict_values([10, 20, 30])
print(f"list(d.values()) --> {list(d.values())}")  # print only the list, not
# or excluding the 'dict_values() in front of the list', see below:
# list(d.value()) --> [10, 20, 30]
# the above indicate that when using the dictionary .values() built-in method,
# we have to use the list() function to access the values in the key-value pairs
# using the index:
second_value = list(d.values())[1]
print(f"second_value --> b = {second_value}")
third_value = list(d.values())[2]
print(f"third_value --> c = {third_value}")

# if we don't use the list() function, then TypeError is generated:
# second_value = d.values()[1]
# Traceback (most recent call last):
#  File "C:\PythonBasicsBookExercises\cha09\cha09-Tutorial_on_Dictionares.py", line 543, in <module>
#    second_value = d.values()[1]
# TypeError: 'dict_values' object is not subscriptable

# Any duplicate values in the list will be returned as many times as they occur:
d = {"a": 10, "b": 10, "c": 10}
print(f"dictionary d = {d}")
print(f"duplicate values in d = {list(d.values())} ")

# Technical Note: The .items(), .keys(), and .values() methods actually return
# something called a view object (like dict_items, dict_keys and dict_values).
# That is why we have to use the list() method to convert the view object into
# a real list. A dictionary view object is more or less like
# a window on the keys and values. For practical purposes, you can think of
# these methods as returning lists of the dictionary's keys and values.

# d.pop(<key> [, default]): Remove a key from a dictionary, if it is present,
# and returns its value.
# if <key> is present in d, d.pop(<key>) removes <key> and returns its
# associated value:
d = {"a": 10, "b": 20, "c": 30}
print(f"dict d --> {d}")
print(f"Delete key='b' using d.pop('b') and returns the value 20 = {d.pop('b')}")
print(f"After deleting key='b': dict d --> {d}")

# if <key> is not in d, and the optinal <default> argument is specified, then
# that value is returned, and no exception is raised:
print(f"when key not found no delete and returns default -1 = {d.pop('z', -1)}")
print(f"After trying deleting key='z': dict d --> {d}")

# d.popitem(): Removes a key-value pair from a dictionary.
# d.popitem() removes the last key-value pair added from the dictionary and
# returns it as a tuple:
d = {"a": 10, "b": 20, "c": 30}
print(f"dict d --> {d}")
del_item = d.popitem()  # deleting last item
print(f"Ater deleting last item {del_item} with d.popitem() {d}")
# Ater deleting last item ('c', 30) with d.popitem() {'a': 10, 'b': 20}
del_item = d.popitem()
print(f"Ater deleting last item {del_item} with d.popitem() {d}")
# Ater deleting last item ('b', 20) with d.popitem() {'a': 10}
del_item = d.popitem()
print(f"Ater deleting last item {del_item} with d.popitem() {d}")
# Ater deleting last item ('a', 10) with d.popitem() {}
# now the dictionary is empty and below attempt to delete will generate the
# keyError exception below:
# del_item = d.popitem()
# Traceback (most recent call last):
#   File "C:\PythonBasicsBookExercises\cha09\cha09-Tutorial_on_Dictionares.py", line 598, in <module>
#     del_item = d.popitem()
# KeyError: 'popitem(): dictionary is empty'

# Note: in Python versions less than 3.6, popitem() would return an arbitrary
# (random) key-value pair because Python dictionaries were unordered before
# version 3.6.

# d.update(<obj>):
# the d.update(<obj>) merge a dictionary 'd' with another dictionary or with
# an iterable of key-value pairs.
# if <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into
# 'd' dictionary. And for each key in <obj>:
#  - If key is not present in 'd', the key-value pair from <obj> is added to 'd'
#  - If the key is already present in 'd', the corresponding value in 'd' for
#    that key is updated with the value from <obj>.
# Here an example:
d1 = {"a": 10, "b": 20, "c": 30}

d2 = {"b": 222, "d": 444}
# first way to update/merge:
print(f"d1 --> {d1}")
print(f"d2 --> {d2}")
d1.update(d2)
print(f"d1 after merge with: d1.update(d2) --> {d1}")
# d1 after merge: d1.update(d2) --> {'a': 10, 'b': 222, 'c': 30, 'd': 444}

# second way to update/merge, using a list of tuples of pair:
d1 = {"a": 10, "b": 20, "c": 30}
d1.update([("b", 200), ("d", 400)])
print(f"d1 after merge with: d1.update([('b', 200), ('d', 400)]) --> {d1}")

# Third way to update/merge, with the values to merge specified as a list of
# keyword arguments:
d1 = {"a": 10, "b": 20, "c": 30}
d1.update(b=2020, d=4040)
print(f"d1 after merge with: d1.update(b=2020, d=4040) --> {d1}")

""" Conclusion
In this tutorial, you covered the basic properties of the Python dictionary and
learned how to access and manipulate dictionary data.

Lists and dictionaries are two of the most frequently used Python types. As you
have seen, they have several similarities, but differ in how their elements are
accessed. Lists elements are accessed by numerical index based on order, and
dictionary elements are accessed by key

Because of this difference, lists and dictionaries tend to be appropriate for
different circumstances. You should now have a good feel for which, if either,
would be best for a given situation.

Next you will learn about Python sets. The set is another composite data type,
but it is quite different from either a list or dictionary."""
