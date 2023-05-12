n = 5
while n > 0:
    n -= 1
    print(n)

# When a list is evaluated in Boolean context, it is truthy if it has elements in it and
# falsy if it is empty. In below example, a is true as long as it has elements in it. Once all
# the items have been removed with the .pop() method and the list is empty, a is false, and the
# loop terminate:
a = ["foo", "bar", "baz"]
while a:
    print(
        a.pop(-1)
    )  # the index of .pop() has to be '-1' to indicate the last object in the list
    # .pop() delete the last object in the list.

print(f"list 'a' {a}")

b = ["111", "222", "333"]
while b:
    print(
        b.pop(-1)
    )  # the index of .pop() has to be '-1' to indicate the last object in the list

print(f"list 'b': {b}")

# Python break and continue statements are use to terminate a loop interation prematurely:
# continue statement: immediately terminates the current loop iteration. So the execution jumps to the top
# of the loop, and the controlling expression is re-evaluated to determine whether the loop will
# execute again or terminate.
#
# break statement: immediately termnates a loop entirely. This is the program execution proceeds
# to the first stemenet following the loop body:
# break example:
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(f"n = {n}")
print("loop termnated (break) when n got the value 2")

# continue example: it is equal to the previous one, but instead of breaking when n == 2 it will
#                   terminate the current iteration, not printing the value 2 of 'n' variable:
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(f"n = {n}")
print("loop ended processing all iterations and skipping iteration with n == 2")

# The ELSE clause: Python allows an optional else clause at the end of the whle loop. this is
# a unique feature of Python, not found in most other programming languages. This is the syntax:
# while <expression>:
#      <statements>
#  else
#      <additional statement(s)>

# when the <additional statement(s)> are placed in an ELSE clause, they will be executed ONLY IF
# the loop terminates "by exhaustion" - that is, if the llop iterates until the controlling
# condition becomes False. If a loop is exited by a brake statement, the ELSE clause won't be
# executed.
n = 5
while n > 0:
    n -= 1
    print(f"n = {n}")
else:
    print("Loop done by exhaustion")

# another one with the brake statement:
n = 5
while n > 0:
    n -= 1
    print(f"n = {n}")
    if n == 2:
        break  # this loop is terminated  prematurely with break, so else clause is not executed.
else:
    print("Loop done won't be printed")

# Else can be used when searching a list for a specific item, using break when the item is found,
# and the else clause can contain code that is meant to be executed if the item is not found:
a = ["foo", "bar", "baz", "qux"]
search = "aaa"

i = 0
while i < len(a):
    if a[i] == search:
        # processing statements when item found
        break
    i += 1
else:
    # processing for item not found
    print(f"{search} not found in list.")

# The code shown above is useful to illustrate the concept, but you would actually be very
# unlikely to search a list that way, because:
# 1- Lists are usually processed with definite iteration (for ...loop), not while loop.
# 2- Python provides built-in ways to search for an item in a list. We can use the "in" operator.
search = "foo"
if search in a:
    print(f"{search} found in list.")
else:
    print(f"{search} not found in list.")


# The list.index() method would also work. This method raises a ValueError exception if the
# item is not found in the list. In Python we use a 'try' statement to handle exception:
search = "bbb"
try:
    print(a.index(search))
except ValueError:
    print(f"cha06-07_While_Loop_Tutorial.py")

# An 'else' clause with a while loop is a bit an oddity, not often seen. but don't shy away
# from it if find a situation in which you feel it adds clarity to our code!!!

# "Infinite Loops" -- while True: .....
""" but this pattern is actually quite common. For example, you might write code for a service that
starts up and runs forever accepting service requests. “Forever” in this context means until you shut
it down,
More prosaically, remember that loops can be broken out of with the break statement. It may be more
straightforward to terminate a loop based on conditions recognized within the loop body, rather than on
a condition evaluated at the top.

Here's another variant of the loop shown above that successively removes items from a list using .pop()
until it is empty:
"""
a = ["foo", "bar", "baz"]
while True:
    if not a:
        break
    print(f"element deleted from the list: {a.pop(-1)}")
