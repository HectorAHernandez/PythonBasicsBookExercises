# 12.5 Reading and writing files:
# What is a file?
# A file is a sequence of BYTES and a byte is a number between 0 and 255. That
# is, a file is a sequence of integer values.
""" The bytes in a file must be DECODED into something meaningful in order to
undertand the contents of the file.

Python has standard library modules for working with text, CSV, and audio files.
There are a number of third-party packages available for working with other
file types.
"""

# Understanding Text Files:
""" Text files are files that contain only text. Issues when working with text
files:
1- Character encoding.
2- Line endings.

Character Encoding: Text files are stored on disk as a sequence of bytes. Each
byte, or group of bytes (double bytes characters) in some cases, represent a
different character in the file.

When text files are written, characters typed in the keyboard are converted into
bytes in a process called ENCODING. When a file is read, the bytes are DECODED
back into text characters.

The integer a character is associated with is determined by the file's CHARACTER
ENCODING. There are many character encodings. These are the four most widely
used:
1- ASCII
2- UTF-8.
3- UTF-16
4- UTF-32

Some character encodings, such as ACII and UTF-8, encode characters the same way.
For example, numbers and English letters are encoded the same way in both ASCII
and UTF-8.
The difference between ASCII and UTF-8 is that UTF-8 can encode more characters.
ASCII CAN NOT encode characters like 'n~' enie our '"' virgulina, but UTF-8 can.
This means that you can DECODE ASCII-encoded text with UTF-8, but you CAN NOT
DECODE UTF-8-encoded text with ASCII.

IMPORTANT: Serious problems may occur when different encodings are used to
encode and decode text.
For instance, text encoded as UTF-8 that is decoded as UTF016 may be interpreted
as an entirely different language than originally intended!
For a thorough introduction to character encodings, check out Real Python's
"Unicode & Character Encoding in Python: A Painless Guide" at:
https://realpython.com/python-encodings-guide/#enter-unicode

Knowing which encodings a file uses is important, but it isn't always obvious.
On modern Windows computers, text files are normally encoded with UTF-16 or UTF-8.
On macOS and Ubuntu Linux, default character encoding is usually UTF-8.
For the remaining of this section, we will assume that the character encoding of
all text files that we work with is UTF-8. If you encounter problems, then you
may alter the examples to use a different encoding.
"""
# Line Ending:
"""Each line in a text file ends with one or two characters that indicate that
the line has ended. These characters are not usually displayed in a text editor,
but they exist as bytes in the file data.
The two character used to represent line ending are the CARRIAGE RETURN and LINE
FEED characters. In Python string, these characters are represented by the scape
sequence \r and \n, respectively.

On Windows, line endings are represented by default with both a carriage return
and a line feed. On macOS and most Linux distributions, line endings are
represented with just a single line feed character.

When you read a Windows file on macOS or Linux, you will sometimes see extra
blank lines between lines of text. This is because the carriage return byte also
represents a line ending on macOS and Linux.
For example, suppose the following text file was created in Windows:
Pug\r\n
Jack Russell Terrier\r\n
English Springer Spaniel\r\n
German Shepherd\r\n

On macOS or Ubuntu, the file is interpreted with double spacing between lines:
Pug\r
\n
Jack Russell Terrier\r
\n
English Springer Spaniel\r
\n
German Shepherd\r
\n

In practice, the differences between line endings on different operating systems
is rarely problematic. Python can handle line ending conversions for you
automatically, so you don't have to worry about it too often.
"""

# Python File Object:
""" Files are represented in Python with FILE OBJECTS, which are instances of
classes designed to work with different types of files.
Python has a couple of different types of FILE OBJECTS:
1- Text file objects: are used for interacting with text files.
2- Binary file object: are used for working directly with the bytes contained
   in files.

Text file objects handle the ENCODING and DECODING bytes for you. All you need
vcruntime140_1.dll). Binary file objects, on the other hand, do not perform any
kind of encoding or decoding.

There are two ways to create a file object in Python:
1- The Path.open() method.
2- The built-in open() function.
"""

