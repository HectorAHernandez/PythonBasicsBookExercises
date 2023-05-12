# Files and the File System:
""" The File System organize files in a hierarchy of DIRECTORIES, which are also
called FOLDERS. At the top of the hierarchy is a directory called the ROOT
DIRECTORY. All other files and directories in the files system aare contained in
the ROOT DIRECTORY.
IMPORTANT:
On Windows, every disk drive has its own file hierarchy with the root directory
represented by the filename.
macOS and Linux are different in that each drive is represented as a
subdirectory of a single root directory.

Every file has a filename that must be unique from any other file in the same
directory. Directories can also contain other directories called subdirectories
or subfolder.
"""

# File Paths:
# To locate a file in a file system, you can list the directories in order,
# starting with the root directory, followed by the name of the file and
# extension
# A File Path is a STRING with the location represented by a string indicating
# the directories and the file name.
# Example: root/photos/dogs/jack_russel.png

# How we write file paths depends on your computer operating system:
# 1- Windows: "C:\Users\ssshh\Documents\hello.txt"
# 2- macOS: "/Users/ssshh/Documents/hello.txt"
# 3- Ubuntu "Linux: /home/ssshh/Documents/hello.txt"

# On macOS and Ubuntu Linux, the operating system uses a Virtual File System
# that organizes all files and directories for all devices on the system under
# a single root directory, usually represented by a forward slash (/) symbol.
# Files and folder for external devices are usually located in a subdirectory
# called media/.

# On Windows, there is no universal root directory. Each device (drive) has a
# separate file system with a unique root directory that is named with a drive
# letter followed by a colon (:) and a back slash (\).
# Tipically, the hard drive on which the operating system is installed is
# assigned the letter C, so the root directory of the file system for that
# drive is C:.

# Windows directories are separated by back slash (\\).
# masOS and Ubuntu directoies are separated by forward slash (/).

# When you write programs that need to run on multiple operating systmes, it is
# critical that you handle the differences in the file paths appropiately. In
# versions of Python greater than 3.4, the Standard Library contains a MODULE
# called "pathlib" that helps take the pain out of handling file paths across
# operating systems.
# This "pathlib" module contains classes (like Path) which contains methods (like
# .home(), .cwd(), .is_absolut(), .mkdir(). """

# Working with File Paths in Python:
""" Python's 'pathlib' module is the main interface for working with file paths.
You will have to import the module before you can do anything with it:
"""
import pathlib

# The pathlib module contains a class called 'Path' that is used to represent
# a file path.

# Creating Path Objects:
""" There are several ways to create a new Path object:
1- From a string.
2- With the Path.home() and Path.cwd() methods of the Path class.
3- With the / operator.
The mosst straightforward way to create a Path object is from a string.
"""

# Creating Path Object From Strings:
# the following command creates a Path object representing the macOS file path
# "/Users/ssshh/Documents/hello.txt"
#        path = pathlib.Path("/Users/ssshh/Documents/hello.txt")

# There's a problem, though, with Windows paths. On Windows, directories are
# separaed by backslahses (\). Python interprets backslashes as the start of an
# ESCAPE SEQUENCE that represents a special character in the string, such as the
# newline (\n).
# Attempting to create a Path object with the Windows file path:
# "C:\Users\ssshh\Documents\hello.txt" raises an exception:
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in
# position 2-3: truncated \UXXXXXXXX escape

# path = pathlib.Path("C:\Users\ssshh\Documents\hello.txt")

# There are two ways to get around this problem. First, you can use the
# forward slash (/) instead of bakcslash (\) in your Windows file paths:
path = pathlib.Path("C:/Users/ssshh/Documents/hello.txt")

# Python can interpret this just fine and will translate the path appropiately
# and automatically  when interfacing with the Windows operating system.
# Second, you can turn the string  into a 'raw' string by prefixing it with
# an 'r':
path = pathlib.Path(r"Users\ssshh\Documents\hello.txt")

# This 'raw' tells Python to ignore any escape sequences and just read the
# string as is.


# Using Path.home() and Path.cwd() to create Path Objects:
"""Beside creating a Path object from a string, the Path class has class methods
that return the class object of special directories in your file system. Two of
the most useful class methods are Path.home() and Path.cwd().

Every operating system has a special directory for storing data for the
currently logged-in user. This directory is called the user's HOME DIRECTORY.
The location of this directory depends on the opeating system:
1- Windows: C:\\Users\\<username>
2- macOS: /Users/<username>
3- Ubuntu Linux: /home/<username>

The Path.home() class method creates a Path object representing the home
directory regarless of which operating system the code runs on:
"""
home = pathlib.Path.home()

# WHEN USING THE REPL to inspect the 'home' variable on Windows, you will see
# something like:
# >>> home
# WindowsPath('C:/Users/ssshh')
# The Path oject created is a subclass of Path called WindowsPath. On other
# operaating systems, the Path object returned is a subclass called PosixPath.
# For example, on macOS, inspecting 'home' variable will displays:
# >>> home
# PosixPath("/Users/ssshh")