# after deleting the last element from the list then the list 'a' becomes empty and therefore the
# condition "if not a:" becomes true and then the executed break statement exits the Infinite loop.
# We can also specify multiple break statements in an Infinite loop:
""" while True:
        if <expr1>: # One condition for loop termination.
            break
        ...
        if <expr2>: # Another termination condition.
            break
        ...
        if <expr3>: # Yet another
            break
In cases like this, where there are multiple reasons to end the loop, it is often cleaner to break out
from several different locations, rather than try to specify all the termination conditions in the loop
header.

Infinite loops can be very useful. Just remember that you must ensure the loop gets broken out of at
some point, so it doesn't truly become infinite.
"""

d = {"foo": 1, "bar": 2, "baz": 3}
while d:
    print(f"deleted item from dictionary: {d.popitem()}")
print(f"dictionary d is empty: {d}")
print("Done.")

a = ["foo", "bar", "baz", "qux", "corge"]
while a:
    if len(a) < 3:
        break
    print(f"deleted from list a: {a.pop()}")
print("Done.")
print(f"remaining in list a: {a}")
""" When no arguments are specified, a.pop() removes and returns the last item in a. So each time
through the loop, the last item is displayed.
But when the loop contains fewer than three items, the break statement on line 4 is reached, and the
loop is terminated. Execution then proceeds to the print() statement following the loop, on line 6."""

s = ""
n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue

    a = ["foo", "bar", "baz"]
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break
print(f"expected value of s is '3foo3bar1foo1bar' --> {s} ")

# Nested while Loops:
# In general, Python control structures can be nested whthin one another, for example if/elif/else:
age = 34
gender = "F"
if age < 18:
    if gender == "M":
        print("son")
    else:
        print("daughter")
elif age >= 18 and age < 65:
    if gender == "M":
        print("Father")
    else:
        print("Mother")
else:
    if gender == "M":
        print("Grandfather")
    else:
        print("Grandmother")

# Similarly, a while loop can be contained within another while loop, as shown below:
a = ["foo", "bar", "hec"]
while len(a):
    print(
        f"deleted element from list a: {a.pop(0)}"
    )  # delete the first element (index 0) of a list.
    b = ["baz", "qux"]
    while len(b):
        print(f"from list b: --> {b.pop(0)} ")
print(f"list a content: {a} and list b: {b}")

""" A break or continue statement found within nested loops applies to the nearest enclosing loop:

while <expr1>:
    statement
    statement

    while <expr2>:
        statement
        statement
        break  # Applies to while <expr2>: loop

    break  # Applies to while <expr1>: loop

Additionally, while loops can be nested inside if/elif/else statements, and vice versa:

if <expr>:
    statement
    while <expr>:
        statement
        statement
else:
    while <expr>:
        statement
        statement
    statement
 
while <expr>:
    if <expr>:
        statement
    elif <expr>:
        statement
    else:
        statement

    if <expr>:
        statement
In fact, all the Python control structures can be intermingled with one another to whatever extent you
need. That is as it should be. Imagine how frustrating it would be if there were unexpected
restrictions like “A while loop can't be contained within an if statement” or “while loops can only be
nested inside one another at most four deep.” You'd have a very difficult time remembering them all.

Seemingly arbitrary numeric or logical limitations are considered a sign of poor program language
design. Happily, you won't find many in Python.
    
"""
# One-Line while loops:
# As with an "if" statement, a while loop can be specified on one line. if there are multiple statements
# in the block that makes up the loop body, they can be separated by semicolons (;) as follow:
n = 5
while n > 0:
    n -= 1
    print(f"n = {n}")
    print(f" 'n' reduced: {n -1}")

"""  This only works with simple statements though. You can't combine two compound statements into one
line. Thus, you can specify a while loop all on one line as above, and you write an if statement on one
line: """

if True:
    print("foo")

# But you can't do this:

""" while n > 0: n -= 1; if True: print('foo')
SyntaxError: invalid syntax
Remember that PEP 8 discourages multiple statements on one line. So you probably shouldn't be doing
any of this very often anyhow"""