# The Path.open() Method:
# To use the Path.open() method, you first neeed a Path object indicating the
# path of the file to open
from pathlib import Path

file_path_1 = Path.home() / "hello.txt"
file_path_1.touch()  # create the file physical

file_obj = file_path_1.open(mode="r", encoding="utf-8")

# First, you create a Path object for the hello.txt file and assign it to the
# file_path_1 varibale. Then file_path_1.touch() creates the file in your home
# directory. Finally .open() returns a nw file object representing the hello.txt
# file and assigns it to the file_obj variable.

# Two keyword parameters are used to open the file:
"""
1- The 'mode' parameter determines in which mode the file should be opened. The
   'r' argument opens the file in READ mode.
2- The 'encoding' parameter determines the character encoding used to decode the
   file. The argument 'utf-8' represent UTF-8 character encoding.
"""
# You can inspect the file_obj variable to see that it is assigned to a text
# file object:
# >>> file_obj
# <_io.TextIOWrapper name='C:\\Users\\ssshh\\hello.txt' mode='r' encoding='utf-8'>
print(file_obj)
# <_io.TextIOWrapper name='C:\\Users\\ssshh\\hello.txt' mode='r' encoding='utf-8'>

# Text file objects are instances of the TextIOWrapper class. You will never
# need to instantiate this class directly since you can create it with the
# Path.open() method.
# Also we can access the attributes that the file_obj instance contains like:
# name, mode and encoding:
# >>> file_obj.name
# --> 'C:\\Users\\ssshh\\hello.txt'
print(file_obj.name)
# --> C:\Users\ssshh\hello.txt
# >>> file_obj.mode
# --> 'r'
print(file_obj.mode)
# --> r
# >>> file_obj.encoding
# --> 'utf-8'
print(file_obj.encoding)
# --> utf-8

""" There are a number of different modes you can use to open a file. These are
described in te following table:
Mode   Description
----   -----------------------------------------------------------------------
'r'    Create a text file object for reading and raises an error if the file
       can not be opened.
'w'    Create a text file object for writing and overwrites all existing data
       in the file.
'a'    Create a text file object for appending data to the end of a file.
'rb'   Create a binary file object for reading and raises an error if the file
       can not be opened.
'wb'   Create a binary file object for writing and overwrites all existing data
       in the file.
'ab'   Create a binary file object for appending data to the end of the file.


The strings for some of the most commonly used character encodings can be found
in the table below:
String   Character Encoding
------   ------------------
'ascii'  ASCII
'utf-8'  UTF-8
'utf-16' UTF-16
'utf-32' UTF-32
"""
# practicing a bit with the file_object:
read_file_path = Path(file_obj.name)
print(f"read_file_path.name --> {read_file_path.name}")

# When you create a file object with .open() method, Python maintains a link to
# the file resource until yo either explicitly tell Python to close the file or
# the program ends.

# IMPORTANT: You should ALWAYS EXPLICITLY tell Python to close a file.
# Forgetting to close opened files is like littering. When your program stops
# running, it shouldn't leave unnecessary waste lying around the system.

# To close a file, use the file object's .close() method:
file_obj.close()

# Using the Path.open() method is the preferred way to open a file when you have
# an existing Path object, but there is also a built-in function called open()
# that can be used to open a file.

# The Built-in open() Function:
""" The built-in open() function works almost exactly like the Path.open()
method, except that its first parameter is a string containing the path to the
file you want to open.
First, create a new variable called file_path and assign to it a string
containing teh path to the hello.txt fiel you created above:
"""
file_path = "C:/Users/ssshh/hello.txt"

