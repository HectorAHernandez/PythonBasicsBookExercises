# this program contains information on how to handle string data type:

paragraph = "this planter ha - or rather had - a problem. which was \
this: mos of the perople living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concernred with the movements of small \
green piece of paper, which is odd because on the whole it wan not \
the small green pieces of paper that were unhappy."
print("paragraph --> ", paragraph)
print()

long_string = "This multiline string is \
displayed on one line"
print("long_string -->", long_string)
print()

# we can also create a multiline strings using triple quotes (""" or ''') as
# delimeters.Here is how to write a long paragraph using this approach:
paragraph_with_doublequotes = """ this planter ha - or rather had - a problem. which was
this: mos of the perople living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concernred with the movements of small
green piece of paper, which is odd because on the whole it wan not
the small green pieces of paper that were unhappy. """
print("paragraph_with_doublequotes -->", paragraph_with_doublequotes)
print()

paragraph_with_singlequotes = ''' this planter ha - or rather had - a problem. which was
this: mos of the perople living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concernred with the movements of small
green piece of paper, which is odd because on the whole it wan not
the small green pieces of paper that were unhappy. '''
print("paragraph_with_singlequotes -->", paragraph_with_singlequotes)
# triple quoted strings preserve whitespace, including newlines. This means that
# running print(paragraph_with...) would display the string on multiple lines, just
# as it appears in the string liter. This may or may not be what you wanted, so we
# have to keep in mind the output we want when choosing the multiline approach;
# because the "\" at the end print every thing in one line.