""" For the rest of this section, WindowsPath objects will be shown in the
example output. However, all of the examples will work with PosixPath objects.
Notes: WindowsPath and PosixPath objects share the same methods and attributes.
From a programming standpoint, there is no difference between the two types of
Path objects.
"""
# but if I print the content of 'home' then only the directory is displayed
print(f"home = pathlib.Path.home() Then home --> {home}")
# C:\Users\ssshh

home_str = str(home)  # move the string representation of the Path object
print(f"home_str --> {home_str}")
# --> home_str --> C:\Users\ssshh


""" The Path.cwd() class method returns a Path object representing the CURRENT
WORKING DIRECTORY, or CWD. The current working directory is a dynamic reference
to a directory that depends on where a process/program on the computer is
currently working/running. Path.cwd() always represents your current location in
the file system.
When you run IDLE, the current working directory is usually set to the
'Documents' directory in the current users's home directory:
>>> pathlib.Path.cwd()
WindowsPath(C:/Users/ssshh/Documents)

This is not always the case, thought.
In my case, I am receiving the directory where Python executable is located:
WindowsPath('C:/Users/ssshh/AppData/Local/Programs/Python/Python39')
Moreover, the cwd may change during the lifetime of a program.

Path.cwd() is useful, but be careful when you use it. When you do, make sure you
know exactly which directory the cwd referst to.
"""

# Using the / Operator to create Path objects:
""" If you have an existing Path object, then you can use the / operator to
extend the path with subdirectories or filename.
For example, the following creates a Path object representing a file named
hello.txt in the 'Desktop' subdirectory of the current user's home directory:
"""
home = pathlib.Path.home()
file_path = home / "Desktop" / "hello.txt"
print(f"file_path --> {file_path}")
# --> C:\Users\ssshh\Desktop\hello.txt

"""The / operator must always have a Path object on the left-hand side. The
right-hand side can have a string representing a single file or directory, or
it can have a string representing a path or other Path object"""


# Absolute vs Relative Paths:
"""A path that begins with the root directory in a file system is called an
absolute file path. Not all of the paths are absolute. A file path that is not
absolute is called Relative file path.
Here's an example of a Path object that references a relative path:
"""
rel_path = pathlib.Path("Photos/image.jpg")
# Notice that the path string does not start with C:\ or /.
# You can determine if a file path is absolute using the .is_absolute() class
# method:
print(f"rel_path.is_absolute() ? --> {rel_path.is_absolute()}")
# rel_path.is_absolute() ? --> False

"""Relative paths only make sense when considered within the context of some
other directory. They are perhaps most commonly used to describe the path to a
file relative to the current working directory -Path.cwd()- or the user's
home directory - Path.home()-
"""

# You can extend a relative path to an absolute path using the forward slash /
# operator:
home = pathlib.Path.home()
photo_path = home / pathlib.Path("Photos/image.png")
print(f"The extended Photo path: photo_path --> {photo_path}")
# The extended Photo path: photo_path --> C:\Users\ssshh\Photos\image.png

# You will not always know how to construct an absolute file path, though. In
# those cases, you can use .resolve() Path's class method.
# When you call the .resolve() on an existing Path object, a new Path object
# representing the absolute path is returned:
relative_path = pathlib.Path("/Users/ssshh")  # The first / is needed, if not
# the .resolve() won't add the C: to make it absolute.
absolute_path = relative_path.resolve()  # this add the C: to make it absolute
# >>> absolute_path
# WindowsPath('C:/Users/ssshh')
print(absolute_path)
# C:\Users\ssshh
# Path.resolve() attempts to create as much of the absolute path as possible.
# Sometimes the relative path is ambigous. In that case, .resolve() returns
# the relative path. In other words, .resolve() isn't guaranteed to return an
# absolute path, like above if missing the first / in the relative path.

# Once you create a Path object, yo can inspect the various components of the
# file path that it refers to.


# Accessing File Path Components:
""" All file paths object contain a list of directories. The .parents attribute
of a Path object returns an iterable containing a list of directories objects in
the file path:
"""
path = pathlib.Path.home() / "hello.txt"
# >>> path
# WindowsPath('C:/Users/ssshh/hello.txt')
print(f"path --> {path}")  # The print() convert the object and displays strings
# path --> C:\Users\ssshh\hello.txt
print("path =", path)  # The print() convert the object and displays strings
# path = C:\Users\ssshh\hello.txt
print(f"type(path) --> {type(path)} \n")


print(f"list(path.parents) --> {list(path.parents)}")
# list(path.parents) --> [WindowsPath('C:/Users/ssshh'),
#                             WindowsPath('C:/Users'), WindowsPath('C:/')]
# >>> list(path.parents)
# [WindowsPath('C:/Users/ssshh'), WindowsPath('C:/Users'), WindowsPath('C:/')]


