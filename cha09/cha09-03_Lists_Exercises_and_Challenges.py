# Exercises:
# 1: Create a tuple called data with two values. The first value should be the
# tuple (1, 2), and the second (3, 4):
data = ((1, 2), (3, 4))

# 2: Write a 'for loop' that loops over data and prints the sum of each nested
# tuple. The output should look like this:
# Row 1 sum 3
# Row 2 sum 7
i = 1
for tuple_item in data:
    sum_1 = tuple_item[0] + tuple_item[1]
    print(f"Row {i} sum: {sum_1}")
    i += 1

# 3: Create the list [4, 3, 2, 1] and assign it to the variable numbers
numbers = [4, 3, 2, 1]
print(f"numbers: {numbers}")

# 4: Create acopy of the numbers ist using the [:] slice notation:
numbers_copy = numbers[:]
print(f"numbers_copy: {numbers_copy}")

# 5: Sort the numbers list in numerical order using .sort():
numbers.sort()
print(f"numbers list sorted: {numbers}")

# Challenge 9.4:
from statistics import mean, median

universities = [
    ["California Institute of Technologies", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technologies", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]


def enrollment_stats(universities_list):
    student_enrollment_list = []
    tuition_fees_list = []
    for university in universities_list:
        student_enrollment_list.append(university[1])
        tuition_fees_list.append(university[2])

    return [student_enrollment_list, tuition_fees_list]


def mean_function(single_list):
    return mean(single_list)


student_enrolled_list, tuition_fees_list = enrollment_stats(universities)

total_students = sum(student_enrolled_list)
total_tuition = sum(tuition_fees_list)

student_mean = mean_function(student_enrolled_list)
student_median = median(student_enrolled_list)

tuition_mean = mean_function(tuition_fees_list)
tuition_median = median(tuition_fees_list)

print()
print("***************************")
print(f"Total students:   {total_students:,}")
print(f"Total tuition:  ${total_tuition: ,}")
print()

print(f"Student mean:    {student_mean: ,.2f}")
print(f"student_median:   {student_median}")
print()

print(f"Tuition mean:   ${tuition_mean: ,.2f}")
print(f"Tuition median: ${tuition_median: ,}")

print(f"sum: {sum(tuition_fees_list): ,}")
print("***************************")
print()


# challenge # 9.5:
import random

# Create lists:
nouns = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glisterning"]
prepositions = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiosly", "sensuously"]

# Select elements from each list:
noun1 = random.choice(nouns)
noun2 = random.choice(nouns)
noun3 = random.choice(nouns)

verb1 = random.choice(verbs)
verb2 = random.choice(verbs)
verb3 = random.choice(verbs)

adj1 = random.choice(adjectives)
adj2 = random.choice(adjectives)
adj3 = random.choice(adjectives)

prep1 = random.choice(prepositions)
prep2 = random.choice(prepositions)

adverb1 = random.choice(adverbs)

print(
    f"{'A' if adj1[0] not in ('a', 'e', 'i', 'o', 'u') else 'An'} \
{adj1} {noun1}"
)
print()
print(
    f"{'A' if adj1[0] not in ('a', 'e', 'i', 'o', 'u') else 'An'} \
{adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}"
)
print(f"{adverb1}, the {noun1} {verb2}")
print(f"the {noun2} {verb3} {prep2} a {adj3} {noun3}")
