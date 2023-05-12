# Classes vs Instances:
"""Classes are used to create user-defined data structures. A class defines
functions called 'methods', which identify the behaviors and actions that an
object, created from the class, can perform with the its data.
A class is a blueprint for how something/object should be defined. A class
doesn't actually contain any data. The Dog class specifies that a name and an
age are necessary for defining a dog/object created from it, but the class
doesn't contain the name or age of any specific dog.

While the class is the blueprint, an 'instance' is an object that is built from
a class and contains real data. An instance of a Dog class is not a blueprint
anymore, It is an actual dog with a name, like Miles, who's 4 years old.

Put in another way, a class is like a form or questionnaire. An instance is
like a form that has been filled out with information. Just like many people
can fill out the same form with their own unique information, many instances
can be created from the same class.

How to Define a class:
all class definitions start with the 'class' keyword, which is followed by the
name of the class (starting with Uppercase) and a colon ':'. Any code that is
indented below the class definition is considered part of the class's body.
Example:
class Dog:
    pass

The body of the Dog class consists of a single statement: the 'pass' keyword.
'pass' is often used as a placeholder indicating where code will eventually go.
It allows us to run this code without Python throwing an error.

Note: Python class names are written in CapitalizedWords notation by convention,
for example, a class for a specific breed of dog like the Jack Russel Terrier
would be written as 'JackRusselTerrier' (CamelStyle)


"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


""" The properties that all Dog objects must have are defined in a method
called .__init__(). When a new Dog object (or for child class) is
instantiated/created, .__init__() is executed, therefore, setting the initial
state of the created object by assigning the values of the object's properties.
That is, .__init__() initializes each new instance of the class or child class.
We can give .__init__() any number of parameters, but the first parameter will
always be a 'variable' called 'self' (Note: 'self' is the Python convention; but
it can be any other variable name; but we need to keep in mind it to use it
accordingly, example:
class Cat:
    def __init__(obj_addr, name, color):
	obj_addr.name = name
	obj_addr.color = color
	print(f"obj_addr --> {obj_addr}")
).
When a new class instance/object is
created, the instance-number /object-address is automatically passed to the
'self' parameter/variable in .__init___() so that the new
attributes/instance-variables can be defined on the object or as belonging to
the created instance/object.

In the body of the .__init__() method, there are two statements using the
'self' variable:
1- self.name = name: creates an attribute called 'name' and assign to it the
   value of the 'name' parameter.
2- self.age = age: creates an attribute called 'age' and assign to ti the value
    of the 'age' parameter.

Instance attribute:
Attributes created in the .__init__() method are called instance attributes. An
instance attribute's value is specific to a particular instance of the class.
All Dog objects have a name and an age, but the values for the name and age
attributes will vary depending on the Dog instance.

Class attribute:
Are attributes that have the same value for all class instances. We can define a
class attribute by assigning a value to a variable defined outside of .__init_()
example:
class Dog:
    species = "Canis familiaris"   --> CLASS ATTRIBUTE
    
    def __init__(self, name, age, coat_color):
        self.name = name  --> INSTANCE ATTRIBUTE
        self.age = age    --> INSTANCE ATTRIBUTE
        self.coat_color = coat_color	--> INSTANCE ATTRIBUTE

Class attributes are defined directly beneath the first line of the class name
and are indented by four spaces. They must always be assigned an INITIAL VALUE.
When an instance of the class is created, class attributes are automatically
created and assigned to their initial values.

We have to use CLASS ATTRIBUTES to define properties/variables that should have
the same value for every instance. Use INSTANCE ATTRIBUTES for
properties/variables that vary from one instance to another.