""" Notice that the directory objects are returned in the reverse order of how
they appear in the file path. That is, the last directory in the path is the
first directory object in the list of parent directories objects.

You can iterate over the parents directories in a for loop:
"""
for directory in path.parents:
    print(f"directory --> {directory}")
    print(f"type(directory) --> {type(directory)}")

# directory --> C:\Users\ssshh
# type(directory) --> <class 'pathlib.WindowsPath'>
# directory --> C:\Users
# type(directory) --> <class 'pathlib.WindowsPath'>
# directory --> C:\
# type(directory) --> <class 'pathlib.WindowsPath'>


# the .parent attribute returns the object of the first parent directory object
# in the list:
print(f"\n path.parent --> {path.parent}")  # --> C:\Users\ssshh
# path.parent --> C:\Users\ssshh
# >>> path.parent   # in the IDLE returns the path object
# WindowsPath('C:/Users/ssshh')

# .parent attribute is a shortcut for .parents[0]
print(f"path.parents[0] --> {path.parents[0]}")
# path.parents[0] --> C:\Users\ssshh
# or:
print(
    f"path.parent == path.parents[0] --> True = \
{path.parent == path.parents[0]}"
)


# If the path is absolue (path.is_absolute() == True), then you can access the
# root directory of the file path with the .anchor attribute:
if path.is_absolute():
    print(path.anchor)
# --> C:\
# >>> path.anchor
# 'C:\\'

# Note that .anchor attribuete returns a string, not another Path object.
# For relative paths, .anchor returns an empty string: ""
path = pathlib.Path("hello.txt")
print(f"\n path.anchor --> '' = {path.anchor}")


# The .name attribute returns the name of the file or the directory that the
# path points to:
home = pathlib.Path.home()
print(f"\n home.name --> ssshh = {home.name}")

home2 = home / "text2.txt"
print(f"home2.name --> text2.txt = {home2.name}")

file1 = pathlib.Path("text3.txt")
print(f"file1.name --> text3.txt = {file1.name}")


# File name: path.stem and path.suffix attributes:
""" File names are broken down into two parts. the part to the left of the dot
(.) is called the stem, and the part starting with the dot is called suffix or
the file extension (including the dot (.)).
The .stem and .suffix attributes returns strings containing each of these parts
of the file name:
"""
sale_file = pathlib.Path.home() / "Nov_sales.CVS"
print(
    f"\n\n for file name: Nov_sales.CVS, sale_file.stem --> Nov_sales = \
{sale_file.stem}"
)
print(
    f"for file name: Nov_sales.CVS, sale_file.suffix --> .CVS = \
{sale_file.suffix}"
)  # including the dot (.) .CVS


# Checking Whether a File Path Exists:
"""You can create a Path object for a file path even if that path doesn't
actually exist. Of course, file paths that don't represent actual files or
directories aren't very useful unless you plan on creating them at some point.

Path objects have an .exists() method that returns True of False depending on
whether or not the file path exists on the machine executing the program.
For instance, if you don't have a "hello.txt file in your home directory, then
calling .exists() on the Path object representing that file path returns False:
"""
hello_path = pathlib.Path.home() / "hello.txt"
print(f"\n hello_path.exists() --> False = {hello_path.exists()}")

# Checking if a file path refers to a file or a directory.
# to check if the file path is a file, use the .is_file() method:
print(f"\n hello_path.is_file() --> True = {hello_path.is_file()}")
print(f"hello_path.name --> hello.txt {hello_path.name}")

# Note that .is_file() method returns False if the file does NOT exist.


# to check if a file path is for a directory, use the .is_dir() method:
# example, hello_path is not for a directory
print(f"\n hello_path.is_dir() ==> False = {hello_path.is_dir()}")

# home is a file path for a directory
print(f"home.is_dir() --> True = {home.is_dir()}")


""" Working with file paths is an essential part of any programming project that
reads or writes data from a hard drive or other storage device. Understanding
the differences  between file paths on different operationg systems and how to
work with pathlib.Path objects so that your programs can work on any operating
system is an important and useful skill.
"""
# Review exercise:
# 1:
file_path = pathlib.Path.home() / "my_folder" / "my_file.txt"
print(f"\n\nfile_path --> {file_path}")
# file_path --> C:\Users\ssshh\my_folder\my_file.txt


# 2: Check whether the path assigned to file_path exists:
print(f"file_path.exists() --> False = {file_path.exists()}")

# 3: Print the name of the path assigned to file_path. the output should be
#    my_file.txt
print(f"file_path.name --> my_file.txt = {file_path.name}")
# file_path.name --> my_file.txt = my_file.txt

# 4: print the name of the parent directory of the path assigned to file_path.
#    The output should be my_folder:
print(f"file_path.parent.name --> my_folder = {file_path.parent.name}")
# file_path.parent.name --> my_folder = my_folder

