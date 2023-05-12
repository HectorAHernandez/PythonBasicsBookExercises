# Creating a Dicionary from scratch
capitals = {"California": "Sacramento", "New York": "Albany", "Texas": "Austin"}
print(capitals)
# {'New York': 'Albany', 'California': 'Sacramento', 'Texas': 'Austin'}
# creating a dictionary from a sequence of tuple using the built-in dict():
key_value_pairs = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin"),
)

capitals = dict(key_value_pairs)
print(capitals)

# we can create an empty dictionary by using {} or dict():
empty_dict_01 = {}
print(f"type(empty_dict_01) --> {type(empty_dict_01)}")

empty_dict_02 = dict()
print(f"type(empty_dict_02) --> {type(empty_dict_02)}")

# Accessing dictionary values:
# we have to enclose the corresponding key in square brackets [] at the end of
# a dictionary or a variable name assigned to a dictionary:
capital_in_south = capitals["Texas"]
print(f"capital_in_south: {capital_in_south}")

# ADDING values in a dictionary:
capitals["Colorado"] = "Denver"
# First, we use square brackets notation with "Colorado" as the key, as if we
# were looking up the value. Then we use the assignment operator (=) to assign
# the value "Denver" to the new key.
print(f"dict capital with Colorado-Denver: {capitals}")

# Each key in a dictionary can be assigned ONLY a single value. If a key is
# given a new value, then Python overwrites the old one:
capitals["Texas"] = "Houston"
print(f"dict capital change Texas-Houston: {capitals}")


# DELETING or REMOVING an item from a dictionary, use the 'del' keyword with
# the key for the value we want to delete:
del capitals["Texas"]
print(f"dict capital DELETED Texas-Houston: {capitals}")


# Cheking the existance of dictionary keys:
""" if we try to access a value in a dictionary using a key that does not
exist, then Python raises a 'keyError'
capt_1 = capitals["Arizona"]
will generate keyError:
Traceback (..)..
  File...., line xx..
    capt_1 = capitals["Arizona"]
KeyError: 'Arizona' """
# the keyError is the most common error encountered when working with
# dictionaries. Whenever you see it, it means that the program attempted to
# access a value using a key that does NOT exist.
# We can check that a key exists in a dictionary by using the 'in' keyword:
print(f"Does Arizona is in capitals dict? --> False = {'Arizona' in capitals}")
print(f"California is in capitals? --> True = {'California' in capitals}")

# With 'in' we can first check that a key exists before doing something with \

# the value for that key:
if "Colorado" in capitals:
    # Print only if Arizona key exist. or any other process needed:
    print(f"The capital of 'Colorado' is {capitals['Colorado']}")

# It is very important to remember that 'in' checks for the existance of keys,
# not the existance of values:
print(f"'Sacramento' is in captials? --> False = {'Sacramento' in capitals} ")

# Even though "Sacramento" is a value for the existing "California" key in
# capitals, cheking for its existance return False.
print()
print()


# Iterating Over Dictionaries:
""" Like lists and tuples, dictionaries are iterable. But looping over a
dictionary is a bit different than looping over a list or a tuple. When we loop
over a dictionary with a for...loop, we iterate over the dictionary's keys:"""
for dict_key in capitals:
    print(f"the key is: {dict_key}")

# So, if we want to loop over the capitals dictionary and print
# "The capital of X is Y", where where X is the key/name of the state and
# Y is the value/state's capital, then we can do the following:
for state in capitals:
    print(f"The capital of {state} is {capitals[state]}")

# However, there's a slightly more succinct way to do this using the .items()
# dictionary's method, which returns a list-like object containing tuples of
# key-value pairs. For example, capitals.items() returns a list of tuples of
# states and their corresponding capitals:
print(f"capitals.items() --> {capitals.items()}")

# The object returned by .items() is NOT really a list. It has a special type
# called a dict_items:
print(
    f"type(capitals.items()) = <class 'dict_items'> --> \
{type(capitals.items())}"
)

# Don't worry about what dict_items really is. We usually won't work with it
# directly. The important thing to know is that we can use .items() dictionary's
# method to loop over a dictionary's keys and values simultaneously.
# Let's rewrite the previous loop using .items() dict's method:
for state, capital in capitals.items():
    print(f"The capital of {state} is {capital}")

# When we loop over capitals.items(), each iteration of the loop produces a
# tuple containing the state name and the corresponding capital city name. By
# assigning this tuple to 'state', 'capital', we ensure that the components are
# unpacked into the two variables 'state' and 'capital'

# Dictionary keys and Immutability:
# there is only one restiction on what constitutes a valid dictionary key.
# Only immutable types are allowed. This means, for example, that a list can't
# be a dictionary key, because it can change/mutable.
# below is a valid key for capitals:
capitals[50] = "Honolulu"  # an integer type.
capitals[51.10] = "San Juan"  # a float type.
print(f"New members in capitals: {capitals}")

# For reference, here's a list of all the data type we've learned about so far
# that are valid dictionary keys:
# integers, floats, strings, Booleans, tuples

# Unlike keys, dictionary values can be any valid Python type, including others
# dictionaries!!

# Nested Dictionaries:
""" Just as we can nest lists inside other lists and tuples inside other
tuples, we can create nested dictionaries. Let's alter the capitals dictionary
to illustrate this idea:"""
states = {
    "California": {"capital": "Sacramento", "flower": "California Popy"},
    "New York": {"capital": "Albany", "flower": "Rose"},
    "Texas": {"capital": "Austin", "flower": "Bluebonnet"},
}
# Instead of mapping state names to their capital cities, we created a 'states'
# dictionary that maps each state name to a dictionary containing the capital
# city and the state flower. The value of each key is a dictionary
states["Texas"]
print(f"The value of key states['Texas'] is a dictionary: {states['Texas']}")

# To get the Texas state flower, first get the value at the key "Texas", and
# then the value at the key "flower"
states["Texas"]["flower"]
print(
    f"The flower of 'Texas' is states['Texas']['flower'] --> Bluebonnet =  \
{states['Texas']['flower']}"
)

""" Nested dictionaries come up more often than you might expect. They're
particularly useful when working with data transmitted over the Web. Nested
dictionaries are also great for modeling structured data, such as spreadsheets
or ralational databases
"""
