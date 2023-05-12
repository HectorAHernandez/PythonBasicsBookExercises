# 1:
word = input("Enter a word: ")
if len(word) < 5:
    print(f"your input is less than 5 characters long")
elif len(word) > 5:
    print(f"Your input is greater than 5 charactes long")
else:
    print(f"your input is 5 characters long")

# 2:
number = int(input("I'm thinking of a numer between 1 and 10. Guess which one. "))
if number == 3:
    print("You win!!!!!")
else:
    print("You lose")

# Challenge: Find the factor of a number:
number = abs(int(input("Enter a number: ")))
for i in range(1,number + 1):
    factor = number % i == 0
    if factor:
        print(f"{i} is a factor of {number}.")
        