# 5: print the parent directory of the path assigned to file_path.
#    The output should be C:\Users\ssshh\my_folder:
print(f"file_path.parent --> C:\my_folder = {file_path.parent}")
# file_path.parent --> C:\my_folder = C:\Users\ssshh\my_folder


# Common File System Operations:
# Creating a Directory and files:
# to create a directory, use the Path.mkdir() method.
import pathlib

new_dir = pathlib.Path.home() / "new_directory"
# new_dir.mkdir()  # physically create the directory in the file system.

# you can check that the new directory exists and is, in fact, a directory:
print(f"\n\n new_dir.exists() --> True = {new_dir.exists()}")
print(f"new_dir.is_dir() --> True = {new_dir.is_dir()}")

# if yo try to create a directory that already exist, then you get an error:
# new_dir.mkdir()
"""Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    new_dir.mkdir()
  File "C:/Users/ssshh/AppData/Local/Programs/Python/Python39/lib/pathlib.py", line 1313, in mkdir
    self._accessor.mkdir(self, mode)
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\ssshh\\new_directory'
>>>"""
# What if you want to create a new directory only if it does not already exist,
# and you also want to avoid raising the FileExistsError if the directory
# does exist?
# In that case, you can set the 'exist_ok' parameter of .mkdir() to True:
new_dir.mkdir(exist_ok=True)

""" When you execute .mkdir(exist_ok=True) with the exist_ok parameter set to
True, the directory is created only if it doesn't exist. If it does already
exist, then nothing happen. This is, no FileExistError is raised.
The above setting is equivalent to this code:
if not new_dir.exists():
    new_dir.mkdir()

Although the above code works just fine, setting the exist_ok parameter to True
is shorter and doesn't sacrifice readability.
"""

# Now let's see what happens if you try to create a subdirectory within a
# directory that does not exist:
nested_dir = new_dir / "folder_a" / "folder_b"
# -->  nested_dir.mkdir()
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     nested_dir.mkdir()
#   File "C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\pathlib.py",
#   line 1313, in mkdir
#    self._accessor.mkdir(self, mode)
# FileNotFoundError: [WinError 3] The system cannot find the path specified:
#                'C:\\Users\\ssshh\\new_directory\\folder_a\\folder_b'

"""The problem is that the parent directory folder_a/ does not exist.
Typically, to create a directory, all of the parent directories of the target
directory (in this case folder_b/) in the path must already exist.

To create any parent directories needed to create the target directory, set the
optional 'parents' parameter of .mkdir() to True
"""
# now:
# -->  nested_dir.mkdir(parents=True)
# Now .mkdir() method creates the parent directory, folder_a/, so that the
# target directory, folder_b/ can be created.

# Putting all this together, you get the following common pattern for creating
# directories:
#        path.mkdir(exist_ok=True, parents=True)
nested_dir.mkdir(exist_ok=True, parents=True)
""" When you set both the parents and exist_ok parameters to True, the entire
path is created if needed, and no exception is raised if the path already exist.

This pattern is useful, but it may not be the right approach in every situation
For example, if a use inputs a nonexisting path, the you may wish to instead
catch an exception so you can ask the user to verify the path that they entered.
They might have just mistyped the name of an existing directory!
"""

# Creating file using the Path.touch() method:
# Now let's look at how to create files. Create a new path object called
# file_path for the path new_directory/file1.txt
file_path = new_dir / "file1.txt"
print(f"\n file_path.exists() --> False = {file_path.exists()}")
# You can create the physical file in the directory by using .touch() Path methd:
file_path.touch()

# this create a new file called file1.txt in the new_directory/ folder. It does
# not contain any data yet, but the file exists:
print(f"file_path.exists() --> True = {file_path.exists()}")
print(f"file_path.is_file() --> True = {file_path.is_file()}")

# Unlike .mkdir(), the .touch() method does not raise an exception if the file
# being created with the Path object already exists:
# --> Calling .touch() a second time does not raise an exception:
file_path.touch()
# And it WON'T CHANGE THE CONTENT OF the already existing file.

# You CAN NOT create a file in a directory that does NOT exist:
file_path = new_dir / "folder_c" / "file2.txt"
# --> file_path.touch()
# Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
#    file_path.touch()
#  File r"C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\pathlib.py",
#  line 1305, in touch
#    fd = self._raw_open(flags, mode)
#  File r"C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\pathlib.py",
#  line 1117, in _raw_open
#    return self._accessor.open(self, flags, mode)
# FileNotFoundError: [Errno 2] No such file or directory:
# r'C:\\Users\\ssshh\\new_directory\\folder_c\\file2.txt'

# The FileNotFoundError is raised because the new_directory/ folder has no
# folder_c/ subfolder.
# Unlike the .mkdir() method, .touch() method has no 'parents' parameter that
# you can set to automatically create parent directories. This means that you
# need to first create any necessary  directories before calling the .touch()
# method to create a file.
print(f"file_path.parent --> {file_path.parent}")
# file_path.parent --> C:\Users\ssshh\new_directory\folder_c

