sum_of_evens = 0
for n in range(101):
    if n % 2 == 0:
        sum_of_evens = sum_of_evens + n

print(f"sum of evens number between 0 and 100 is: {sum_of_evens}")

# Using break statement: to stop/terminate the loop execution and exit to the
# next statement outside the loop:
for n in range(4):
    if n == 2:
        break
    print(f"n = {n}")

print(f"Finished with n = {n}")

# using the 'continue' statement: To terminate the execution of the current
# iteration and start a new one. This is skip any remaining code in the loop body
# and start a new iteration:
for i in range(4):
    if i == 2:
        continue
    print(f"n = {i}")
print(f"Finished with i = {i}")

# using for... else Loops: the else will be executed is the loops finish by exhastion
# this is completing all the iteration from the iterable. This is the break
# statement is not executed:
phrase = "it makes the spot"
for character in phrase:
    if character == "X":
        break
else:
    print("There was no 'X' in the phrase")

# This example gives a user three attempts to enter the right password:
for n in range(3):
    password = input("Enter password: ")
    if password == "I-pass":
        break
    print("Password is incorrect")
else:
    print("suspicious activity. the authorities have been alerted.")

# Exercise 1:
# Using break, write a program that repeatedly asks the user for some input
# and quits only if the user enters "q" or "Q":
while True:
    word = input("Enter something OR letter 'q' to exit. ")
    if word.upper() == "Q":
        break

# Exercise 2:
# Using continue, write a program that loops ovre the numbers 1 to 50 and
# prints all numbers that are not multiple of 3:
for i in range(1, 50):
    not_multiple_of_3 = i % 3 != 0
    if not_multiple_of_3:
        print(f"{i} is not a multiple of 3")

"""
Evaluation of Non-Boolean Values in Boolean Context
Many objects and expressions are not equal to True or False. Nonetheless, they
may still be evaluated in Boolean context and determined to be “truthy” or
“falsy.”
So what is true and what isn't? As a philosophical question, that is outside
the scope of this tutorial!
But in Python, it is well-defined. All the following are considered false when
evaluated in Boolean context:
The Boolean value False
Any value that is numerically zero (0, 0.0, 0.0+0.0j)
An empty string
An object of a built-in composite data type which is empty (see below)
The special value denoted by the Python keyword None
Virtually any other object built into Python is regarded as true.

You can determine the “truthiness” of an object or expression with the
built-in bool() function. bool() returns True if its argument is truthy and
False if it is falsy."""
# Numeric Value
# A zero value is false.
# A non-zero value is true.
print(bool(0), bool(0.0), bool(0.0 + 0j))

# result: False False False

print(bool(-3), bool(3.14159), bool(1.0 + 1j))

# result: True True True

# String
# An empty string is false.
# A non-empty string is true.

print(bool(""), bool(""), bool(""""""))

# result: False False False

print(bool("foo"), bool(" "), bool(""" """))

# result: True True True

"""
Built-In Composite Data Object
Python provides built-in composite data types called list, tuple, dict, and
set. These are “container” types that contain other objects. An object of one
of these types is considered false if it is empty and true if it is non-empty.
The examples below demonstrate this for the list type. (Lists are defined in
Python with square brackets.)

For more information on the list, tuple, dict, and set types, see the upcoming
tutorials. """
type([])
# result: <class 'list'>

bool([])
# result: False

type([1, 2, 3])
# result: <class 'list'>

bool([1, 2, 3])
# result: True

# The “None” Keyword
# None is always false:
bool(None)
# result: False

"""
Logical Expressions Involving Non-Boolean Operands
Non-Boolean values can also be modified and joined by not, or and, and. The
result depends on the “truthiness” of the operands.

“not” and Non-Boolean Operands
Here is what happens for a non-Boolean value x:
If x is	        not x is (return)
“truthy”	False
“falsy”	        True
Here are some concrete examples: """

x = 3
bool(x)
# return: True

not x
# return: False

x = 0.0
bool(x)
# return: False

not x
# return: True

"""
“or” and Non-Boolean Operands
This is what happens for two non-Boolean values x and y:
If x is 	x or y is (return)
truthy	        x
falsy	        y

Note that in this case, the expression x or y does not evaluate to either
True or False, but instead to one of either x or y:"""

x = 3
y = 4
x or y
# return x: 3

x = 0.0
y = 4.4
x or y
# return y: 4.4
# Even so, it is still the case that the expression x or y will be truthy if
# either x or y is truthy, and falsy if both x and y are falsy.

