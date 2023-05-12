# 1: Create an empty dictionary named captains:
captains = {}

# :
# Using square brackets notation, enter the following data into the dictonary
# one item at at time:
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# 3:
# write two if statements that check if "Enterprise" AND "Discovery" exists as
# keys in the dictionary. Set their values to if the does not exist:
if "Enterprise" in captains:
    next
else:
    captains["Enterprise"] = "unknown"

if "Discovery" in captains:
    next
else:
    captains["Discovery"] = "unknown"

# 4:
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")

for ship in captains:
    print(f"the new ship {ship} is captained by {captains[ship]}")

# 5:
del captains["Discovery"]
print()
print(f"captains after deleting Discovery ship: {captains}")

# 6:
captains_2 = dict({"Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko"})
print()

for ship, captain in captains_2.items():
    print(f"In captains_2 dict: The {ship} is captained by {captain}")
print()

for ship in captains_2:
    print(f"Ship {ship} has a captain called {captains_2[ship]}")

# Challenge: 9.7 :
# Create below capitals dicionary:
import random

capitals_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
}

# Pick a random state name from the dictionary and assign both the state and
# its capital to two variables. You'll need to import random module at the top
# of the program.
states_list = []
for state in capitals_dict:
    states_list.append(state)

random_state = random.choice(states_list)
random_capital = capitals_dict[random_state]


# Then displays the name of the random state to the user and ask them to enter
# the capital for that state. If the user answer incorrectly, then repeatedly
# ask them for the capital until they either enter the correct answer or type
# 'exit'
# If the user answer correctly, then display "Correct" and end the program.
# However, if the user exits without answer correctly, display the correct
# answer and the word "Goodbye.."
while True:
    user_response = input(f"What is the capital for state {random_state}? ")
    if user_response.upper() == "EXIT":
        print(f"The capital of {random_state} is {random_capital}. Goodbye...")
        break
    elif user_response.upper() == random_capital.upper():
        print(
            f"You are correct, {user_response} is the capital of \
{random_state}!!!!!!"
        )
        break
    else:
        continue

# Challenge 9.9 Cats with Hats:
"""We have one hundred cats. One day, we decide to arrange all the cats in a
giant circle. Initially, none of the cats has a hat on. We walk the circle a
hundred times, always starting with the first cat (cat #1). Each time we stop
at a cat, we check if it has a hat on. If it doesn't, then we put a hat on it
if it does, then we take the hat off.
1- The first round, we stop at every cat, placing a hat on each one.
2- The second round, we stop only at every second cat (#2, 4, 6, 8 and so on).
3- The third round, we stop only a every third cat (#3, 6, 9, 12 and so on).
4- We continue this process until we've made one hundred rounds around the
   cats. On the last round, we stop only at cat #100.

Write a program that simply outputs which cats have hats at the end. """
cats = []
number_of_rounds = 100
for i in range(0, number_of_rounds, 1):
    if i == 0:
        for x in range(number_of_rounds):
            cats.append(True)
    else:
        for j in range(i, number_of_rounds, i + 1):
            # print(f"i,j = {i, j}")
            if cats[j] is True:
                cats[j] = False
            else:
                cats[j] = True
    # print(f"round #{i +1} cats list: {cats}")

for i in range(len(cats)):
    if cats[i]:
        print(f"cat #{i + 1} is wearing a beautiful hat!!")

# Now the solution from github:
# This solution use a dictionary:
the_cats = {}

""" By default, no cats have been visited so we set every cat's number
to false:"""
for i in range(1, 101):
    the_cats[i] = False

# walk aroung the circle 100 times:
for i in range(1, 101):
    # visit all cats each time we do a lap
    for cat, hat in the_cats.items():
        # Determine whether or not to visit a cat
        if cat % i == 0:
            # Add or remove the hat:
            if the_cats[cat]:
                the_cats[cat] = False
            else:
                the_cats[cat] = True

# Print whether each cat has a hat
for cat, hat in the_cats.items():
    if the_cats[cat]:
        print(f"*** Cat {cat} has a hat.")
    # else:
    #    print(f"*** Cat {cat} is hatless!!!")
