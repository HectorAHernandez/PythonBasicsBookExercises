# Do lines execute?

if "foo" in ["foo", "bar", "baz"]:
    print("Outher condition is True")

    if 10 > 20:
        print("Inner condition 1")

    print("Between inner conditions")

    if 10 < 20:
        print("Inner condition 2")

    print("End of Outer condition")
print("After outer condition")

# using if..elif..else:
name = "Joe"
if name == "Fred":
    print("Hello Fred")
elif name == "Xander":
    print("Hello Xander")
elif name == "Joe":
    print("hello Joe")
elif name == "Arnold":
    print("hello Arnold")
else:
    print("I don't know who you are")

# now using a better Pythonic way for the above code:
names = {
    "Fred": "Hello Fred",
    "Xander": "Hello Xander",
    "Joe": "Hello Joe",
    "Arnold": "Hello Arnold",
}

print(names.get("Joe", "I don't know who you are!"))
print(names.get("Rick", "I don't know who you are!"))
print(names.get("Xander"))
print(names.get("Fred"))
print(names.get("Carlos", "Carlos is not in the names dictionary"))

"""
Conditional Expressions (Python's Ternary Operator)
Python supports one additional decision-making entity called a conditional
expression. (It is also referred to as a conditional operator or ternary
operator in various places in the Python documentation.) Conditional
expressions were proposed for addition to the language in PEP 308 and
green-lighted by Guido in 2005.

In its simplest form, the syntax of the conditional expression is as follows:
<expr1> if <conditional_expr> else <expr2>
This is different from the if statement forms listed above because it is not a
control structure that directs the flow of program execution. It acts more
like an operator that defines an expression. In the above example,
<conditional_expr> is evaluated first. If it is true, the expression evaluates
to <expr1>. If it is false, the expression evaluates to <expr2>.

Notice the non-obvious order: the middle expression is evaluated first, and
based on that result, one of the expressions on the ends is returned. Here are
some examples that will hopefully help clarify: """
raining = False
print("Let's go to the", "beach" if not raining else "Library")
raining = True
print("Let's go to the", "beach" if not raining else "Library")

age = 12
s = "minor" if age < 21 else "adult"
print(f"s = {s}")

print("yes" if ("qux" in ["foo", "bar", "baz"]) else "no")

"""
Note: Python's conditional expression is similar to the <conditional_expr> ?
<expr1> : <expr2> syntax used by many other languages—C, Perl and Java to name
a few. In fact, the ?: operator is commonly called the ternary operator in
those languages, which is probably the reason Python's conditional expression
is sometimes referred to as the Python ternary operator.

You can see in PEP 308 that the <conditional_expr> ? <expr1> : <expr2> syntax
was considered for Python but ultimately rejected in favor of the syntax shown
above.

A common use of the conditional expression is to select variable assignment.
For example, suppose you want to find the larger of two numbers. Of course,
there is a built-in function, max(), that does just this (and more) that you
could use. But suppose you want to write your own code from scratch.

You could use a standard if statement with an else clause: """
a = 30
b = 90

if a > b:
    m = a
else:
    m = b

# But a conditional expression is shorter and arguably more readable as well:
m = a if a > b else b
# Remember that the conditional expression behaves like an expression
# syntactically. It can be used as part of a longer expression. The conditional
# expression has lower precedence than virtually all the other operators, so
# parentheses are needed to group it by itself."""

#
# In the following example, the + operator binds more tightly than the conditional
# expression, so 1 + x and y + 2 are evaluated first, followed by the conditional
# expression. The parentheses in the second case are unnecessary and do not
# change the result:
x = y = 40

z = 1 + x if x > y else y + 2
print(f"z = 42 = {z}")

z = (1 + x) if x > y else (y + 2)
print(f"z = 42 = {z}")

# If you want the conditional expression to be evaluated first, you need to
# surround it with grouping parentheses. In the next example, (x if x > y else
# y) is evaluated first. The result is y, which is 40, so z is
# assigned 1 + 40 + 2 = 43:
x = y = 40

z = 1 + (x if x > y else y) + 2
print(f"z = 43 = {z}")

# If you are using a conditional expression as part of a larger expression, it
# probably is a good idea to use grouping parentheses for clarification even
# if they are not needed.

# Conditional expressions also use short-circuit evaluation like compound logical
# expressions. Portions of a conditional expression are not evaluated if they
# don't need to be.

# In the expression <expr1> if <conditional_expr> else <expr2>:
# If <conditional_expr> is true, <expr1> is returned and <expr2> is not evaluated.
# If <conditional_expr> is false, <expr2> is returned and <expr1> is not evaluated.
# As before, you can verify this by using terms that would raise an error:

# >>> 'foo' if True else 1/0
# 'foo'
# >>> 1/0 if False else 'bar'
# 'bar'
# In both cases, the 1/0 terms are not evaluated, so no exception is raised.

# Conditional expressions can also be chained together, as a sort of alternative
# if/elif/else structure, as shown here:

# >>> s = ('foo' if (x == 1) else
# ...      'bar' if (x == 2) else
# ...      'baz' if (x == 3) else
# ...      'qux' if (x == 4) else
# ...      'quux'
# ... )
# >>> s
# 'baz'
# It's not clear that this has any significant advantage over the corresponding
# if/elif/else statement, but it is syntactically correct Python.


#
# The Python pass Statement
# Occasionally, you may find that you want to write what is called a code
# stub: a placeholder for where you will eventually put a block of code that you
# haven't implemented yet.

# In languages where token delimiters are used to define blocks, like the curly
# braces in Perl and C, empty delimiters can be used to define a code stub. For
# example, the following is legitimate Perl or C code:

# # This is not Python
# if (x)
# {
# }
# Here, the empty curly braces define an empty block. Perl or C will evaluate
# the expression x, and then even if it is true, quietly do nothing.

# Because Python uses indentation instead of delimiters, it is not possible to
# specify an empty block. If you introduce an if statement with if <expr>:,
# something has to come after it, either on the same line or indented on the
# following line.

# More..

# Consider this script foo.py:
# if True:

# print('foo')
# If you try to run foo.py, you'll get this:

# C:\Users\john\Documents\Python\doc>python foo.py
#   File "foo.py", line 3
#     print('foo')

# IndentationError: expected an indented block
# The Python pass statement solves this problem. It doesn't change program
# behavior at all. It is used as a placeholder to keep the interpreter happy in
# any situation where a statement is syntactically required, but you don't
# really want to do anything:

# if True:
#     pass

# print('foo')
# Now foo.py runs without error:

# C:\Users\john\Documents\Python\doc>python foo.py
# foo
# Conclusion
# With the completion of this tutorial, you are beginning to write Python code
# that goes beyond simple sequential execution:

# You were introduced to the concept of control structures. These are compound
# statements that alter program control flow—the order of execution of program
# statements.
# You learned how to group individual statements together into a block or suite.
# You encountered your first control structure, the if statement, which makes it
# possible to conditionally execute a statement or block based on evaluation of
# program data.
# All of these concepts are crucial to developing more complex Python code.

# The next two tutorials will present two new control structures: the while
# statement and the for statement. These structures facilitate iteration,
# execution of a statement or block of statements repeatedly.

print(f"**** end *****")