"""
“and” and Non-Boolean Operands
Here's what you'll get for two non-Boolean values x and y:
If x is	        x and y is (return)
“truthy”	y
“falsy”	        x """
x = 3
y = 4
x and y
# return y: 4

x = 0.0
y = 4.4
x and y
# return x: 0.0
# As with or, the expression x and y does not evaluate to either True or False,
# but instead to one of either x or y. x and y will be truthy if both x and y
# are truthy, and falsy otherwise.
"""
Compound Logical Expressions and Short-Circuit Evaluation
So far, you have seen expressions with only a single or or and operator and two
operands:
x or y
x and y
Multiple logical operators and operands can be strung together to form compound
logical expressions."""

# Compound “or” Expressions
"""Consider the following expression:
x1 or x2 or x3 or … xn
This expression is true if any of the xi are true.
In an expression like this, Python uses a methodology called short-circuit
evaluation, also called McCarthy evaluation in honor of computer scientist
John McCarthy. The xi operands are evaluated in order from left to right. As
soon as one is found to be true, the entire expression is known to be true. At
that point, Python stops and no more terms are evaluated. The value of the
entire expression is that of the xi that terminated evaluation.

To help demonstrate short-circuit evaluation, suppose that you have a simple
“identity” function f() that behaves as follows:
f() takes a single argument.
It displays the argument to the console.
It returns the argument passed to it as its return value.
(You will see how to define such a function in the upcoming tutorial on
Functions.) """


def f(value):
    print(f"f({value}): {value}")
    return value


# Several example calls to f() are shown below:

f(0)
# return: -> f(0) = 0
# return: 0

f(False)
# return: -> f(False) = False
# return: False

f(1.5)
# return: -> f(1.5) = 1.5
# return: 1.5

"""Because f() simply returns the argument passed to it, we can make the
expression f(arg) be truthy or falsy as needed by specifying a value for arg
that is appropriately truthy or falsy. Additionally, f() displays its argument
to the console, which visually confirms whether or not it was called.

Now, consider the following compound logical expression: """

f(0) or f(False) or f(1) or f(2) or f(3)
# return: -> f(0) = 0
# return: -> f(False) = False
# return: -> f(1) = 1
# return: 1
"""The interpreter first evaluates f(0), which is 0. A numeric value of 0 is
false. The expression is not true yet, so evaluation proceeds left to right.
The next operand, f(False), returns False. That is also false, so evaluation
continues.
Next up is f(1). That evaluates to 1, which is true. At that point, the
interpreter stops because it now knows the entire expression to be true. 1 is
returned as the value of the expression, and the remaining operands, f(2) and
f(3), are never evaluated. You can see from the display that the f(2) and f(3)
calls do not occur. """

# Compound “and” Expressions
"""A similar situation exists in an expression with multiple and operators:
x1 and x2 and x3 and … xn
This expression is true if all the xi are true.
In this case, short-circuit evaluation dictates that the interpreter stop
evaluating as soon as any operand is found to be false, because at that point
the entire expression is known to be false. Once that is the case, no more
operands are evaluated, and the falsy operand that terminated evaluation is
returned as the value of the expression:"""
f(1) and f(False) and f(2) and f(3)
# return: -> f(1) = 1
# return: -> f(False) = False
# return: False

f(1) and f(0.0) and f(2) and f(3)
# return: -> f(1) = 1
# return: -> f(0.0) = 0.0
# return: 0.0
"""In both examples above, evaluation stops at the first term that is
false—f(False) in the first case, f(0.0) in the second case—and neither the
f(2) nor f(3) call occurs. False and 0.0, respectively, are returned as the
value of the expression.

If all the operands are truthy, they all get evaluated and the last (rightmost)
one is returned as the value of the expression: """
f(1) and f(2.2) and f("bar")
# return: -> f(1) = 1
# return: -> f(2.2) = 2.2
# return: -> f(bar) = bar
# return: 'bar'"""

##### place holder
"""
Idioms That Exploit Short-Circuit Evaluation
There are some common idiomatic patterns that exploit short-circuit evaluation
for conciseness of expression. """

# Avoiding an Exception
# Suppose you have defined two variables a and b, and you want to know whether
# (b / a) > 0:
a = 3
b = 1
(b / a) > 0
# return: True

