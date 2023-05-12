""" Python provides several functionss for generating random numbers in the random
module. A module is a collection of related code. Python's Standard Library is
an organized collection of modules that you can import into your own code to
solve various problems. """
# to import the random module:
import random

# randint() function in the random module has two required parameters called a
# and b, both of which must be integers. The function returns a random interger
# that is greater than or equal to a of less than or equal to b. Example:
value_int = random.randint(1, 10)  # returns an integer between 1 and 10

# Since randint() is located in the random module, we must type random followed
# by a dot(.) and then the function name in order to use it.

value_0_or_1 = random.randint(0, 1)  # return 0 ro 1.

# Each integer between a and b is equally likely to be returned by randint(). So
# randint(1, 10), each integer between 1 and 10 has a 10 percent chance of being
# returned. For randint(0, 1), there is a 50 percent chance that 1 will be retuned

# Fair Coins: following code is to simulate the flipping a fair coin. By fair
# Coin we mean a coin that, when flipped, has equal chance of landing heads or
# tails. With randint() all possible value from the range have equal probability
# to be returned.

def coin_flip():
    """ Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


# First initialize the tallies to 0
heads_tally = 0
tails_tally = 0
repetitions = int(input("Enter number of repetitions: "))

for trial in range(repetitions):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally += 1
print(f"with randint(): heads_tally = {heads_tally}, tails_tally = {tails_tally}")
print(f"with randint(): The ratio of heads to tails is {heads_tally / tails_tally}")

# Unfair Coins: can be accomplished using the random() fucntion.
# the random() function takes no arguments and returns a floating-point number
# greater than or equal to 0.0 but less than 1.0. And each possible return value
# is equally likely, In probability theory, this is known as a "Uniform
# probability distribution". One consequence of this is that, given a number 'n'
# between 0 and 1, the probability that the function random() returns a number
# less than 'n' is just 'n' itself. For example, the probability that random()
# returns a value less than 0.8 is 0.8, and the probability that random()
# returns a value less than 0.25 is 0.25
# Using this fact, we can write a function that simulates a coin flip but returns
# tails with a specified probability:
def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"

# Now calling unfair_coin_flip(0.7) has a 70 percent chance of returning "tails"
heads_tally = 0
tails_tally = 0

for trial in range(repetitions):
    if unfair_coin_flip(0.7) == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

print(f"with random(): tails_tally = {tails_tally}, heads_tally = {heads_tally}")
print(f"with random(): The ratio of tails to heads is --> {tails_tally / heads_tally}")
print(f"with random(): The percentage of tails is 70% --> {tails_tally / repetitions}")

# Write a function called roll() that uses randint() to simulate a fair die by
# returning  a random integer between 1 and 6
def roll():
    return random.randint(1, 6)

# Write a program that simulate ten thousand rolls of a fair die and displays
# the average numer rolled:
from statistics import mean  # import the mean function from statistics module

die_results_list = []
for trial in range(repetitions):
    die_results_list.append(roll())

rolled_average = mean(die_results_list)
print(f"Average rolled dies --> {round(rolled_average,0)}")

    

