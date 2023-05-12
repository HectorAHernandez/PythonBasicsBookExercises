phrase = "The surprise is here somewhere"
print(phrase)
phrase.find("surprise")
print(phrase.find("surprise"))
phrase.find("here")
print(phrase.find("here"))
phrase.find("hector")
print(phrase.find("hector"))
"I put a string in your string".find("string")
# "my number is 555-555-5555".find(5)
"my number is 555-555-5555".find("5")


my_story = "I'am telling you the truth, nothing but the truth"
print(my_story)
my_story.replace("the truth","lies")
print(my_story)
my_story = my_story.replace("the truth","lies")
print(my_story)
text = "some of the stuff"
print(text)
new_text = text.replace("some of","all")
print(new_text)
new_text = new_text.replace("stuf","things")
print(new_text)

# Chapter exercises:
# 1:
print("The result of 'AAA'.find('a') must be -1 --> {} ".format("AAA".find("a")))
print(f"The result of 'AAA'.find('a') must be -1 --> {'AAA'.find('a')} ")

print('Somebody said something to Samanthas.'.replace('s','x'))
print("Somebody said something to Samanthas.".replace("s","x"))

letter_to_find = input("Enter letter to find: ")
text1 = input("Enter a text: ")
print(f"The first locatin of the letter '{letter_to_find}' is in index {text1.find(letter_to_find)} ")