# For instance, you can use the '.parent' attribute to get te path to the
# paarent folder for file2.txt and then call .mkdir() to create the directory:
file_path.parent.mkdir(exist_ok=True)
file_path.touch()


# Now that you know how to create files and directories, let's look at how to
# get the contents of a directory:

# Iterating Over Directory Contents:
""" Using pathlib, you can iterate over the contents of a directory. You might
need to do this in order to process all the files in a directory.
Everything in a directory is either a file or a subdirectory. The Path.iterdir()
method returns an iterator over Path objects representing each item in the
directory.
To use .iterdir() you first need a Path object representing a directory. Let's
use the new_directory/ folder that you previously created in your home directory
ans assigned to the new_dir variable:
"""
for path in new_dir.iterdir():
    print(f"path --> {path}")

# path --> C:\Users\ssshh\new_directory\file1.txt
# path --> C:\Users\ssshh\new_directory\folder_a
# path --> C:\Users\ssshh\new_directory\folder_c
# Right now, the new_dir/ folder contains the above three items.

# .iterdir() returns an iterable of path objects, so you can convert it to a list:
print(f"list(new_dir.iterdir() --> {list(new_dir.iterdir())})")
# list(new_dir.iterdir() --> [WindowsPath('C:/Users/ssshh/new_directory/file1.txt')
# , WindowsPath('C:/Users/ssshh/new_directory/folder_a'),
# WindowsPath('C:/Users/ssshh/new_directory/folder_c')])

# You will not often need to convert the iterable .iterdir() to a list.
# Generally, you will use .iterdir() in a for... loop like you did in the first
# example.

""" Notice that .iterdir() retuns only those items that are directly contained
in the new_directory/ folder. That is, yo can not see the path to the file that
exists in the folder_c directory.
There is a way to iterate over the contents a directory and all of its
subdirectories, but you can't do it easily with .iterdir().  We will get to
this task in a moment, but first let's talk about how to SEARCH FOR A FILE IN
A DIRECTORY.
"""
# SEACHING FOR A FILE IN A DIRECTORY:
"""Sometimes you only need to iterate over files of a certain type or files
with certain naming schemes. You can use the Path.glob() method on a path
representing a directory to get an iterable over directory contents that meet
some criteria.
The name of this methos is .glob(), because in early version of the Unix
operaating system, a program called glob was used to expand file path patterns
to full paths.
The .glob() method does something similar. You pas to the method a string
containing a pattern with a wildcard character, and .glob() RETURN A LIST OF
FILE PATHS THAT MATCH THE PATTERN.

A WILDCARD CHARACTER is a special character that acts as a placeholder in a
pattern. A wildcard character is replaced by other characters to create a
concrete file path. For example, in the pattern "*.txt", the asterisk (*) is
a wildcard character that can be replaced by any number of other characters.

The pattern "*.txt" matches any file path that ends with .txt. That is,
replacing the '*' in the pattern  with every characters in a file path up to
the last four characters results in the original file path, then that file path
is a MATCH for the pattern "*.txt".

Let's look at an example using he new_directory/ folder previously assigned to
the new_dir variable:
"""
for path in new_dir.glob("*.txt"):
    print(f"\n path --> {path}")

# path --> C:\Users\ssshh\new_directory\file1.txt
# Like .iterdir(), .glob() method returns an iterable of paths, but this time
# only the paths that match the pattern "*.txt" are returned.
# Note that .glob() method returns only the paths that are directly contained
# in the folder on which it is called.

# You can convert the return value of .glob() to a list:
path_obj_list = list(new_dir.glob("*.txt"))
print(f"\n path_obj_list --> {path_obj_list}")
print(f"list(new_dir.glob('*.txt')) --> {list(new_dir.glob('*.txt'))}")

first_file_name = path_obj_list[0].name
print(f"first_file_name --> {first_file_name}")
# or
first_file_name = list(new_dir.glob("*.txt"))[0].name
print(f"first_file_name --> {first_file_name}")

# You must often use .glob() in a for... loop.

# Below table describes some common wildcard characters:
# wildcard
# character     Description         Example Matches             Not match
# ---------     ------------------  ------- --------------      ---------
#     *         Any number of char  "*b*"   b, ab, bc, abc      a, c, ac
#     ?         A single char       "?bc"   abc, bbc, cbc       bc, aabc, abcd
#   [abc]       Match one char in
#               the brackes(optin)  [CB]at  Cat, Bat            at, cat, bat

"""We will  look at some examples of each of the wildcard characters later. But
first, let's  create a few more files in the new_directory/ folder so tha we
have more options to play with:
"""
paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
]

for path in paths:
    path.touch()

# Now this is the content of the new_directory and subdirectories:
# new_directory/