# Next, create a new file object using the built-in function open() and assign
# it to the variable file_2:
file_2 = open(file_path, mode="r", encoding="utf-8")
# other way: file_2 = open("C:/Users/ssshh/text.txt", mode="r", encoding="utf-8")

# Just like the file object returned by Path.open() method, the file object
# returned by the open() function is a TextIOWrapper instance.
# >>> file_2
# <_io.TextIOWrapper name='C:/Users/ssshh/hello.txt' mode='r' encoding='utf-8'>
# >>>

# To close the file, use the file object's .close() method:
file_2.close()

# For the most part, you will use the Path.open() method to open a file from an
# existing pathlib.Path object. However, if you don't need all of the
# functionality of teh pathlib module, then the built-in open() function is a
# great way to quickly create a file object to open a file.


# The 'with' Statement:
""" When you open a file, your program accesses data external to the program
itself. The operating system must manage the connection between your program and
the physical file. When you call a file object's .close() method, the operating
system knows to close the connection.

If your program crashes between the time a file is opened and when it is closed,
then the system resources used by the connection may live on until the operating
system realizes that they are no longer needed.

To ensure that file system resources are cleaned up even if a program crashes,
you can open the file in a 'with' statement. The pattern for using the 'with'
statement looks like this:
with path.open(mode="r", encoding="utf-8") as file_object:
    # Do something with file.

The 'with' statement has two partsa: a header and a body. The header always
start with the 'with' keyword and ends with a colon (:). The return value of
path.open() is assigned to the variable name after the 'as' keyword.

After the 'with' statment header is an indented block of code. When code
execution leaves the indented block, the file object assigned to file_object is
closed automatically, even if an exception is raised during execution of the
code inside the block.

'with' statement also works with the built-in function open():
with open(file_path, mode="r", encoding="utf-8") as file_obj:
    # Do somthing with file_obj

There really is no reason for NOT to open files in a 'with' statemenet. It is
considered the Pythonic way of working with files. For the rest of this book,
we will use this pattern when opening files.
"""

# Reading data from a file:
# Using a text editor program, open the hello.txt file in your home directory
# that you previously created and type the text "Hello, World" into it. Then
# save the file.
file_path = Path.home() / "hello.txt"
with file_path.open(mode="r", encoding="utf-8") as file_obj:
    text_1 = file_obj.read()

# The file object created by file_path.open() is assigned to the file_obj
# variable. Inside the 'with' block, the file object's .read() method reads the
# content from the file and assigns the result to the variable text_1.
# The value returned by .read() method is a string object with the value
# "Hello, World":
# >>> text_1
# 'Hello, World.'
# >>> type(text_1)
# <class 'str'>
# >>>

# The .read() method reads ALL the text in the file and returns it as a string.
# If there are multiple lines of text in the file, then each line in the string
# is SEPARATED with the NEWLINE CHARACTER (\n). In a text editor, open the
# hello.txt file again and put the text "Hello again" on the second line. Then
# save the file.

# Now read the text from teh file again:
with file_path.open(mode="r", encoding="utf-8") as file_obj:
    text_2 = file_obj.read()

print(f"text_2 --> {text_2}")
# --> text_2 --> Hello, World.
#     Hello again
# >>> text_2
# 'Hello, World.\nHello again'
# >>>
# The text from each line has a newline (\n) character in between.
# Instead of reading the entires file at once, you can process each line of the
# file one at a time using teh .readlines() method:
with file_path.open(mode="r", encoding="utf-8") as file_obj:
    for line in file_obj.readlines():
        print(f"line --> {line}")
# -->
# line --> Hello, World.
#
# line --> Hello again
# >>>

# The .readlines() method returns an ITERABLE of lines from the file. At each
# step of the for loop, the next line of text in the file is returned and printed
# Notice the extra line between the two lines of text. This is not caused by
# line ending \n in the file. It happens because the built-in print() function
# automatically inserts a newline character \n at the end of every string it
# print.
# To print the two lines without the extra blank line, set the print()
# function's optional 'end' parameter to an empty string "":
with file_path.open(mode="r", encoding="utf-8") as file_obj:
    for line in file_obj.readlines():
        print(line, end="")