"""


class Cat:
    pass


# Every time tha we instantiate/create an object a new Memory Address is
# assigned to the instance/object and save in 'self' variable of the init():
a = Cat()
print(f"address of object 'a' is: {a}")
# address of object 'a' is: <__main__.Cat object at 0x000002BB4952BB50>
# or in IDLE:
# >>> a
# <__main__.Cat object at 0x000002BB4952BB50>

b = Cat()
print(f"address of object 'b' is: {b}")
# address of object 'b' is: <__main__.Cat object at 0x000002BB494C0CA0>
# >>> b
# <__main__.Cat object at 0x000002BB494C0CA0>

# >>> Cat()
# <__main__.Cat object at 0x000002BB494C0CD0>
# >>>


# Every new instance is located at a different memory address. That is because
# it is an entirely new instance and in completely unique from the first Cat
# object that have been instantiated:
a = Cat()
b = Cat()
print(f"a == b --> False = {a == b}")
print(f"a is b --> False = {a is b}")


class Dog:
    def __init__(self, name, age):
        print(f"self: {self}, name: {name} and age: {age}")
        self.name = name
        self.age = age


dog1 = Dog("Lolo", 23)
# instantiate Dog class and automatically the method
# __init__ is execute printing this:
# self: <__main__.Dog object at 0x000001FBBE2B53D0>, name: Lolo and age: 23
# self contains the memory address of the instance/object dog1, in this case:
# <__main__.Dog object at 0x000001FBBE2B53D0>
print(f"1- instance dog1's memory address --> {dog1} ")
# displayed --> <__main__.Dog object at 0x000001FBBE2B53D0>

dog2 = Dog("Ruby", 7)  # instantiate Dog class and automatically the method
# __init__ is execute printing this:
# self: <__main__.Dog object at 0x000001FBBE2FB430>, name: Ruby and age: 7
# self contains the memory address of the instance dog1, in this case:
# <__main__.Dog object at 0x000001FBBE2FB430>


dog1 = dog2  # Assign the same address of instance dog2 to dog1 therefore dog1
# and dog2 makes reference to the same memory location and same object instance
# this is why below print(dog1) display same 'self' addres for print(dog2):
print(f"1- instance dog2's memory address --> {dog2} ")
# displayed --> <__main__.Dog object at 0x000001FBBE2FB430>
print(f"2- instance dog1's memory address --> {dog1} ")
# displayed --> <__main__.Dog object at 0x000001FBBE2FB430>
print(
    f"After assigning object dog2 address to dog1 variable: dog1 == \
dog2? --> True = {dog1 == dog2}"
)
# And dog2.name displays the same content as dog1.name
print(f"dog2.name --> Ruby = {dog2.name}")
print(f"dog1.name --> Ruby = {dog1.name}")
# and"
print(f"dog1.age == dog2.age --> True = {dog1.age == dog2.age}")

dog1 = Dog("Lolo", 23)  # now instantiating object dog1, create a new memory
# addres for dog1, which is different from dog2 object.
# self: <__main__.Dog object at 0x000001FBBE2B53D0>, name: Lolo and age: 23
print(f"After instantiating dog1 then dog1 == dog2? --> False = {dog1 == dog2}")


print()
dog3 = Dog("Ruby", 7)  # instantiating an object dog3 with the same attributes
# than object dog2. This will create a new/different memory address and
# therefore a different object.
# dog3: self: <__main__.Dog object at 0x000001FBBE2FBAC0>, name: Ruby and age: 7
print(
    "just created a new object dog3 with the same attribute's value \
than object dog2"
)
print(f"dog2 == dog3 --> False = {dog2 == dog3}")

# dog3 and dog2 are different objects but their attribute have the same value
# and point to the same momory address, this is why:
# 1- dog2.name == dog3.name is True.
# 2- dog2.name is dog3.name is True.
# 3- id(dog2.name) == id(dog3.name) is True.
# 4- but when we change the value of dog3.name to 'Adolfo' then id(dog3.name)
#   change.
print(f"1- dog2.name == dog3.name --> True = {dog2.name == dog3.name}")
print(f"2- dog2.name is dog3.name --> True = {dog2.name is dog3.name}")
print(
    f"3- id(dog2.name) == id(dog3.name) --> True = \
{id(dog2.name) == id(dog3.name)}"
)
print(f"id(dog2.name)= {id(dog2.name)} and dog2.name --> {dog2.name}")
# 2180739206448
# id(dog2.name)= 1326658333424 and dog2.name --> Ruby
print(f"id(dog3.name)= {id(dog3.name)} and dog3.name --> {dog3.name}")
# 2180739206448
# id(dog3.name)= 1326658333424 and dog3.name --> Ruby
dog3.name = "Adolfo"  # Changing the name of dog3 to 'Adolfo' this now changes
# the id of dog3.name
print(
    f"After changed dog3.name then: id(dog3.name)= {id(dog3.name)} and \
dog3.name --> {dog3.name}"
)
print(
    f"After the change dog2 stay the same: id(dog2.name)= {id(dog2.name)} \
and dog2.name --> {dog2.name}"
)

# String Literal, like "Ruby", "Adolfo" are object and, at run time, Python
# load then at a memory address/location and assign this memory address to the
# field/object/variable that contains the String Literal. If a new variable/
# object contains the same String Literal then Python will assign the same
# address of the previous one, so they will have same id() and therefore will
# be consider as equal. this is explain what is happening above.
# Now if we change the dog3.name back to 'Ruby' then it will have the same id()
# and content thatn dog2.name, because they will have the same memory address.
dog3.name = "Ruby"
print(
    f"After dog3.name back to 'Ruby': id(dog3.name)= {id(dog3.name)} \
and dog3.name --> {dog3.name}"
)
print(f"id(dog2.name)--> {id(dog2.name)} and dog2.name --> {dog2.name}")

print(f"dog3.age == dog2.age? --> True = {dog3.age == dog2.age}")
print(f"dog3.age is dog2.age? --> True = {dog3.age is dog2.age}")
print(
    f"id(dog3.age) == id(dog2.age)? --> True = \
{id(dog3.age) == id(dog2.age)}"
)

# The above does also happen with primitive data type: int and booean:
print("\n*** integer ***")
one = 1
dos = 1
print(f"one == dos --> True = {one == dos}")
print(f"id(one): {id(one)}")
# 2700947908912
print(f"id(dos): {id(dos)}")
# 2700947908912
print(f"one is dos --> True = {one is dos}")
# Boolean:
print("\n*** boolean ***")
bool_1 = True
bool_2 = True
print(f"bool_1 is bool_2 --> True = {bool_1 is bool_2}")
print(f"id(bool_1): {id(bool_1)}")
# 140731473844328
print(f"id(bool_2): {id(bool_2)}")
# 140731473844328

# With float the memory address are equal and the content is the same:
print("\n*** float ***")
f_one = 1.255656
f_two = 1.255656
print(f"f_one: {f_one} and f_two: {f_two}")

print(f"f_one is f_two --> True = {f_one is f_two}")
print(f"id(f_one): {id(f_one)}")
print(f"id(f_two): {id(f_two)} \n")


# CLASS and INSTANCE attributes:
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):  # this will be executed when an object is created and\
        # its information is needed. Below is returned instead of the object
        # address: philo --> <__main__.Dog object at 0x000001F29941E070>
        # and print(philo) --> Philo is 5 years old.
        return f"{self.name} is a {self.age} years old dog."

    def speak(self, sound):
        return f"{self.name} says {sound}"


"""To instantiate an object of the above Dog class, we need to provide values
for the name, age and coat_color parameters in the .__init__() method. If we
dln't then Python raises a TypeError:
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Dog()
TypeError: __init__() missing 3 required positional arguments: 'name', 'age',
and 'coat_color'
This error also happens when we are instantiating an object of a CHILD class, we
have to provision values/arguments for the parameters defined in the .__init__()
method of the PARENT class. This is required to make sure that the CHILD object
has a PARENT created.

