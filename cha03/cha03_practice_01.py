month_last_day = 31
print(month_last_day)

# this is a block comment, using the # at the beginning of the line:
greeting = "Hello World"
greeting
print(greeting)  # this is an inline commentm, # at the end of the line.

print("the # can be used inside a string")

# if the comment is big, then we can
# use multiple # at the beginning of the line.

##To comment out a section of the code in the IDLE, highlight one or more of the
##lines to be commented and press Alt+3, to roll it back Alt+4

commented_section = "To comment out a section of the code in the IDLE, highlighted one or more of the lines to be commented and press Alt+3, to roll it back Alt+4"
print(commented_section)

## When debugging, it is important to have a methodological approach to help you
## find where things are breaking down. Going through your code in the order in
## which it is executed and making sure each part works is a great way to do this.
##
## Once you have an idea of where things might be breaking down, insert the following
## line of code into your script:
""" import pdb; pdb.set_trace() #  and run it. This is the Python debugger and will """
## drop you into interactive mode. The debugger can also be run from the command line with:
## python -m pdb <my_file.py>.

my_string = "I am a string"
print("dir(my_string) -->", dir(my_string))

print("my_string.upper() -->", my_string.upper())

print("\ntype(my_string) -->", type(my_string))

# print("\nhelp(str) -->", help(str))

from datetime import datetime

print("\ndir(datetime) -->", dir(datetime))

print("\ndatetime.now()", datetime.now())

import os

os.system("dir")
print("\nos.system('dir') -->", os.system("dir"))

## Tip #9: Ask “GOOD” Questions
## People always say there is no such thing as a bad question, but when it comes to programming, it is
## possible to ask a question badly. When you are asking for help from someone who has little or no
## context on the problem you are trying to solve, its best to ask GOOD questions by following this acronym:
##
## G: Give context on what you are trying to do, clearly describing the problem.
## O: Outline the things you have already tried to fix the issue.
## O: Offer your best guess as to what the problem might be. This helps the person who is helping you to not
##    only know what you are thinking, but also know that you have done some thinking on your own.
## D: Demo what is happening. Include the code, a traceback error message, and an explanation of the steps you
##    executed that resulted in the error. This way, the person helping does not have to try to recreate the issue.
## Good questions can save a lot of time. Skipping any of these steps can result in back-and-forth conversations
## that can cause conflict. As a beginner, you want to make sure you ask good questions so that you practice
## communicating your thought process, and so that people who help you will be happy to continue helping you.


""" using 3 double quotes is another way
to write a multiple
lines comment in Python """
print('\nJust created a multiple lines comments using 3 "')

""" This is like multiline comments in Java, where everything enclosed in the triple quotes will function as a
comment.
While this gives you the multiline functionality, this isn't technically a comment. It's a string that's not
assigned to any variable, so it's not called or referenced by your program. Still, since it'll be ignored at
runtime and won't appear in the bytecode, it can effectively act as a comment. (You can take a look at this
article for proof that these strings won't show up in the bytecode.)

However, be careful where you place these multiline “comments.” Depending on where they sit in your program,
they could turn into docstrings, which are pieces of documentation that are associated with a function or method.
If you slip one of these bad boys right after a function definition, then what you intended to be a comment will
become associated with that object.

Be careful where you use these, and when in doubt, just put a hash mark on each subsequent line. If you're
interested in learning more about docstrings and how to associate them with modules, classes, and the like,
check out our tutorial on Documenting Python Code."""


def a():
    a = 2
    ab = 2 * a


def b():
    b3 = 3


def c():
    month_last_day = 31
    print(month_last_day)
