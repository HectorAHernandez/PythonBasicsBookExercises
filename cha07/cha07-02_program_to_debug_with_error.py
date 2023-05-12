def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word += word[i] + "_"
        print(f"i = {i}; new_word = {new_word}")
    return new_word


phrase = "hello"
print(add_underscores(phrase))


# Refactoring the above code:
# The process of rewriting existing code to be cleaner,  easier to read and
# understand, or more in line with the standards set by a team is called REFACTORING.
def add_underscores_v2(word):
    new_word = "_"
    for letter in word:
        new_word += letter + "_"
    return new_word


phrase = "excellente code"
print(add_underscores_v2(phrase))