To pass arguments to the name, age and coat_color parameters, we put values
into parentheses afer the class name:
"""
philo = Dog("Philo", 5, "brown")
print(f"philo.name --> Philo = {philo.name}")
# 'Philo'
print(f"philo.age --> 5 = {philo.age}")

print(f"age: {philo.age}")
age: 5
print(f"{philo.name}'s coat is {philo.coat_color}.")
# Philo's coat is brown.

print(f"Who is philo? {philo}")
# Who is philo? Philo is a 5 years old dog.
print(philo.speak("hou hou hou"))
# Philo says hou hou hou

"""The Dog class's .__init__() method has four parameters, so why are only
three arguments passed to it in the above example? When we instantiate a Dog
object, Python creates a new instance/Memory address and passes it to the first
parameter of .__init__() (self). This essentially removes the need from us to
pass a value to the 'self' parameter, so we only need to worry about the
others parameters: name, age, coat_color.
Above we see tha after creating a Dog instance, we can access their instance
attributes using the 'dot notation': philo.name and philo.age, philo.coat_color
And we can access CLASS ATTRIBUTE also with dot.noataion:
"""
print(f"\nphilo.species is {philo.species}")
# philo.species is Canis familiaris


# Also:
# class Car:
class Car:
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles


car1 = Car("blue", 20000)
car2 = Car("red", 30000)
print(f"\n The {car1.color} has {car1.miles} miles.")
# the blue has 20000 miles.
print(f"The {car2.color} has {car2.miles} miles.")
# The red has 30000 miles.

"""One of the biggest advanages of using classes to organize data is that
instances are guaranteed to have the attributes we expect. All Dog instances
have .species, .name, .age and .coat_color attributes, so we can use those
attributes with confidence that they'll always return value.
Although the attributes are guaranteed to exist, their values can be changed
dinamically.
the key takeaway here is that custom objects are mutable by default:
"""
buddy_dog = Dog("Buddy", 9, "black")
dester = Dog("Dester", 10, "yellow")

buddy_dog.age = 6
dester.coat_color = "white and brown"
dester.species = "Felis silvestris"  # now dester is a cat.
print(f"\n new age for buddy_dog: buddy_dog.age --> {buddy_dog.age}")
# new age for buddy_dog: buddy_dog.age --> 6
print(f"new species for dester: dester.species --> {dester.species}")
# new species for dester: dester.species --> Felis silvestris


# Instance Methods:
"""Instance methods are functions that are defined inside a class and can only
be called from an instance/object of that class. Just like .__init__(), an
instance method's first parameter is always 'self'
(Note: 'self' is the Python convention; but
it can be any other variable name; but we need to keep in mind it to use it
accordingly, example:
class Cat:
    def __init__(obj_addr, name, color):
	obj_addr.name = name
	obj_addr.color = color

>>> faly = Cat("Fally", "green")
obj_addr --> <__main__.Cat object at 0x000002AD543DEE20>
>>>
)
"""


# now updating the Dog class:
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # instance method:
    def description(self):
        return f"{self.name} is a {self.age} years old dog."

    # another instance method:
    def speak(self, sound):
        return f"{self.name} says {sound}"


""" Above Dog class has two instance methods:
1- .description() returns a string displaying the name and age of the dog.
2- .speak() which has one parameter called 'sound' and returns a string
containing the dog's name and the sound it makes.