#       folder_a/
#           folder_b/
#               image1.jpg
#               image2.png

#       program3.py

#       folder_c/
#           file2.txt
#
#       file1.txt
#       program1.py
#       program2.py

# The '*' Wildcard:
# The '*' wildcard matches any number of characters in a file path pattern.
# for example, the pattern "*.py" matches all file paths that end in ".py":
new_dir_list_paths_end_py = list(new_dir.glob("*.py"))
print(f"\nnew_dir_list_paths_end_py --> {new_dir_list_paths_end_py}")
# new_dir_paths_end_py -->
# [WindowsPath('C:/Users/ssshh/new_directory/program1.py'),
# WindowsPath('C:/Users/ssshh/new_directory/program2.py')]

# You can use '*' multiple times in a single pattern:
new_dir_list_paths_with_number_1 = list(new_dir.glob("*1*"))
print(f"\n new_dir_list_paths_with_number_1 --> {new_dir_list_paths_with_number_1}")
# new_dir_list_paths_with_number_1 -->
# [WindowsPath('C:/Users/ssshh/new_directory/file1.txt'),
# WindowsPath('C:/Users/ssshh/new_directory/program1.py')]
# The '*1*' pattern matches any file path containing the number '1' with any
# number of characters before and after it.
# if you leave off the first *  from the pattern  "*1*" to get pattern "1*",
# then nothing gets matched
# >>> list(new_dir.glob("1*"))
# []


# The '?' Wildcard:
# The '?' wildcard characer matches a single character in a pattern. For
# example, the pattern "program?.py" will match any file path that starts with
# the word 'program' and is followed by a single character (any) and then .py
new_dir_list_program_paths = list(new_dir.glob("program?.py"))
print(f"\n new_dir_list_program_paths --> {new_dir_list_program_paths}")
# new_dir_list_program_paths -->
# [WindowsPath('C:/Users/ssshh/new_directory/program1.py'),
# WindowsPath('C:/Users/ssshh/new_directory/program2.py')]

# You can use multiple instances of '?' in a single pattern:
new_dir_list_folders = list(new_dir.glob("?older_?"))
print(f"\n new_dir_list_folders --> {new_dir_list_folders}")
#
# new_dir_list_folders -->
# [WindowsPath('C:/Users/ssshh/new_directory/folder_a'),
# WindowsPath('C:/Users/ssshh/new_directory/folder_c')]

# You can also combine the '*' and '?' wildcards:
new_dir_list_end_in_1_ext_2_chars = list(new_dir.glob("*1.??"))
print(
    f"\n new_dir_list_end_in_1_ext_2_chars --> \
{new_dir_list_end_in_1_ext_2_chars}"
)
# new_dir_list_end_in_1_ext_2_chars -->
# [WindowsPath('C:/Users/ssshh/new_directory/program1.py')]
# The pattern "*1.??" matches any file path that contains a 1 followed by a
# dot (.) and two more characters. The only path in new_directory/ matching
# this pattern is 'program1.py'. Notice that 'file1.txt' doesn't match the
# pattern because the dot is followed by three characters..


# The [] Wildcard:
""" The [] wildcard works kind of like the '?' wildcard because it matches only
a single character. The difference is that, instead of matcing any single
charaacter like '?' does, [] matches those characters that are between the
square brackets.
For example, the pattern "program[13].py" matches any path contaning the word
'program', followed by either a 1 or a 3 and the extension .py. In the
new_directory/ folder, program1.py is the only path matching this pattern:
"""
print(
    f"\n list(new_dir.glob('program[13].py')) --> \
{list(new_dir.glob('program[13].py'))}"
)
# list(new_dir.glob('program[13].py')) -->
#    [WindowsPath('C:/Users/ssshh/new_directory/program1.py')]

# As with other wildcards, you can use multiple instances of the [] wildcard as
# well as combine it with any of the others.


# RECURSIVE MATCHING WITH THE '**' WILDCARD:
""" The major limitation you've seen with both .iterdir() and .glob() is that
they return only those paths that are directly contained in the folder on which
they're called.
For example, new_dir.glob("*.txt") returns only the file1.txt path in the
new_directory/. It doesn't return the file2.txt path in the folder_c/
subdirectory even though that path matches the "*.txt" pattern.

There is a special wildcard character '**' that makes the pattern recursive.
The common way to used it is to prefix your pattern with "**/". This tells
to .glob() method to match your pattern in the current directory and in any of
its subdirectories.
For example, the pattern "**/*.txt" matches both file1.txt and folder_c/file2.txt
"""
print(f"\n list(new_dir.glob('**/*.txt')) --> {list(new_dir.glob('**/*.txt'))}")
# list(new_dir.glob('**/*.txt')) -->
# [WindowsPath('C:/Users/ssshh/new_directory/file1.txt'),
# WindowsPath('C:/Users/ssshh/new_directory/folder_c/file2.txt')]

