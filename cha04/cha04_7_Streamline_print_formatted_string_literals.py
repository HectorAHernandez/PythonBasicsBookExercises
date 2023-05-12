heads = 2
arms = 3
name = "Zaphod"

# before way:
print(name + " has " + str(heads) + " heads and " + str(arms) + " arms")

# using earlier version of Python 3.6:
print("{} has {} heads and {} arms".format(name, heads, arms) )

# new way using Python 3.6 and above versions:
print(f"{name} has {heads} heads and {arms} arms")

# Exercises:
# 1:
weight = 0.2
animal = "newt"
print(str(weight) + " kg is the weight of the " + animal)

# 2:
print("{} kg is the weight of the {}".format(weight, animal))

# 3:
print(f"{weight} kg is the weight of the {animal}")