NOTE: The instance varibles created in .__init__() method are available to all
      the instance's methods by using 'self.instacne_var_name'. ie. self.age

"""
miles = Dog("Miles", 4, "green")
print(f"\n\n miles.description() --> {miles.description()}")
#  miles.description() --> Miles is a 4 years old dog.
print(f"miles.speak('Woof Woof') --> {miles.speak('Woof woof')}")
# miles.speak('Woof Woof') --> Miles says Woof woof
print(f"miles.speak('Bow Wow') --> {miles.speak('Bow wow')}")
# miles.speak('Bow Wow') --> Miles says Bow wow

""" In the above Dog class, .description() returns a string contaiing
information about the Dog instance miles. When writing my own classes, it is a
good idea to have a method that returns a string containing useful information
about an instance of the class. However, .description is not the most Pythonic
way of doing this. Because When we create a 'list' object, we can use print()
function to displays a string that looks like the list:
"""
names = ["David", "Dan", "Joanna", "Fletcher"]
print(names)
# ['David', 'Dan', 'Joanna', 'Fletcher']
# Let's see what happens when we print() the miles object:
print(miles)
# <__main__.Dog object at 0x00000221677FEEE0>
# When we print(miles), we get a cryptic looking message telling we that miles
# is a Dog object at the memory address 0x00000221677FEEE0. This message is not
# very helpful. We can change what we get printed by defining a special
# instance method called .__str__() as below:


# now updating the Dog class again to use __str__():
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # instance method:
    def __str__(self):  # this will be executed when an object is created and\
        # its information is needed. Belos is returned instead of the object
        # address: philo --> <__main__.Dog object at 0x000001F29941E070>
        # and print(philo) --> Philo is 5 years old.
        return f"\n {self.name} is a {self.coat_color} {self.age} years old dog."

    # another instance method:
    def speak(self, sound):
        return f"{self.name} says {sound}"


# Now to get a much friendlier output:
miles = Dog("Miles", 4, "brown")
print(f"print(miles) --> Miles is a brown 4 years old dog. = {miles} ")
# Miles is a brown 4 years old dog.

""" Methods like .__init__() and .__str__() are called 'dunder methods' because
they begin and end with double underscores. There are many dunder methods that
we can use to customize classes in Python. Although it is no advance a topic for
a beginning Python book, understanding dunder methods is an important part of
mastering OOP in Python.
"""


# Exercises:
class Car:
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

    def drive(self, new_miles):
        self.miles += new_miles


car3 = Car("green", 0)
car3.drive(100)
print(f"\n car3.miles --> {car3.miles}")
# 100

car2 = Car("red", 30000)
car2.drive(300)
print(f"car2.miles --> {car2.miles}")
# 30300
car2.drive(500)
print(f"car2.miles --> {car2.miles}")
# 30800


# Inherit From Other Classes
""" Inheritance is the process by which one class takes on the properties/
attributes and methods of another. Newly formed classes are called Child classes
and the classes that a child class is derived from are called parent classes.

Child classes can OVERRIDE or EXTEND the attributes and methods of parent
classes. In other words, child classes inherit all of the parent's attributes
and methods but can also specify attributes and methods that are unique to
themselves.

NOTE: To instantiate/create a CHILD class object, we HAVE TO PROVIDE all the
      attributes defined in the PARENT class's .__init__() method.

Although the analogy is not perfect, we can think of object inheritance sort of like
genetic inheritance. We may have inherited our hair color from the mother. it's
an attribute that I was born with. Let's say that I decide to color my hair
purple. Then I have just OVERRIDEN the hair color attribute from my mom.
I can also inherit, in a sense, my language from my parents. If my parent speak
English then I'll also speak English. Now imagine that I decide to learn a
second language, like Spanish. In this case I have EXTENDED my attributes because
I have added an attribute that my parent don't have.

