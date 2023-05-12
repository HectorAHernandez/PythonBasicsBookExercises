num = float(input("Enter a positive number: "))
while num <= 0:
    print(f"{num: .2f} is not a positive number")
    num = float(input("Enter a positive number: "))

word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index = index + 1

print()

# Same as above but with for loop:
for letter in "Python":
    print(letter)

# for loop with range:
for n in range(7):
    print(f"{n} Python")

# for loop with range using starting point for the range:
for n in range(10, 20):
    print(f"{n} square is {n * n}")

# another one:
amount = float(input("Enter an amount: "))
for number_people in range(3, 10):
    print(f"{number_people} people: {amount / number_people: ,.2f} each.")

# Nested for loops:
for n in range(1, 4):
    for j in range(6, 9):
        print(f"n = {n} and j = {j}")