# But you need to account for the possibility that 'a' might be 0, in which case
# the interpreter will raise an exception:
a = 0
b = 1
# (b / a) > 0
"""Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    (b / a) > 0
ZeroDivisionError: division by zero """
# You can avoid an error with an expression like this:
a = 0
b = 1
a != 0 and (b / a) > 0
# return: False

# When a is 0, a != 0 is false. Short-circuit evaluation ensures that
# evaluation stops at that point. (b / a) is not evaluated, and no error is
# raised.

# If fact, you can be even more concise than that. When a is 0, the expression
# a by itself is falsy. There is no need for the explicit comparison a != 0:
a = 0
b = 1
a and (b / a) > 0
# retun: 0
"""
Selecting a Default Value
Another idiom involves selecting a default value when a specified value is
zero or empty. For example, suppose you want to assign a variable s to the
value contained in another variable called string. But if string is empty,
you want to supply a default value.

Here is a concise way of expressing this using short-circuit evaluation: """
# s = string or '<default_value>'
# If string is non-empty, it is truthy, and the expression string or
# '<default_value>' will be true at that point. Evaluation stops, and the
# value of string is returned and assigned to s:
string = "foo bar"
s = string or "<default_value>"
print(f"s = {s}")
# return: 'foo bar'
number = 34
r = number or 9999
print(f"r = {r}")
# return: 34

# On the other hand, if string is an empty string, it is falsy. Evaluation of
# string or '<default_value>' continues to the next operand, '<default_value>'
# , which is returned and assigned to s:
string = ""
s = string or "<default_value>"
print(s)
# return: '<default_value>'
number = 0
r = number or 9999
print(f"r = {r}")
# return: 9999

# Chained Comparisons
""" Comparison operators can be chained together to arbitrary length. For
example, the following expressions are nearly equivalent: 
x = 1
y = 2
z = 3

x < y <= z  (Chained comparison)
x < y and y <= z
They will both evaluate to the same Boolean value. The subtle difference
between the two is that in the chained comparison x < y <= z, 'y' is evaluated
only once. The longer expression x < y and y <= z will cause y to be evaluated
twice.

Note: In cases where 'y' is a static value, this will not be a significant
distinction. But consider these expressions, where using/repeatng a function:

x < f() <= z
x < f() and f() <= z
If f() is a function that causes program data to be modified, the difference
between its being called once in the first case and twice in the second case
may be important.

More generally, if op1, op2, …, opn are comparison operators, then the
following have the same Boolean value:
x1 op1 x2 op2 x3 … xn-1 opn xn (chained comparison)
x1 op1 x2 and x2 op2 x3 and … xn-1 opn xn (using 'and' operator)

In the former case, each xi is only evaluated once. In the latter case, each
will be evaluated twice except the first and last, unless short-circuit
evaluation causes premature termination."""

# Identity Operators
"""Python provides two operators, is and is not, that determine whether the
given operands have the same identity— that is, refer to the same object. This
is not the same thing as equality, which means the two operands refer to
objects that contain the same data but are not necessarily the same object.
Here is an example of two object that are equal but not identical:"""
x = 1001
y = 1000 + 1
print(f"x: {x}, y: {y}")
# return: 1001 1001

x == y
print(f" x == y : {x} == {y} -->", x == y)
# return: True

x is y
# return: False
print(f"x is y ", x is y)
# Here, x and y both refer to objects whose value is 1001. They are equal. But
# they do not reference the same object, as you can verify:
id(x)
# return: 60307920
id(y)
# return: 60307936
# x and y do not have the same identity, and x is y returns False.

# You saw previously that when you make an assignment like x = y, Python
# merely creates a second reference to the same object, and that you could
# confirm that fact with the id() function. You can also confirm it using the
# is operator:

a = "I am a string"
b = a
id(a)
# return: 55993992
id(b)
# return: 55993992

a is b
# return: True
a == b
# return: True
# In this case, since a and b reference the same object, it stands to reason
# that a and b would be equal as well.

# Unsurprisingly, the opposite of 'is' is 'is not':
x = 10
y = 20
x is not y
# return: True


