x = "Hello World"


def func():
    x = 2
    print(f"Inside 'func()' x has the value '2' = {x}")


func()
print(f"Outside 'func()', x has the value 'Hello World' = {x}")

# The func() body has its own set of names available to it. Code outside the function body is in global scope.
# Scope is a set of names mapped to objects. When we are using a particular name in our code, such
# as a variable or function name, Python checks the current scope to determine whether that
# name exists.

# Scope resolution: Scope has a hierarchy, example:
x = 5


def outer_func():
    y = 3

    def inner_func():
        z = x + y
        return z

    print(inner_func())
    return inner_func()


outer_func()

# inner_func() is called an inner function because it is defined inside another function. it
# same as nesting loop.
# the variable 'z' is in the Local Scope of the inner_func(). When Python execute the line:
# z = x + y, it looks for variable x and y in the Local Scope. Neither of them exist there, so
# Python moves up to the scope of the outer_func().
# The Scope for the outer_func() is an Enclosing scope of inner_func(). It is not quite the
# Global Scope, nor is it the Local Scope for inner_func(). it lies between the two.
# The variable y is defined in the scope of the outer_func() and is assigned the value 3. However
# variable x does not exists in this scope, so Python moves up once again to the Global Scope. There
# it finds the name x, which has the value 5. Now that the names x and y are resolved, Python
# can execute the line z = x + y. which assigns to z the value of 8.

# The LEGB (Local, Enclosing, Global, Built-in) Rule:
# Local Scope: The local or current, scope could be the body of a function or the top-level scope of
# a code file. It always represents the scope that the Python interpreter is currently working in.
#
# Enclosing Scope: The enclosing scope is the scope one level up from the local scope. If the local
# scope is an inner function, then the Enclosing scope is the outer function. If the scope is
# a top-level function, then the Enclosing scope is the same as the Global Scope.
#
# Global Scope: The Global Scope is the topmost scope in a program. It contains all the names
# defined in the code that are not contained in a function body.
#
# Built-in Scope: Contains all the names, such as key-words, that are built into Python. Functions
# such as round() and abs() are in the built-in scope. Anything that we can use without first
# defining it ourself is contained in the built-in scope.

# Brake the Rule:
total = 0


def add_to_total(n):
    total = total + n


add_to_total(5)
print(total)

""" Traceback (most recent call last):
  File "C:/PythonBasicsBookExercises/cha06/cha06-06_Understanding_Scope_In_Python.py", line 64, in <module>
    add_to_total(5)
  File "C:/PythonBasicsBookExercises/cha06/cha06-06_Understanding_Scope_In_Python.py", line 62, in add_to_total
    total = total + n
UnboundLocalError: local variable 'total' referenced before assignment
>>>  """
# The above error is generated because of this problem: the code attempts to make an assignment
# to the variable 'total' (total = total + n), which create a new name in the Local Scope. Then,
# when Python executes the right-hand side of the assignment, it finds the name 'total' in the
# Local Scope with nothing assigned to it yet.
# This kind of error "UnboundLocalError: local variable 'total' referenced before assignment" are
# tricky and are one of the reasons it is best to use unique variable and function names no
# matter which scope you are in.
# We can get around this issue with the 'global' keyword (But this is not a best practice):
total = 0


def add_to_total(n):
    global total
    total = total + n


add_to_total(5)
print(total)

# the keyword 'global' with the total variable, tells Python to look in the Global Scope area
# for the name total. That way, the line total = total + n doesn't create a new Local variable.
# Although this "fixes" the program, the use of the 'global' keyword is considered bad form in
# general. If you find yourself using 'global' keyword to fix problems like the one above, stop
# and think if there's a better way to write your code. Often, you will find that there is.