# -->
# Hello, World.
# Hello again

# You will often want to use .readlines() instead of .read(). For example, each
# line in a file might represent a single record. You can use .readlines()
# method to loop over the lines and process them as needed.

# If you try to read from a file that DOES NOT exist, then both Path.open() and
# the built-in open() function rasise a FileNotFoundError:
# path = Path.home() / "new_file.txt"
# with path.open(mode="r", encoding="utf-8") as file_obj:
#    text = file_obj.read()
# -->
"""Traceback (most recent call last):
  File r"C:\\PythonBasicsBookExercises\\cha12\\cha12-05_Reading_And_Writing_Files.py",
  line 333, in <module> with path.open(mode="r", encoding="utf-8") as file_obj:
  File r"C:\\Users\ssshh\\AppData\\Local\\Programs\\Python\\Python39\\vcruntime140_1.dll\lib\pathlib.py",
  line 1242, in open
    return io.open(self, mode, buffering, encoding, errors, newline,
  File r"C:\\Users\\ssshh\\AppData\\Local\\Programs\\Python\\Python39\\lib\\pathlib.py",
    line 1110, in _opener return self._accessor.open(self, flags, mode)
FileNotFoundError: [Errno 2]
No such file or directory: r'C:\\Users\\ssshh\\new_file.txt'
>>> 
"""

# Writing Data To a File:
"""To write data to a plain text file, you passa string to a file object's
.writes() method. The file must be opened in WRITE MODE by passing the value 'w'
to the 'mode' parameter.
For instance, the following writes the text "Hi there!" to the 'hello.txt' file
in your home directory:
"""
# >>> with file_path.open(mode="w", encoding="utf-8") as file:
# 	file.write("Holaa There!")
#
#
# 12
with file_path.open(mode="w", encoding="utf-8") as file_obj:
    chars_written = file_obj.write("Holaa there!")
    print(f"\nchars_written --> 12 = {chars_written}")
# Hello There!chars_written --> 12 = 12
"""Notice that the integer 12 is displayed after the with block executes. That
is because .write() method returns the number of characters it writes. The
string 'Holaa there!' has 12 characters, to .write() returns 12.

When the text 'Holaa there!' is written to the hello.txt file, any existing
contents are overwritten. It is as if you deleted the old hello.txt file and
created a new one.

IMPORTANT: When you set mode='w' in .open(), the contents of the original file
           are overwritten. This result in the loss of the original data in the
           file.

You can verify that the file contains only the text 'Holaa There!' by reading
and displaying the contents of the file:
"""
with file_path.open(mode="r", encoding="utf-8") as file_obj:
    text = file_obj.read()
    print(f"\n text --> {text}")
# -->  text --> Holaa there!

# Appending Data to The End of a File:
# You can append data to the end of a file by opening the file in append mode:
with file_path.open(mode="a", encoding="utf-8") as file_obj:
    file_obj.write("\nHello")

# >>> with file_path.open(mode="a", encoding="utf-8") as file:
# 	file.write("\nHello")
#
# 6
# >>>
# When a file is opened in append mode, new data is written at the end of the
# file and old data is left intact. The newline character \n is put at the
# beginning of the string so that the word "Hello" is printed on a new line at
# the end of the file.
# Without the newline character at the beginning of the string, the word "Hello"
# would be printed on the same line as anyu existing text at the end of the file
# Also, the newline character is counted as part of the number of characters
# written to the end of the file, this is why 6 is displayed.

# Below check that the word "Hello" was appended to a new line:
with file_path.open(mode="r", encoding="utf-8") as file_obj:
    text = file_obj.read()
    print(f"text after appending 'Hello' --> \n{text}")