# Similarly the patter "**/*.py" matches any .py in new_directory and in any of
# its subdirectories:
print(f"\n list(new_dir.glob('**/*.py')) --> {list(new_dir.glob('**/*.py'))}")
# list(new_dir.glob('**/*.py')) -->
# [WindowsPath('C:/Users/ssshh/new_directory/program1.py'),
# WindowsPath('C:/Users/ssshh/new_directory/program2.py'),
# WindowsPath('C:/Users/ssshh/new_directory/folder_a/program3.py')]

# There is also a shorthand method of recursive matching called .rglob(). To
# use it, pass the pattern without the "**/" prefix.
print(f"\n list(new_dir.rglob('*.py')) --> {list(new_dir.rglob('*.py'))}")
#  list(new_dir.rglob('*.py')) -->
# [WindowsPath('C:/Users/ssshh/new_directory/program1.py'),
# WindowsPath('C:/Users/ssshh/new_directory/program2.py'),
# WindowsPath('C:/Users/ssshh/new_directory/folder_a/program3.py')]

""" The 'r' in .rglob() stands for recursive. Some people prefer to use this
method instead of prefixing their patterns with "**/" because it's slightly
shorter. Both version are perfectly valid.
In this book, we will use .rglob() instead of the '**/' prefix.
"""

# Moving and Deleting Files and Folders:
""" Sometimes you need to move a file or directory to a new location or delete a
file or directory altogether. You can do this using pathlib. keep in mind that
the delete or moving files or directory can lead to loss of data.

To move a file or directory, use the .replace() method. For example, the
following moves the file1.txt file in the new_directory/ folder to the folder_a/
subfolder:
"""
source = new_dir / "file1.txt"
destination = new_dir / "folder_a" / "file1.txt"
source.replace(destination)  # Moves the file1.txt to destination.
destination.replace(source)  # Moves the file1.txt to source

# Notice that .replace() moves the file and returns the path of the new location
# of the file:
# >>> destination.replace(source)
# WindowsPath('C:/Users/ssshh/new_directory/file1.txt')
# >>> source.replace(destination)
# WindowsPath('C:/Users/ssshh/new_directory/folder_a/file1.txt')

moved_to_loc = source.replace(destination)
if moved_to_loc == destination:
    print("\n *** yes moved successfully")
    print(str(moved_to_loc))
else:
    print("\nreview hector")
    print(str(moved_to_loc))
if str(moved_to_loc) == r"C:\Users\ssshh\new_directory\folder_a\file1.txt":
    print("Yes again moved successfully")

# if the destination path IS FOR A FILE and already exists, then .replace()
# overwrites the
# destination with the source file without raising any kind of exception. This
# can cause undesired loss of data if you are not careful.
# You may want to first check if the destination file exists and move the file
# only if it does not:
# if not destination.exists():
#     source.replace(destination)

# You can also use .replace() to move or rename an entire directory. For
# instance, the following code rename the folder_c subdirectory of
# new_directory/ to folder_d/:
source = new_dir / "folder_c"
folder_d = new_dir / "folder_d"
if not folder_d.exists():
    source.replace(folder_d)  # destination

# Again, if the destination path is for a FOLDER AND already exists, then the
# Permission.Error will be generated:
# Traceback (most recent call last):
#  File "C:\PythonBasicsBookExercises\cha12\cha12-01_Files_FileSystem_Direc
# toryFolder.py", line 787, in <module>
#    source.replace(destination)
# File "C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\pathlib.py",
# line 1385, in replace
#    self._accessor.replace(self, target)
# PermissionError: [WinError 5] Access is denied: 'C:\\Users\\ssshh\\new_direc
# tory\\folder_c' -> 'C:\\Users\\ssshh\\new_directory\\folder_d'


# DELETE file and folder:
# To delete a file use the .unlink() method:
file_path = new_dir / "program1.py"
file_path.unlink()
# This deletes the program1.py file in the new_directory/ folder, which you can
# check with .exists() method:
print(f"file_path.exists() ? --> False = {file_path.exists()}")

# You can also see tht it's been removed using .iterdir() method:
# >>> list(new_dir.iterdir())
# [WindowsPath('C:/Users/ssshh/new_directory/folder_a'),
# WindowsPath('C:/Users/ssshh/new_directory/folder_c'),
# WindowsPath('C:/Users/ssshh/new_directory/folder_d'),
# WindowsPath('C:/Users/ssshh/new_directory/program2.py')]
# >>>

# if the path that you call .unlink() on does not exist, then a
# FileNotFoundError exception is raised:
# >>> file_path.unlink()
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     file_path.unlink()
#   File "C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\pathlib.py",
#        line 1344, in unlink
#     self._accessor.unlink(self)
# FileNotFoundError: [WinError 2] The system cannot find the file specified:
# 'C:\\Users\\ssshh\\new_directory\\program1.py'
# >>>