Dog Park Example:
Pretend for a moment that you are at a dog park. There are many dogs of
different breeds at the park, all engaging in vaious dog behaviors.

Suppose now that you want to model the dog park with Python classes. Now let
add the .breed attribute to the previous Dog class:
"""


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

        # instance method:

    def __str__(self):  # this will be executed when an object is created and\
        # its information is needed. Belos is returned instead of the object
        # address: philo --> <__main__.Dog object at 0x000001F29941E070>
        # and print(philo) --> Philo is 5 years old.
        return f"\n {self.name} is a {self.breed} {self.age} years old dog."

    # another instance method:
    def speak(self, sound):
        return f"{self.name} says {sound}"


# Now you can model the dog park by instantiating a bunch of differnt dogs as
# follow:
miles = Dog("Miles", 4, "Jack Russel Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

# Each breed of dog has slightly different behavior, For example, bulldogs
# have a low bark that sounds like 'woof', but dachshunds have a higher-pitched
# bark that sounds more like 'yap'
# Using just the Dog class, you must supply a string for the 'sound' argument
# of the .speak() method every time you call it on a Dog instance:
print(f"buddy.speak('Yap') --> {buddy.speak('Yap')}")
print(f"jim.speak('Woof') --> {jim.speak('Woof')}")
print(f"jack.speak('Woof') --> {jack.speak('Woof')}")

# Passing a string to every call to .speak() is repetitive and inconvinient.
# Moreover, the string representing the sound that each Dog instance makes
# should be determine by its .breed attribute, but here you have to manually
# pass the correct string to .speak() method every time it is called.
# You can simplify the experience of working with the Dog class by creating a
# child class for each breed of dog. This allow you to EXTEND the functionality
# that each chld class inherits, including specifying a default argument for the
# .speak() method.


# Parent Classes vs Child classes:
# Using the modified Dog class (removing the breed attribute), Let's create a
# child class for each of the three breeds mentioned above: Jack Russel
# Terrier, Dachshund, and Bulldog.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # instance method:

    def __str__(self):  # this will be executed when an object is created and\
        # its information is needed. Belos is returned instead of the object
        # address: philo --> <__main__.Dog object at 0x000001F29941E070>
        # and print(philo) --> Philo is 5 years old.
        return f"{self.name} is a {self.age} years old dog."

    # another instance method:
    def speak(self, sound):
        return f"{self.name} says {sound}"


# To create a child class, you create a new class with its own name and then put
# the name of the parent class in parentheses, like this:
class JackRusselTerrier(Dog):
    pass


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


# With the child classes defined/created, you can now instantiate some dogs of
# specific breeds:
miles = JackRusselTerrier("Miller", 4)  # The child class does not have
# parameters but the parent does (name, age) therefore, we need to provide them
# when instantiating an object of the child class. These parameters (name, age)
# are the ones that define a Dog in the .__init__() method, this is why we need
# then when instantiating a object in a child class.
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# Instances of child classes inherit all of the attributes and methods of the
# parent class:
print(f"\n miles.species --> {miles.species}")
#  miles.species --> Canis familiaris
print(f"buddy.name --> {buddy.name}")
# buddy.name --> Buddy
print(f"jack --> {jack}")
# jack --> Jack is a 3 years old dog.
print(f"jim.speak('Woof woof') --> {jim.speak('Woof woof')}")
# jim.speak('Woof woof') --> Jim says Woof woof

# You can see which class an object belongs to using the buit-in type() function
print(f"\ngetting the class of miles object with type(miles) --> {type(miles)}")
# getting the class ...with type(miles) --> <class '__main__.JackRusselTerrier'>

# What if we want to determine if 'miles' is also an instance of the Dog class?
# You can do this using the built-in fucntion isinstance():
print(f"isinstance(miles, Dog) --> True = {isinstance(miles, Dog)}")
# isinstance(miles, Dog) --> True
# isinstance() takes two arguments, an object and a class and return True/False.
print(
    f"isinstance(miles, JackRusselTerrier) --> True == \
{isinstance(miles, JackRusselTerrier)}"
)
# isinstance(miles, JackRusselTerrier) --> True == True
print(f"isinstance(miles, Bulldog) --> False = {isinstance(miles, Bulldog)}")
# isinstance(miles, Bulldog) --> False = False

# The miles, buddy, jack, and jim objects are all Dogs instances, but miles is
# not a Bulldog instance, and jack is not a dachshund instance.

# More generally, all objects created from a child class are instances of the
# parent class, although they may NOT be instances of other child class.

# Now that you've created child classes for some different breeds of dogs, let's
# give each breed its own sound. for this we have to EXTEND the parent class.

# Extend the Functionality of a Parent Class:
""" Since different breeds of dogs have slightly different barks, you want to
provide a default value for the 'sound' argument/parameter of their respective
.speak() methods. To do this, you need to OVERRIDE the .speak() method (defined
in Dog class) in each one of the definition of the child classes for each breed:
"""


class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    def speak(self, sound="Grrrummmp"):
        return f"{self.name} says {sound}"


# Now the .speak() method is defined/overriden on each child class and EXTENDED
# with a default argument/value for 'sound' parameter set to "Arf", "Grrrummmp".

# Now we can call the .speak() method from objects/instance of each child class
# without passing an argument/value to the 'sound' parameter and the default
# will be used; because we have OVERRIDEN and EXTENDED the .speak() method
# behavior:
miles = JackRusselTerrier("Miles", 4)
print(f"\n Default bark of: miles.speak() --> {miles.speak()}")
#  Default bark of: miles.speak() --> Miles says Arf
buddy = Bulldog("Buddy", 6)
print(f"Default bark of: buddy.speak() --> {buddy.speak()}")
# Default bark of: buddy.speak() --> Buddy says Grrrummmp

# Sometimes dogs make different barks, so if Buddy gets smooth we can still
# call the .speak() method with different sound like Miauuu:
print(f" barking Miauuu: buddy.speak('Miauuu') --> {buddy.speak('Miauu')}")
# barking Miauuu: buddy.speak('Miauuu') --> Buddy says Miauu


# One thing to keep in mind about class inheritance is that changes to the
# parent class automatically propagate to the child classes. This occurs as long
# as the attribute or method being changed is NOT OVERRIDEN in the child class.
# for example, if we change the string returned by the .speak() method in the
# Dog class to 'barks' instead of 'says'
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # instance method:

    def __str__(self):  # this will be executed when an object is created and\
        # its information is needed. Belos is returned instead of the object
        # address: philo --> <__main__.Dog object at 0x000001F29941E070>
        # and print(philo) --> Philo is 5 years old.
        return f"{self.name} is a {self.age} years old dog."

    # another instance method:
    def speak(self, sound):
        return f"{self.name} barks {sound}"


# Child classes
class JackRusselTerrier(Dog):  # OVERRIDING the .speak()
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Bulldog(Dog):  # OVERRIDING the .speak()
    def speak(self, sound="Grrrummmp"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):  # NOT OVERRIDING the .speak(), stays as in Dog.
    pass


# Now when you create a new Dachshund instance named jim, then jim.speak() will
# return the new string 'barks' instead of 'says':
jim = Dachshund("Jim", 10)
print(f"\n Now jim barks: jim.speak('Woooff') --> {jim.speak('Wooof')}")
# Now jim barks: jim.speak('Woooff') --> Jim barks Wooof

# However, calling .speak() method on the other child instances will NOT shows
# the new string 'barks' because both of then OVERRIDE the .speak() method:
miles = JackRusselTerrier("Miles", 4)
print(f"miles still 'says': miles.speak() --> {miles.speak()}")
# miles still 'says': miles.speak() --> Miles says Arf
buddy = Bulldog("Buddy", 33)
print(f"buddy still 'says': buddy.speak('Graaon') --> {buddy.speak('Graaon')}")
# buddy still 'says': buddy.speak('Graaon') --> Buddy says Graaon


""" Sometimes it makes sense to completely OVERRIDE a method from a parent class,
like we did above with JackRusselTerrier and Bulldog child classes. But assuming
that we don't want a child class to lose any changes that might be made to the
parent class (In this case the string in Dog.speak() method). Then to have this,
you still need to define a .speak() method on the child class JackRusselTerrier
child class, But instead of explicitly defining the output string:
   ({self.name} barks {sound}), you need to call the parent/Dog's class .speak()