# Writing Multiple lines to a file at the same time:
# You can write multiple lines to a file at the same time using the
# .writelines() method. First, we have to create a list of strings containing
# all the lines to add:
lines_of_text = ["Hello from line 1\n", "Hello from line 2\n", "Hello from line 3\n"]

with file_path.open(mode="w", encoding="utf-8") as file_obj:
    file_obj.writelines(lines_of_text)

# Each string in lines_of_text is written to the file. Notice that each string
# ends with the newline character \n. That is because .writelines() method
# does not automatically write each string on a new line.

# Now appending multiple lines, is the same we just need to open the file in the
# append mode:
lines_of_text_2 = (
    "Hola desde linea 4\n",
    "Hola desde linea 5\n",
    "Hola desde Linea 6\n",
)
with file_path.open(mode="a", encoding="utf-8") as file_obj:
    file_obj.writelines(lines_of_text_2)

# If you open a nonexisting file_path in write mode, then Python will create the
# file as long as all the parent folders in the path exist:
file_path = Path.home() / "new_file.txt"
with file_path.open(mode="w", encoding="utf-8") as file_obj:
    file_obj.write("Hello new_file.txt")

# Since the file_path (Path.home()) directory exists, a new file called
# new_file.txt is created automatically. However, if one of the parent
# directories does not exist, then .open() will raise a FileNotFoundError:
# path = Path.home() / "new_folder" / "new_file2.txt"
# with path.open(mode="w", encoding="utf-8") as file:
#    file.write("hello new_file2.txt")
"""Traceback (most recent call last):
  File "C:\\PythonBasicsBookExercises\\cha12\cha12-05_Reading_And_Writing_Files.
  py\\cha12-05_Reading_And_Writing_Files.py
  ", line 447, in <module>
    with path.open(mode="w", encoding="utf-8") as file:
  File "C:\\Users\\ssshh\\AppData\\Local\\Programs\\Python\\Python39\\lib\zoneinfo\\pathlib.py",
  line 1242, in open
    return io.open(self, mode, buffering, encoding, errors, newline,
  File "C:\\Users\ssshh\\AppData\\Local\\Programs\\Python\\Python39\\lib\\pathlib.py",
  line 1110, in _opener
    return self._accessor.open(self, flags, mode)
FileNotFoundError: [Errno 2] No such file or directory:
'C:\\Users\\ssshh\\new_folder\\new_file2.txt'
>>> 
"""
# if you want to write to a path with parent folders that may not exist, call
# the .mkdir() method with the 'parents' parameter set to True before opening
# the file in write mode:
file2_path = Path.home() / "new_folder" / "new_file2.txt"
file2_path.parent.mkdir(parents=True, exist_ok=True)
with file2_path.open(mode="w", encoding="utf-8") as file:
    file.write("hello new_file2.txt")

# above file2_path.parent. --> calls the parent directory of the file path
# defined in order to create the directory for it.

# Review Exercises:
# 1:
# Write the following text to a file in your home directory called
# starships.txt: Discovery, Enterprise, Defiant, Voyager.
# Each word should be in a separate line:
starships_list = ["Discovery\n", "Enterprise\n", "Defiant\n", "Voyager\n"]
file_path = Path.home() / "starships.txt"
with file_path.open(mode="w", encoding="utf-8") as file_obj:
    file_obj.writelines(starships_list)

# 2:
# Read the file starships.txt that you created in exercise 1 and print each
# line of text in the file. the output should not ahve extra blank lines between
# each word.
with file_path.open(mode="r", encoding="utf-8") as file_obj:
    for line in file_obj.readlines():
        print(f"Starship: {line}", end="")

# 3:
# Read the file starships.txt and print the names of the starships that start
# with the letter D:
with file_path.open() as file:
    print("\nStarships with name starting with lette 'D':")
    for line in file.readlines():
        if line[0] == "D":
            print(line, end="")


# xxxxxxxxxx