# If you want to ignore the exception, then set the optinal 'missing_ok'
# parameter to True:
file_path.unlink(missing_ok=True)


# IMPORTANT: When you delete a file, it is gone forever. Make sure you really
# want to delete it before you proceed.

# You can use .unlink() only with paths representing files. To remove a
# directory instead, you can use the .rmdir() method. Keep in mind that the
# folder must be empty. Otherwise, the operation will raise an OSError exception

# folder_d.rmdir()
# Traceback (most recent call last):
#   File "<pyshell#1>", line 1, in <module>
#     folder_d.rmdir()
#   File "C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\pathlib.py",
#   line 1353, in rmdir
#     self._accessor.rmdir(self)
# OSError: [WinError 145] The directory is not empty:
# 'C:\\Users\\ssshh\\new_directory\\folder_d'
# >>>


# In the case of folder_d/, it contains only a single file called file2.txt. To
# delete folder_d/, first delete all of the files it contains:
for path in folder_d.iterdir():
    path.unlink()

# now:
folder_d.rmdir()
# Verify is folder_d is deleted:
print(f"folder_d.exists()? --> False = {folder_d.exists()}")

hect_dir = new_dir / "hect_dir"
hect_dir.mkdir()
print(f"hect_dir.exists()? --> True = {hect_dir.exists()}")
hect_dir.rmdir()
print(f"hect_dir.exists()? --> False = {hect_dir.exists()}")

# If you need to delete an entired directory even if it is not empty, then
# pathlib won't help you much. However, the built-in 'shutil' module includes a
# rmtree() function that you can use to delete directories populated with files.
# Here is how you ue rmtree() function to delete folder_a/:
import shutil

folder_a = new_dir / "folder_a"
shutil.rmtree(folder_a)

# Recall that folder_a/ contains a subfolder, folder_b/, which itself contains
# two files called image1.jpg and image2.png.
# When you pass the folder_a path object to shutil.rmtree(), folder_a/ and all
# its contents are deleted.
# The folder_a/ directory no longer exists:
folder_a.exists()
# --> False
# Searching for 'image*.*' files returns nothing.
list(new_dir.rglob("image*.*"))
# --> []

# You should always use caution when working with the file system. When in
# doubt, check that a file path exists before performing an operation, and
# always confirm with the user that what you're about to do is okay.

# Review Exercises:
# 1: Create a new directory in your home folder called my_folder:
my_folder = pathlib.Path.home() / "my_folder"
my_folder.mkdir(parents=True, exist_ok=True)

# 2: Inside the my_folder/ create three files
file_path = my_folder / "file1.txt"
file_path.touch()

file_path = my_folder / "file2.txt"
file_path.touch()

file_path = my_folder / "image1.png"
file_path.touch()

# 3: Move the file image1.png to a new directory called images/ inside the
# my_folder/ directory:
images = my_folder / "images"
images.mkdir(parents=True, exist_ok=True)

destination = images / "image1.png"
source = my_folder / "image1.png"

source.replace(destination)

# 4: Delete the file file1.txt
file_path = my_folder / "file1.txt"
file_path.unlink()

# 5: Delete the my_folder/ directory:
import shutil

shutil.rmtree(my_folder)

# Challenge: Move All Image Files to a New Directory.
# In my Home directory: Create a folder called practice_files/, containing a
# subfolder called documents/. This subfolder contains several files and
# subfolders. Some of the files are image ending with the .png, .gif, or .jpg
# file extension.
# Create a new folder in the practice_folder/ called images/, and move all the
# image files to that folder.
practice_files = pathlib.Path.home() / "practice_files"
practice_files.mkdir(parents=True, exist_ok=True)
documents = practice_files / "documents"
documents.mkdir(parents=True, exist_ok=True)
folder_path = documents / "folder_a"
folder_path.mkdir(parents=True, exist_ok=True)
folder_path = documents / "folder_b"
folder_path.mkdir(parents=True, exist_ok=True)

image_files_list = ["image1.png", "image2.gif", "image3.png", "image4.jpg"]

for file in image_files_list:  # loop to create the files in documents/
    file_path = documents / file  # Create the file path
    file_path.touch()  # create the file using the file path

images_folder = practice_files / "images"
images_folder.mkdir(parents=True, exist_ok=True)

for file_path in documents.iterdir():
    if file_path.is_file:
        if file_path.suffix.lower() in (".png", ".gif", ".jpg"):
            file_path.replace(images_folder / file_path.name)

# To prepare the solution from the book:


# Solution from the book:
# Change this path to match the location on your computer
# documents_dir = Path.cwd() / "practice_files" / "documents"

# Create an images/ directory in your home directory
# images_dir = Path.home() / "images"
# images_dir.mkdir(exist_ok=True)

# Search for image files in the documents directory and move
# them to the images/ directory
# for path in documents_dir.rglob("*.*"):
#    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
#        path.replace(images_dir / path.name)