# Operator Precedence
"""Consider this expression:

>>> 20 + 4 * 10
60
There is ambiguity here. Should Python perform the addition 20 + 4 first and
then multiply the sum by 10? Or should the multiplication 4 * 10 be performed
first, and the addition of 20 second?
Clearly, since the result is 60, Python has chosen the latter; if it had chosen
the former, the result would be 240. This is standard algebraic procedure,
found universally in virtually all programming languages.

All operators that the language supports are assigned a precedence. In an
expression, all operators of highest precedence are performed first. Once those
results are obtained, operators of the next highest precedence are performed.
So it continues, until the expression is fully evaluated. Any operators of equal
precedence are performed in left-to-right order.

Here is the order of precedence of the Python operators you have seen so far,
from lowest to highest:

 	            Operator	Description
lowest precedence	or	Boolean OR
                        and	Boolean AND
                        not	Boolean NOT
                        ==, !=, <, <=,
                        >, >=, is, is not -->comparisons, identity
                       |	bitwise OR
                       ^	bitwise XOR
                       &	bitwise AND
                     <<, >>	bit shifts
                    +, -	addition, subtraction
                    *, /, //, %	multiplication, division, floor division, modulo
              +x, -x, ~x	unary positive, unary negation, bitwise negation
highest precedence	**	exponentiation

Operators at the top of the table have the lowest precedence, and those at the
bottom of the table have the highest. Any operators in the same row of the table
have equal precedence.
It is clear why multiplication is performed first in the example above:
multiplication has a higher precedence than addition.
Similarly, in the example below, 3 is raised to the power of 4 first, which
equals 81, and then the multiplications are carried out in order from left to
right (2 * 3 ** 4 * 5 = 810):"""

print("2 * 3 ** 4 * 5 = 810 =  ", 2 * 3**4 * 5)
# return: 810

# Operator precedence can be overridden using parentheses. Expressions in
# parentheses are always performed first, before expressions that are not
# parenthesized. Thus, the following happens:

print(" 20 + 4 * 10 = 60 = ", 20 + 4 * 10)
# return: 60
print(" (20 + 4) * 10 = 240 = ", (20 + 4) * 10)

print(" 2 * 3 ** 4 * 5 = 810 = ", 2 * 3**4 * 5)

print(" 2 * 3 ** (4 * 5) = 6973568802", 2 * 3 ** (4 * 5))

# In the first example, 20 + 4 is computed first, then the result is multiplied
# by 10. In the second example, 4 * 5 is calculated first, then 3 is raised to
# that power, then the result is multiplied by 2.

# There is nothing wrong with making liberal use of parentheses, even when they
# aren't necessary to change the order of evaluation. In fact, it is considered
# good practice, because it can make the code more readable, and it relieves
# the reader of having to recall operator precedence from memory. Consider the
# following:

# (a < 10) and (b > 30)
# Here the parentheses are fully unnecessary, as the comparison operators have
# higher precedence than and does and would have been performed first anyhow.
# But some might consider the intent of the parenthesized version more
# immediately obvious than this version without parentheses:

# a < 10 and b > 30
# On the other hand, there are probably those who would prefer the latter;
# it's a matter of personal preference. The point is, you can always use
# parentheses if you feel it makes the code more readable, even if they aren't
# necessary to change the order of evaluation.


# Augmented Assignment Operators:
"""You have seen that a single equal sign (=) is used to assign a value to a
variable. It is, of course, perfectly viable for the value to the right of the
assignment to be an expression containing other variables:

>>> a = 10
>>> b = 20
>>> c = a * 5 + b
>>> c
70
In fact, the expression to the right of the assignment can include references
to the variable that is being assigned to:

>>> a = 10
>>> a = a + 5
>>> a
15

>>> b = 20
>>> b = b * 3
>>> b
60
The first example is interpreted as “a is assigned the current value of 'a'
plus 5,” effectively increasing the value of a by 5. The second reads “b is
assigned the current value of b times 3,” effectively increasing the value of
'b' threefold.

Of course, this sort of assignment only makes sense if the variable in question
has already previously been assigned a value:
>>> z = z / 12
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    z = z / 12
NameError: name 'z' is not defined
Python supports a shorthand augmented assignment notation for these arithmetic
and bitwise operators:

Arithmetic	Bitwise
    +           &
    -           |
    *           ^
    /           >>
    %           << 
    //
    **	
For these operators, the following are equivalent:

x <op>= y
x = x <op> y
Take a look at these examples:

Augmented                       Standard
Assignment		        Assignment
a += 5	  is equivalent to	a = a + 5
a /= 10	  is equivalent to	a = a / 10
a ^= b	  is equivalent to	a = a ^ b """

# Conclusion:
# In this tutorial, you learned about the diverse operators Python supports to
# combine objects into expressions.

# Most of the examples you have seen so far have involved only simple atomic
# data, but you saw a brief introduction to the string data type. The next
# tutorial will explore string objects in much more detail.