method inside the child class's .speak() method using the same arguments that
you passed to the JackRusselTerrier.speak() method.
You can access the parent class's method from inside a method of a child class
by using the super():
"""


class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)  # call the .speak() in the parent class.


# When you call super().speak(sound) inside the child class JackRusselTerrier,
# Python searches the parent class, Dog, for a .speak() method and calls it
# with the variable 'sound'.

# Now save this program and run it again, and instantiate miles dog again:
miles = JackRusselTerrier("Miles", 4)
print(
    f"Now child class instance -miles- uses the parent class .speak() when:\
 miles.speak() --> {miles.speak()}"
)
# Now miles.speak(), displays the output reflecting the new formatting in the
# Dog class with the default value in child class for 'sound' argument, this is:
# Now child class instance -miles- uses the parent class .speak() when: \
# miles.speak() --> Miles barks Arf


""" In the above example, the class hierarchy is very simple: the
JackRusselTerrier chld class has a single parent class, Dog. In real world
example, the class hierarchy can get quite complicated. The super(). does much
more than just search the parent class for a method or an attribute. It
traverses the entire class hierarchy for a matching method or attribute. If you
are not careful, super(). can have surprising results
"""


# Exercises:
# 1:
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"


# 2:
class Rectangle:
    def __init__(self, length, width=0):
        self.length = length
        self.width = width or length
        print(f"\n self.length: {self.length} and self.width: {self.width}")

    def area(self):
        return self.length * self.width


class Square(Rectangle):  # child class from Rectangle
    def __init__(self, side_length):  # receive one parameter.
        super().__init__(side_length, side_length)  # calls the .__init__()
        # method of the PARENT class with the received parameter as the two
        # arguments needed by the parent's .__init_() method.


square_1 = Square(4)  # instantiate the square_1 object from child class.
# NOTE: The child class's .__init__() method only uses
# one parameter; but the parent's class one uses two
# parameters, therefore the child class instaniating needs
# to provide two, but only is provisioning one, this is
# why in the child class's .__init__() the first statement
# is to call the parent class's .__init__() with two
# parameters: super().__init__(side_length, side_length)
# to avoid the error.
print(f"square_1.area() is --> 16 {square_1.area()} ")

square_1.width = 5  # Now assign a value 5 to the inherited 'width' attribute,
# So that we can calculate the area again as 4 * 5 = 20
print(
    f"New area with a 'width' value 5: square_1.area() --> 20 = \
{square_1.area()}"
)


# Challenge 10.4: Model A Farm
class Animal_1:
    def __init__(self, name, domestic, animal_type, weight):
        self.name = name
        self.domestic = domestic
        self.animal_type = animal_type
        self.weight = weight

    def __str__(self):
        return f"{self.name} {'is a ' if self.domestic else 'is not a '}\
domestic animal, belongs to the {self.animal_type} family and weights \
{self.weight} pounds"

    def drink_water(self, number_glass):
        return f"{self.name} is drinking {number_glass} glass of water"

    def sleeping(self, number_hours):
        return f"{self.name} is sleeping for {number_hours} hours"


class Pig(Animal_1):
    area_needed = 20
    temper = "Good"
    amount_of_food_eaten = 10


class Cow(Animal_1):
    average_grass_eaten = 25
    average_milk_bottles = 40

    def produce_milk(self, amount_to_produce):
        return f"{self.name} is producing {amount_to_produce} and still can \
produce {Cow.average_milk_bottles - amount_to_produce} bottles"

    def eat_grass(self, grass_amount):
        if Cow.average_grass_eaten > grass_amount:
            return f"{self.name} can eat more grass"
        else:
            return f"{self.name} DO NOT NEED TO EAT MORE"


class Goat(Animal_1):
    average_grass_eaten = 12
    average_milk_bottles = 125

    def produce_milk(self, amount_to_produce):
        return f"{self.name} is producing {amount_to_produce} and still can \
produce {Goat.average_milk_bottles - amount_to_produce} bottles"

    def eat_grass(self, grass_amount):
        if Goat.average_grass_eaten > grass_amount:
            return f"{self.name} can eat more grass"
        else:
            return f"{self.name} DO NOT NEED TO EAT MORE"


class Donkey(Animal_1):
    travel_distance = 105
    maximum_load = 45
    average_grass_eaten = 125

    def transport_product(self, weight):
        if weight > Donkey.maximum_load:
            return "{weight} pounds is {weight - Donkey.maximum_load} heavier for \
{self.name} to transport"
        else:
            return f"{self.name} can transport {Donkey.maximum_load - weight} more \
pounds."


print("\n\n")
molly_cow = Cow("Molly Cow", False, "Cow", 350)
print(molly_cow)
print("*** PARENT properties: ***")
print(
    f"molly_cow.name --> {molly_cow.name}, molly_cow.animal_type --> \
{molly_cow.animal_type}"
)
print(
    f"{molly_cow.name} weight {molly_cow.weight} pounds, \
{'is' if molly_cow.domestic else 'is not'} a domestic animal"
)

print("*** PARENT Methods: ***")
print(molly_cow.sleeping(9))
print(molly_cow.drink_water(3))

print("-- Child methods and variables:")
print(molly_cow.eat_grass(5))
print(f"molly_cow.average_grass_eaten --> {molly_cow.average_grass_eaten}")
print(molly_cow.produce_milk(300))
print(f"molly_cow.average_milk_bottles --> {molly_cow.average_milk_bottles}")


print("\n\n")
lulo = Donkey("Lulo", False, "Donkey", 212)
print(lulo)
print("*** PARENT properties: ***")
print(f"lulo.name --> {lulo.name}, lulo.animal_type --> {lulo.animal_type}")
print(f"lulo.weight --> {lulo.weight}, lulo.domestic --> {lulo.domestic} ")

print("*** PARENT Methods: ***")
print(lulo.drink_water(4))
print(lulo.sleeping(5))

print("-- Child methods and variables:")
print(lulo.transport_product(40))
print(f"lulo.average_grass_eaten --> {lulo.average_grass_eaten}")
print(f"lulo.travel_distance --> {lulo.travel_distance}")
print(f"lulo.maximum_load --> {lulo.maximum_load}")


print("\n\n")
aurelio = Donkey("Aurelio", True, "Donkey", 114)
print(aurelio)
print(f"{aurelio.name} can travels {aurelio.travel_distance} miles")

print("\n\n")
porcina = Pig("Porcina", True, "Pig", 65)
print(porcina)
print("*** PARENT properties: ***")
print(
    f"porcina.name --> {porcina.name}, porcina.animal_type --> \
{porcina.animal_type }"
)
print(
    f"porcina.domestic --> {porcina.domestic}, porcina.weight --> \
porcina.weight"
)

print("*** PARENT Methods: ***")
print(porcina.drink_water(6))
print(porcina.sleeping(3))

print("-- Pig DOES NOT Child methods:")

print("-- Child methods and variables:")
print(f"porcina.amount_of_food_eaten --> {porcina.amount_of_food_eaten}")
print(
    f"porcina.area_needed --> {porcina.area_needed}, porcina.temper --> \
{porcina.temper}"
)


# Challenge 10.4: Model A Farm --> SOLUTION FROM BOOK:
# Parent class:
class Animal:
    # Class attributes:
    stuff_in_belly = 0
    position = 0

    # Initializer:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Object description __str__()
    def __str__(self):
        return f"{self.name} has a color {self.color}"

    # Instance methods:
    def talk(self, sound=None):
        """Return the string "<name> says <sound>"
        if 'sound' is left out, returns "Hello, I'am <name>"
        """
        if sound is None:
            return f"Hello, I'am {self.name}!"
        return f"{self.name} says {sound}"

    def walk(self, walk_increment):
        self.position += walk_increment
        return self.position

    def run(self, run_increment):
        self.position += run_increment
        return self.position

    def feed(self):
        self.stuff_in_belly += 1
        if self.stuff_in_belly > 3:
            return self.poop()
        else:
            return f"{self.name} is eating."

    def is_hungry(self):
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry."
        else:
            return f"{self.name} is not hungry."

    def poop(self):
        self.stuff_in_belly = 0
        return f"Ate too much... {self.name} is running to the restroom."


# Child classes:
class Dog(Animal):
    # Instance methods:
    def talk(self, sound="Bark Bark!!"):  # OVERRIDE talk() in PARENT and
        # EXTEND it with a default sound.
        return super().talk(sound)  # super() uses the same code in PARENT.

    def fetch(self):
        return f"{self.name} is fetching..."


class Sheep(Animal):
    # Instance method:
    def talk(self, sound="Baaa Baaa"):
        return super().talk(sound)


class Pig(Animal):
    # Instance method:
    def talk(self, sound="Oink Oink"):
        return super().talk(sound)


# the folling code illustrate how to use the classes defined above. It is not
# necesarrily a part of the solution, and is included for illustration
# purposes only:

# Create a dog.
dog = Dog("Blitzer", "yellow")
print(f"\n\n dog instance --> {dog}")


# Output the dog's attributes:
print(f"Our dog's name is {dog.name}.")
print(f"And he's {dog.color}")

# Output some behavior:
print("Some dog's behavior...")
print(f"Say something, {dog.name}")
print(dog.talk())
print(f"and now again, {dog.talk('Grrrrouoooummp')}")
print(f"Go fetch! {dog.fetch()}")

# Walk the dog:
print(f"\n Walking {dog.name} is at position {dog.walk(2)}.")

# Run the dog:
print(f"Running {dog.name} is at position {dog.run(4)}.")

# Feed the dog:
print(dog.feed())

# Is the dog hungry?
print(dog.is_hungry())

# Feed the dog more...
print(dog.feed())
print(dog.feed())

# Is still hungry?
print(dog.is_hungry())
print(dog.feed())
print(dog.feed())

print("\n")
# create a sheep:
sheep = Sheep("Shaun", "white")
print(f"Tell me about this sheep? {sheep}")

# the sheep talks!!!
print(sheep.talk())

# When the sheep runs, the distance is returned:
print(f"{sheep.name} is running {sheep.run(102)} miles")
print(f" continue running {sheep.run(20)} more.")
print(f"Now {sheep.name} is walking {sheep.walk(2)}")


print("\n")
# Create a pig:
pig = Pig("Carl", "pink")

print(f"Tell me about this pig? {pig}")
# Pigs love to oink!!
print(pig.talk())
