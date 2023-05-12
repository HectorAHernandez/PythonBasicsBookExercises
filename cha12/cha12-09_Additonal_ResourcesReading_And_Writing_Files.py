"""
Getting a Directory Listing
Suppose your current working directory has a subdirectory called my_directory
that has the following contents:

my_directory/
|
├── sub_dir/
|   ├── bar.py
|   └── foo.py
|
├── sub_dir_b/
|   └── file4.txt
|
├── sub_dir_c/
|   ├── config.py
|   └── file5.txt
|
├── file1.py
├── file2.csv
└── file3.txt
The built-in os module has a number of useful functions that can be used to
list directory contents and filter the results. To get a list of all the files
and folders in a particular directory in the filesystem, use os.listdir() in
legacy versions of Python or os.scandir() in Python 3.x. os.scandir() is the
preferred method to use if you also want to get file and directory properties
such as file size and modification date.

Directory Listing in Legacy Python Versions
In versions of Python prior to Python 3, os.listdir() is the method to use to get a directory listing:
"""
import os

entries = os.listdir("c:/users/ssshh/my_directory/")
print(f"entries --> {entries}")
# os.listdir() returns a Python list containing the names of the files and
# subdirectories in the directory given by the path argument:
# entries --> ['file1.py', 'file2.csv', 'file3.txt', 'sub_dir', 'sub_dir_b',
# 'sub_dir_c']

# We can also process the result as a list:
for entry in entries:
    print(f"entry --> {entry}")
# entry --> file1.py
# entry --> file2.csv
# entry --> file3.txt
# entry --> sub_dir
# entry --> sub_dir_b
# entry --> sub_dir_c


""" Directory Listing in Modern Python Versions:
In modern versions of Python, an alternative to os.listdir() is to use
os.scandir() and pathlib.Path().

os.scandir() was introduced in Python 3.5 and is documented in PEP 471.
os.scandir() returns an iterator as opposed to a list when called:"""
print("\n")
import os

entries = os.scandir("c:/users/ssshh/my_directory/")
print(f"entries --> {entries}")
# entries --> <nt.ScandirIterator object at 0x000001841AEC8EE0>
# The ScandirIterator points to all the entries in the current directory. You
# can loop over the contents of the iterator and print out the filenames:
import os

with os.scandir("c:/users/ssshh/my_directory/") as entries:
    for entry in entries:
        print(f"Using os.scandir() entry.name --> {entry.name}")
        # the name of the file or sub_dir.
"""Here, os.scandir() is used in conjunction with the with statement because it
supports the context manager protocol. Using a context manager closes the
iterator and frees up acquired resources automatically after the iterator has
been exhausted. The result is a print out of the filenames in my_directory/ just
like you saw in the os.listdir() example:
Using os.scandir() entry.name --> file1.py
Using os.scandir() entry.name --> file2.csv
Using os.scandir() entry.name --> file3.txt
Using os.scandir() entry.name --> sub_dir
Using os.scandir() entry.name --> sub_dir_b
Using os.scandir() entry.name --> sub_dir_c """

print("\n")
# Another  way to get a directory isting is to use the pathlib module:
from pathlib import Path

entries = Path("c:/users/ssshh/my_directory/")
for entry in entries.iterdir():
    print(f"Using pathlib.Path entry.name --> {entry.name}")
"""    Running the code above produces the following:

Using pathlib.Path entry.name --> file1.py
Using pathlib.Path entry.name --> file2.csv
Using pathlib.Path entry.name --> file3.txt
Using pathlib.Path entry.name --> sub_dir
Using pathlib.Path entry.name --> sub_dir_b
Using pathlib.Path entry.name --> sub_dir_c



The objects returned by Path are either PosixPath or WindowsPath objects
depending on the OS.

pathlib.Path() objects have an .iterdir() method for creating an iterator of
all files and folders in a directory. Each entry yielded by .iterdir() contains
information about the file or directory such as its name and file attributes.
pathlib was first introduced in Python 3.4 and is a great addition to Python
that provides an object oriented interface to the filesystem.

In the example above, you call pathlib.Path() and pass a path argument to it.
Next is the call to .iterdir() to get a list of all files and directories in
my_directory.

pathlib offers a set of classes featuring most of the common operations on
paths in an easy, object-oriented way. Using pathlib is more if not equally
efficient as using the functions in os. Another benefit of using pathlib over
os is that it reduces the number of imports you need to make to manipulate
filesystem paths. For more information, read Python 3's pathlib Module: Taming
the File System.


Using pathlib.Path() or os.scandir() instead of os.listdir() is the preferred
way of getting a directory listing, especially when you're working with code
that needs the file type and file attribute information. pathlib.Path() offers
much of the file and path handling functionality found in os and shutil, and
it's methods are more efficient than some found in these modules. We will
discuss how to get file properties shortly.

Here are the directory-listing functions again:

Function	Description
os.listdir()	Returns a list of all files and folders in a directory
os.scandir()	Returns an iterator of all the objects in a directory including
                file attribute information
pathlib.Path.iterdir()	Returns an iterator of all the objects in a directory
                including file attribute information
                
These functions return a list of everything in the directory, including
subdirectories. This might not always be the behavior you want. The next
section will show you how to filter the results from a directory listing.


Listing All Files in a Directory:
This section will show you how to print out the names of files in a directory
using os.listdir(), os.scandir(), and pathlib.Path(). To filter out directories
and only list files from a directory listing produced by os.listdir(), use
os.path:
"""
import os

# List all files in a directory using os.listdir
basepath = "c:/users/ssshh/my_directory/"
for entry in os.listdir(basepath):
    print(f"entry-0 --> {entry}")
    if os.path.isfile(os.path.join(basepath, entry)):
        print(f"entry --> {entry}")

# Here, the call to os.listdir() returns a list of everything in the specified
# path, and then that list is filtered by os.path.isfile() to only print out
# files and not directories. This produces the following output:
"""
entry-0 --> file1.py
entry --> file1.py
entry-0 --> file2.csv
entry --> file2.csv
entry-0 --> file3.txt
entry --> file3.txt
entry-0 --> sub_dir
entry-0 --> sub_dir_b
entry-0 --> sub_dir_c"""
# An easier way to list files in a directory is to use os.scandir() or
# pathlib.Path():
import os

# List all files in a directory using scandir()
basepath = "c:/users/ssshh/my_directory/"
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(f"scandir entry.name --> {entry.name}")

# Using os.scandir() has the advantage of looking cleaner and being easier to
# understand than using os.listdir(), even though it is one line of code longer.
# Calling entry.is_file() on each item in the ScandirIterator returns True if
# the object is a file. Printing out the names of all files in the directory
# gives you the following output:
"""
scandir entry.name --> file1.py
scandir entry.name --> file2.csv
scandir entry.name --> file3.txt"""


# Here's how to list files in a directory using pathlib.Path():
from pathlib import Path

basepath = Path.home() / "my_directory/"
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(f"path.iterdir(), file.name --> {item.name}")
"""
Here, you call .is_file() on each entry yielded by .iterdir(). The output
produced is the same:
path.iterdir(), file.name --> file1.py
path.iterdir(), file.name --> file2.csv
path.iterdir(), file.name --> file3.txt

The code above can be made more concise if you combine the for loop and the if
statement into a single generator expression. Dan Bader has an excellent article
on generator expressions and list comprehensions.

The modified version looks like this:
"""
from pathlib import Path

# List all files in directory using pathlib:
basepath = Path.home() / "my_directory/"
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for file in files_in_basepath:
    print(f"new way with Pathlib, file.name --> {file.name}")

"""
This produces exactly the same output as the example before it. This section
showed that filtering files or directories using os.scandir() and pathlib.Path()
feels more intuitive and looks cleaner than using os.listdir() in conjunction
with os.path."""

# Listing Subdirectories:
# To list subdirectories instead of files, use one of the methods below. Here is
# how to use os.listdir() and os.path() methods:
import os

# List all subdirectories using os.listdir
basepath = Path.home() / "my_directory/"
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(f"All subdir using os.listdir() --> {entry}")
"""
Manipulating filesystem paths this way can quickly become cumbersome when you
have multiple calls to os.path.join(). Running this on my computer produces the
following output:
All subdir using os.listdir() --> sub_dir
All subdir using os.listdir() --> sub_dir_b
All subdir using os.listdir() --> sub_dir_c"""

# Here is how to use os.scandir()
import os

# List all subdirectories using os.scandir()
basepath = Path.home() / "my_directory/"

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(f"All subdir using os.scandir() --> {entry.name}")

""" As in the file listing example, here you call .is_dir() on each entry
returned by os.scandir(). If the entry is a directory, .is_dir() returns True,
and the directory's name is printed out. The output is the same as above:
All subdir using os.scandir() --> sub_dir
All subdir using os.scandir() --> sub_dir_b
All subdir using os.scandir() --> sub_dir_c"""

# using pathlib.Path:
from pathlib import Path

# List all subdir usint pathlib
basepath = Path.home() / "my_directory/"
for entry in basepath.iterdir():
    if entry.is_dir():
        print(f"All subdir using Path.iterdir() --> {entry.name}")

""" Calling .is_dir() on each entry of the basepath iterator checks if an entry
is a file or a directory. If the entry is a directory, its name is printed out
to the screen, and the output produced is the same as the one from the
previous example:
All subdir using Path.iterdir() --> sub_dir
All subdir using Path.iterdir() --> sub_dir_b
All subdir using Path.iterdir() --> sub_dir_c



Getting File Attributes
Python makes retrieving file attributes such as file size and modified times
easy. This is done through os.stat(), os.scandir(), or pathlib.Path().

os.scandir() and pathlib.Path() retrieve a directory listing with file
attributes combined. This can be potentially more efficient than using
os.listdir() to list files and then getting file attribute information for
each file.

The examples below show how to get the time the files in my_directory/ were last
modified. The output is in seconds:
"""
import os

with os.scandir(Path.home() / "my_directory/") as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(f"name --> {entry.name} info - entry.stat() --> {info}")
        print(f"modified time info.st_mtime --> {info.st_mtime}")
        print(f"number of characters in file info.st_size --> {info.st_size}")
# info.st_size --> attribute with the number of characters in the file. dir=0
# info.st_mtime--> attribute with the number of seconds when the file was
# modified
"""
name --> file1.py info - entry.stat() --> os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=5, st_atime=1671203456, st_mtime=1670965516, st_ctime=1670965740)
modified time info.st_mtime --> 1670965516.3172512
number of characters in file info.st_size --> 5

name --> file2.csv info - entry.stat() --> os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=20, st_atime=1671203481, st_mtime=1671203481, st_ctime=1670965788)
modified time info.st_mtime --> 1671203481.8934693
number of characters in file info.st_size --> 20

name --> file3.txt info - entry.stat() --> os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=10, st_atime=1671203458, st_mtime=1671203458, st_ctime=1670965811)
modified time info.st_mtime --> 1671203458.1173935
number of characters in file info.st_size --> 10

name --> sub_dir info - entry.stat() --> os.stat_result(st_mode=16895, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0, st_atime=1670965535, st_mtime=1670965535, st_ctime=1670965440)
modified time info.st_mtime --> 1670965535.2021341
number of characters in file info.st_size --> 0 ....


os.scandir() returns a ScandirIterator object. Each entry in a ScandirIterator
object has a .stat() method that retrieves information about the file or
directory it points to. .stat() provides information such as file size and the
time of last modification. In the example above, the code prints out the
st_mtime attribute, which is the time the content of the file was last modified.

The pathlib module has corresponding methods for retrieving file information
that give the same results:"""
from pathlib import Path

current_dir = Path.home() / "my_directory/"
for path in current_dir.iterdir():
    info = path.stat()
    print(
        f"file/dir: {path.name} info.st_mtime: {info.st_mtime} \
file size: {info.st_size} characters"
    )

"""
file/dir: file1.py info.st_mtime: 1670965516.3172512 file size: 5 characters
file/dir: file2.csv info.st_mtime: 1671203481.8934693 file size: 20 characters
file/dir: file3.txt info.st_mtime: 1671203458.1173935 file size: 10 characters
file/dir: sub_dir info.st_mtime: 1670965535.2021341 file size: 0 characters
file/dir: sub_dir_b info.st_mtime: 1670965607.5616095 file size: 0 characters
file/dir: sub_dir_c info.st_mtime: 1670965694.913252 file size: 0 characters


In the example above, the code loops through the object returned by .iterdir()
and retrieves file attributes through a .stat() call for each file in the
directory list. The st_mtime attribute returns a float value that represents
seconds since the epoch. To convert the values returned by st_mtime for display
purposes, you could write a helper function to convert the seconds into a
datetime object:
"""
from datetime import datetime
from os import scandir


def convert_date(timestamp):
    date = datetime.utcfromtimestamp(timestamp)
    print(f"date --> {date}")
    formated_date = date.strftime("%Y %b %d")
    return formated_date


def get_files():
    dir_entries = scandir(Path.home() / "my_directory/")
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(
                f"file: {entry.name}\t Last Modified: \
{convert_date(info.st_mtime)}"
            )


"""
This will first get a list of files in my_directory and their attributes and
then call convert_date() to convert each file's last modified time into a
human readable form. convert_date() makes use of .strftime() to convert the
time in seconds into a string.

The arguments passed to .strftime() are the following:
Code	Example	Description
%a	Sun	Weekday as locale's abbreviated name.
%A	Sunday	Weekday as locale's full name.
%w	0	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d	08	Day of the month as a zero-padded decimal number.
%-d	8	Day of the month as a decimal number. (Platform specific)
%b	Sep	Month as locale's abbreviated name.
%B	September	Month as locale's full name.
%m	09	Month as a zero-padded decimal number.
%-m	9	Month as a decimal number. (Platform specific)
%y	13	Year without century as a zero-padded decimal number.
%Y	2013	Year with century as a decimal number.
%H	07	Hour (24-hour clock) as a zero-padded decimal number.
%-H	7	Hour (24-hour clock) as a decimal number. (Platform specific)
%I	07	Hour (12-hour clock) as a zero-padded decimal number.
%-I	7	Hour (12-hour clock) as a decimal number. (Platform specific)
%p	AM	Locale's equivalent of either AM or PM.
%M	06	Minute as a zero-padded decimal number.
%-M	6	Minute as a decimal number. (Platform specific)
%S	05	Second as a zero-padded decimal number.
%-S	5	Second as a decimal number. (Platform specific)
%f	000000	Microsecond as a decimal number, zero-padded on the left.
%z	+0000	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the
                object is naive).
%Z	UTC	Time zone name (empty string if the object is naive).
%j	251	Day of the year as a zero-padded decimal number.
%-j	251	Day of the year as a decimal number. (Platform specific)
%U	36	Week number of the year (Sunday as the first day of the week) as
                a zero padded decimal number. All days in a new year preceding
                the first Sunday are considered to be in week 0.
%W	35	Week number of the year (Monday as the first day of the week) as
                a decimal number. All days in a new year preceding the first
                Monday are considered to be in week 0.
%c	Sun Sep 8 07:06:05 2013	Locale's appropriate date and time representation.
%x	09/08/13	Locale's appropriate date representation.
%X	07:06:05	Locale's appropriate time representation.
%%	%	A literal '%' character.
"""
# Together, these directives produce output that looks like this:
get_files()
"""
date --> 2022-12-13 21:05:16.317251
file: file1.py	 Last Modified: 2022 Dec 13
date --> 2022-12-16 15:11:21.893469
file: file2.csv	 Last Modified: 2022 Dec 16
date --> 2022-12-16 15:10:58.117393
file: file3.txt	 Last Modified: 2022 Dec 16

The syntax for converting dates and times into strings can be quite confusing.
To read more about it, check out the official documentation on it. Another
handy reference that is easy to remember is http://strftime.org/ .


Making Directories
Sooner or later, the programs you write will have to create directories in
order to store data in them. os and pathlib include functions for creating
directories. We'll consider these:

Function	        Description
os.mkdir()	        Creates a single subdirectory
pathlib.Path.mkdir()	Creates single or multiple directories
os.makedirs()	        Creates multiple directories, including intermediate
                        directories
Creating a Single Directory
To create a single directory, pass a path to the directory as a parameter to
os.mkdir():
import os
os.mkdir(Path.home() / "example_directory/")

If a directory already exists, os.mkdir() raises FileExistsError. Alternatively,
you can create a directory using pathlib:
from pathlib import Path

p = Path('example_directory/')
p.mkdir()
If the path already exists, mkdir() raises a FileExistsError:

>>> p.mkdir()
Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
  File '/usr/lib/python3.5/pathlib.py', line 1214, in mkdir
    self._accessor.mkdir(self, mode)
  File '/usr/lib/python3.5/pathlib.py', line 371, in wrapped
    return strfunc(str(pathobj), *args)
FileExistsError: [Errno 17] File exists: '.'
[Errno 17] File exists: '.'
To avoid errors like this, catch the error when it happens and let your user
know:
"""
from pathlib import Path

p = Path.home() / "example_directory/"
try:
    p.mkdir()
except FileExistsError as exc:
    print(f"\n*** Directory ALREADY EXIST: {exc}")

# Alternatively, you can ignore the FileExistsError by passing the exist_ok=True
# argument to .mkdir() method:
from pathlib import Path

p = Path.home() / "example_directory"
p.mkdir(exist_ok=True)
# This will not raise an error if the directory already exist. all preivous
# content in the directory remain the same.

"""
Creating Multiple Directories
os.makedirs() is similar to os.mkdir(). The difference between the two is that
not only can os.makedirs() create individual directories, it can also be used
to create directory trees. In other words, it can create any necessary
intermediate folders in order to ensure a full path exists.

os.makedirs() is similar to running mkdir -p in Bash. For example, to create a
group of directories like 2018/10/05, all you have to do is the following:

import os

os.makedirs(Path.home() / 'my_directory/2018/10/05')
This will create a nested directory structure that contains the folders 2018,
10, and 05:

.
|
└── 2018/
    └── 10/
        └── 05/
.makedirs() creates directories with default permissions. If you need to create
directories with different permissions call .makedirs() and pass in the mode you
would like the directories to be created in:
import os

os.makedirs('2018/10/05', mode=0o770)
This creates the 2018/10/05 directory structure and gives the owner and group
users read, write, and execute permissions. The default mode is 0o777, and the
file permission bits of existing parent directories are not changed. For more
details on file permissions, and how the mode is applied, see the
docs https://docs.python.org/3/library/os.html#os.makedirs.

Run tree to confirm that the right permissions were applied (Linux):
$ tree -p -i .
.
[drwxrwx---]  2018
[drwxrwx---]  10
[drwxrwx---]  05
This prints out a directory tree of the current directory. tree is normally
used to list contents of directories in a tree-like format. Passing the -p and
-i arguments to it prints out the directory names and their file permission
information in a vertical list. -p prints out the file permissions, and -i
makes tree produce a vertical list without indentation lines.

As you can see, all of the directories have 770 permissions. An alternative way
to create directories is to use .mkdir() from pathlib.Path:"""
import pathlib

p = pathlib.Path.home() / "my_directory/2022/12/16"
p.mkdir(parents=True, exist_ok=True)

"""
Passing parents=True to Path.mkdir() makes it create the directory 05 and any
parent directories necessary to make the path valid.

By default, os.makedirs() and Path.mkdir() raise an OSError if the target
directory already exists. This behavior can be overridden (as of Python 3.2)
by passing exist_ok=True as a keyword argument when calling each function.

Running the code above produces a directory structure like the one below in
one go:

.
|
└── 2018/
    └── 10/
        └── 05/
I prefer using pathlib when creating directories because I can use the same
function to create single or nested directories.


Filename Pattern Matching:
After getting a list of files in a directory using one of the methods above,
you will most probably want to search for files that match a particular pattern.

These are the methods and functions available to you:

endswith() and startswith() string methods
fnmatch.fnmatch()
glob.glob()
pathlib.Path.glob()
Each of these is discussed below. The examples in this section will be performed on a directory called some_directory that has the following structure:

.
|
├── sub_dir/
|   ├── file1.py
|   └── file2.py
|
├── admin.py
├── data_01_backup.txt
├── data_01.txt
├── data_02_backup.txt
├── data_02.txt
├── data_03_backup.txt
├── data_03.txt
└── tests.py
If you're following along using a Bash shell, you can create the above directory
structure using the following commands:
In Linux:
$ mkdir some_directory
$ cd some_directory/
$ mkdir sub_dir
$ touch sub_dir/file1.py sub_dir/file2.py
$ touch data_{01..03}.txt data_{01..03}_backup.txt admin.py tests.py
"""
basepath = Path.home() / "some_directory/"
basepath.mkdir(exist_ok=True)
sub_dir = basepath / "sub_dir/"
sub_dir.mkdir(exist_ok=True)
path_file_to_create = sub_dir / "file1.py"
path_file_to_create.touch()

path_file_to_create = sub_dir / "file2.py"
path_file_to_create.touch()

path_file_to_create = basepath / "data_01.txt"
path_file_to_create.touch()
path_file_to_create = basepath / "data_02.txt"
path_file_to_create.touch()
path_file_to_create = basepath / "data_03.txt"
path_file_to_create.touch()

path_file_to_create = basepath / "data_01_backup.txt"
path_file_to_create.touch()
path_file_to_create = basepath / "data_02_backup.txt"
path_file_to_create.touch()
path_file_to_create = basepath / "data_03_backup.txt"
path_file_to_create.touch()

path_file_to_create = basepath / "admin.py"
path_file_to_create.touch()

path_file_to_create = basepath / "tests.py"
path_file_to_create.touch()

"""
This will create the some_directory/ directory, change into it, and then create
sub_dir. The next line creates file1.py and file2.py in sub_dir, and the last
line creates all the other files using expansion. To learn more about shell
expansion, visit this site.


Using String Methods:
Python has several built-in methods for modifying and manipulating strings. Two
of these methods, .startswith() and .endswith(), are useful when you're
searching for patterns in filenames. To do this, first get a directory listing
and then iterate over it:
"""
import os

# Get .txt files:
for file_name in os.listdir(basepath):
    if file_name.endswith(".txt"):
        print(f"file ending with .txt --> {file_name}")
""" The code above finds all the files in some_directory/, iterates over them
and uses .endswith() to print out the filenames that have the .txt file
extension. Running this on my computer produces the following output:
file ending with .txt --> data_01.txt
file ending with .txt --> data_01_backup.txt
file ending with .txt --> data_02.txt
file ending with .txt --> data_02_backup.txt
file ending with .txt --> data_03.txt
file ending with .txt --> data_03_backup.txt
"""

# Get files starting with 'data':
for file_name in os.listdir(basepath):
    if file_name.startswith("data"):
        print(f"file starting with 'data' --> {file_name}")
"""
file ending with .txt --> data_03_backup.txt
file starting with 'data' --> data_01.txt
file starting with 'data' --> data_01_backup.txt
file starting with 'data' --> data_02.txt
file starting with 'data' --> data_02_backup.txt
file starting with 'data' --> data_03.txt
file starting with 'data' --> data_03_backup.txt



Simple Filename Pattern Matching Using fnmatch:
String methods are limited in their matching abilities. fnmatch has more
advanced functions and methods for pattern matching. We will consider
fnmatch.fnmatch(), a function that supports the use of wildcards such as * and
? to match filenames. For example, in order to find all .txt files in a
directory using fnmatch, you would do the following:"""
import os
import fnmatch

for file_name in os.listdir(basepath):
    if fnmatch.fnmatch(file_name, "*.py"):
        print(f"all file with .py extension --> {file_name}")
"""
all file with .py extension --> admin.py
all file with .py extension --> tests.py
This iterates over the list of files in some_directory and uses .fnmatch() to
perform a wildcard search for files that have the .py extension.


More Advanced Pattern Matching:
Let's suppose you want to find .txt files that meet certain criteria. For
example, you could be only interested in finding .txt files that contain the
word data, a number between a set of underscores, and the word backup in their
filename. Something similar to data_01_backup, data_02_backup, or
data_03_backup.
Using fnmatch.fnmatch(), you could do it this way:
"""
for file_name in os.listdir(basepath):
    if fnmatch.fnmatch(file_name, "data_*_backup.txt"):
        print(f"file that match 'data_*_backup.txt' --> {file_name}")

""" Here, you print only the names of files that match the data_*_backup.txt
pattern. The asterisk in the pattern will match any character, so running this
will find all text files whose filenames start with the word data and end in
backup.txt, as you can see from the output below:
file that match 'data_*_backup.txt' --> data_01_backup.txt
file that match 'data_*_backup.txt' --> data_02_backup.txt
file that match 'data_*_backup.txt' --> data_03_backup.txt


Filename Pattern Matching Using glob:
Another useful module for pattern matching is glob.
.glob() in the glob module works just like fnmatch.fnmatch(), but unlike
fnmatch.fnmatch(), it treats files beginning with a period (.) as special.

UNIX and related systems translate name patterns with wildcards like ? and *
into a list of files. This is called globbing.
For example, typing mv *.py python_files/ in a UNIX shell moves (mv) all files
with the .py extension from the current directory to the directory
python_files. The * character is a wildcard that means “any number of characters
,” and *.py is the glob pattern. This shell capability is not available in the
Windows Operating System. The glob module adds this capability in Python,
which enables Windows programs to use this feature.

Here's an example of how to use glob to search for all Python (.py) source files
in the current directory:"""
import glob

basepath
print(glob.glob("*.py"))

"""
LIST: ['cha12-01_Files_FileSystem_DirectoryFolder.py',
'cha12-05_Reading_And_Writing_Files.py',
'cha12-06_Reading_And_Writing_CSV_Files.py',
'cha12-08_Additonal_ResourcesReading_And_Writing_Files.py',
'cha12-09_Additonal_ResourcesReading_And_Writing_Files.py']
glob.glob('*.py') searches for all files that have the .py extension in the
current directory and RETURNS them as a LIST. glob also supports shell-style
wildcards to match patterns:"""
import glob

for name in glob.glob("c:/users/ssshh/some_directory/*[0-9]*.txt"):
    print(f"name for .glob(*[0-9]*.txt) --> {name}")
"""
name for .glob(*[0-9]*.txt) --> c:/users/ssshh/some_directory\data_01.txt
name for .glob(*[0-9]*.txt) --> c:/users/ssshh/some_directory\data_01_backup.txt
name for .glob(*[0-9]*.txt) --> c:/users/ssshh/some_directory\data_02.txt
name for .glob(*[0-9]*.txt) --> c:/users/ssshh/some_directory\data_02_backup.txt
name for .glob(*[0-9]*.txt) --> c:/users/ssshh/some_directory\data_03.txt
name for .glob(*[0-9]*.txt) --> c:/users/ssshh/some_directory\data_03_backup.txt

glob makes it easy to search for files recursively in subdirectories too:"""
import glob

for file in glob.iglob("c:/users/ssshh/some_directory/**/*.py", recursive=True):
    print(f" recursive file ..> {file}")
"""
This example makes use of glob.iglob() to search for .py files in the current
directory and subdirectories. Passing recursive=True as an argument to .iglob()
makes it search for .py files in the current directory and any subdirectories.
The difference between glob.iglob() and glob.glob() is that .iglob() returns
an iterator instead of a list.

Running the program above produces the following:
c:/users/ssshh/some_directory\admin.py
c:/users/ssshh/some_directory\tests.py
c:/users/ssshh/some_directory\sub_dir\file1.py
c:/users/ssshh/some_directory\sub_dir\file2.py

pathlib contains similar methods for making flexible file listings. The example
below shows how you can use .Path.glob() to list file types that start with
the letter p:"""
from pathlib import Path

p = Path("c:/users/ssshh/some_directory/")
for name in p.glob("*.p*"):
    print(name)

"""
c:/users\\ssshh\\some_directory\admin.py
c:/users\\ssshh\\some_directory\tests.ppy
c:/users\\ssshh\\some_directory\tests.py
Calling p.glob('*.p*') returns a generator object that points to all files in the current directory that start with the letter p in their file extension.

Path.glob() is similar to os.glob() discussed above. As you can see, pathlib
combines many of the best features of the os, os.path, and glob modules into
one single module, which makes it a joy to use."""

# to recap, here is a table of the functions we have covered in this section:
"""
Function	Description
startswith()	Tests if a string starts with a specified pattern and returns
                True or False
endswith()	Tests if a string ends with a specified pattern and returns True
                or False
fnmatch.fnmatch(filename, pattern)	Tests whether the filename matches the
                pattern and returns True or False
glob.glob()	Returns a list of filenames that match a pattern
pathlib.Path.glob()	Finds patterns in path names and returns a generator
                object.            
"""

# Traversing Directories and Processing Files
""" A common programming task is walking a directory tree and processing files
in the tree. Let's explore how the built-in Python function os.walk() can be
used to do this. os.walk() is used to generate filename in a directory tree by
walking the tree either top-down or bottom-up. For the purposes of this section,
we'll be manipulating the following directory tree:
my_directory_02/
|
├── folder_1/
|   ├── file1.py
|   ├── file2.py
|   └── file3.py
|
├── folder_2/
|   ├── file4.py
|   ├── file5.py
|   └── file6.py
|
├── test1.txt
└── test2.txt   """
from pathlib import Path

top_path = Path.home() / "my_directory_02"
top_path.mkdir(exist_ok=True)
file_to_create = top_path / "test1.txt"
file_to_create.touch()
file_to_create = top_path / "test2.txt"
file_to_create.touch()

folder_1 = top_path / "folder_1"
folder_1.mkdir(exist_ok=True)
file_to_create = folder_1 / "file1.py"
file_to_create.touch()
file_to_create = folder_1 / "file2.py"
file_to_create.touch()
file_to_create = folder_1 / "file3.py"
file_to_create.touch()


folder_2 = top_path / "folder_2"
folder_2.mkdir(exist_ok=True)
file_to_create = folder_2 / "file4.py"
file_to_create.touch()
file_to_create = folder_2 / "file5.py"
file_to_create.touch()
file_to_create = folder_2 / "file6.py"
file_to_create.touch()

# The following is an example that shows you how to list all files and
# directories in a directory tree using os.walk().
# os.walk() defaults to traversing directories in a top-down manner:
for dirpath, dirnames, files in os.walk(top_path):
    print(f"Found directory: {dirpath}")
    print(f"dirnames --> {dirnames}")
    print(f"files in folder --> {files}")
    for file_name in files:
        print(f"file_name --> {file_name}")
"""
os.walk() returns three values on EACH ITERATION of the loop:

1- The name of the current folder: C:\\Users\\ssshh\\my_directory_02
2- A list of folders in the current folder: ['folder_1', 'folder_2']
3- A list of files in the current folder: ['test1.txt', 'test2.txt']

On each iteration, it prints out the names of the subdirectories and files it
finds:
Found directory: C:\\Users\\ssshh\\my_directory_02
dirnames --> ['folder_1', 'folder_2']
files in folder --> ['test1.txt', 'test2.txt']
file_name --> test1.txt
file_name --> test2.txt
Found directory: C:\\Users\\ssshh\\my_directory_02\\folder_1
dirnames --> []
files in folder --> ['file1.py', 'file2.py', 'file3.py']
file_name --> file1.py
file_name --> file2.py
file_name --> file3.py
Found directory: C:\\Users\\ssshh\\my_directory_02\\folder_2
dirnames --> []
files in folder --> ['file4.py', 'file5.py', 'file6.py']
file_name --> file4.py
file_name --> file5.py
file_name --> file6.py
"""

print("\n\n")
# To traverse the directory tree in a bottom-up manner, pass in a topdown=False
# keyword argument to os.walk():
for dirpath, dirnames, files in os.walk(top_path, topdown=False):
    print(f"Found directory: {dirpath}")
    print(f"dirnames --> {dirnames}")
    print(f"files in folder --> {files}")
    for file_name in files:
        print(f"file_name --> {file_name}")
"""
Passing the topdown=False argument will make os.walk() print out the files it
finds in the subdirectories first:
Found directory: C:\\Users\\ssshh\\my_directory_02\\folder_1
dirnames --> []
files in folder --> ['file1.py', 'file2.py', 'file3.py']
file_name --> file1.py
file_name --> file2.py
file_name --> file3.py
Found directory: C:\\Users\\ssshh\\my_directory_02\\folder_2
dirnames --> []
files in folder --> ['file4.py', 'file5.py', 'file6.py']
file_name --> file4.py
file_name --> file5.py
file_name --> file6.py
Found directory: C:\\Users\\ssshh\\my_directory_02
dirnames --> ['folder_1', 'folder_2']
files in folder --> ['test1.txt', 'test2.txt']
file_name --> test1.txt
file_name --> test2.txt

As you can see, the program started by listing the contents of the
subdirectories before listing the contents of the root directory. This is very
useful in situations where you want to recursively delete files and directories.
You will learn how to do this in the sections below. By default, os.walk does
not walk down into symbolic links that resolve to directories. This behavior
can be overridden by calling it with a followlinks=True argument.


Making Temporary Files and Directories
Python provides a handy module for creating temporary files and directories
called tempfile.
tempfile can be used to open and store data temporarily in a file or directory
while your program is running. tempfile handles the deletion of the temporary
files when your program is done with them.
Here's how to create a temporary file:"""
from tempfile import TemporaryFile

# Create a temporary file and write some data to it
fp = TemporaryFile("w+t")
fp.write("Hello universe!")

# Go back to the beginning and read data from file
fp.seek(0)
data = fp.read()

# Close the file, after which it will be removed
fp.close()

"""The first step is to import TemporaryFile from the tempfile module. Next,
create a file like object using the TemporaryFile() method by calling it and
passing the mode you want to open the file in. This will create and open a
file that can be used as a temporary storage area.

In the example above, the mode is 'w+t', which makes tempfile create a temporary
text file in write mode. There is no need to give the temporary file a filename
since it will be destroyed after the script is done running.

After writing to the file, you can read from it and close it when you're done
processing it. Once the file is closed, it will be deleted from the filesystem.
If you need to name the temporary files produced using tempfile, use
tempfile.NamedTemporaryFile().

The temporary files and directories created using tempfile are stored in a
special system directory for storing temporary files. Python searches a standard
list of directories to find one that the user can create files in.

On Windows, the directories are C:\TEMP, C:\TMP, \TEMP, and \TMP, in that order.
On all other platforms, the directories are /tmp, /var/tmp, and /usr/tmp, in
that order. As a last resort, tempfile will save temporary files and directories
in the current directory.

.TemporaryFile() is also a context manager so it can be used in conjunction
with the 'with' statement. Using a context manager takes care of closing and
deleting the file automatically after it has been read:"""

with TemporaryFile("w+t") as fp:
    fp.write("Hello universe!")
    fp.seek(0)
    fp.read()
# File is now closed and removed
"""This creates a temporary file and reads data from it. As soon as the file's
contents are read, the temporary file is closed and deleted from the file
system.

tempfile can also be used to create temporary directories. Let's look at how
you can do this using tempfile.TemporaryDirectory():"""

import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    print("Created temporary directory ", tmpdir)
    os.path.exists(tmpdir)

# Created temporary directory  /tmp/tmpoxbkrm6c
# True

# Directory contents have been removed
print(f"tmpdir --> {tmpdir}")
# --> '/tmp/tmpoxbkrm6c'

print(os.path.exists(tmpdir))
# False
"""Calling tempfile.TemporaryDirectory() creates a temporary directory in the
file system and returns an object representing this directory. In the example
above, the directory is created using a context manager, and the name of the
directory is stored in tmpdir. The third line prints out the name of the
temporary directory, and os.path.exists(tmpdir) confirms if the directory was
actually created in the file system.

After the context manager goes out of context, the temporary directory is
deleted and a call to os.path.exists(tmpdir) returns False, which means that
the directory was succesfully deleted.
"""

# Deleting Files and Directories
"""You can delete single files, directories, and entire directory trees using
the methods found in the os, shutil, and pathlib modules. The following sections
describe how to delete files and directories that you no longer need.

Deleting Files in Python
To delete a single file, use pathlib.Path.unlink(), os.remove(). or os.unlink().

os.remove() and os.unlink() are semantically identical. To delete a file using
os.remove(), do the following:
"""
from pathlib import Path

top_path = Path.home() / "my_directory_03"
top_path.mkdir(exist_ok=True)
file_to_create = top_path / "test1.txt"
file_to_create.touch()
print(f"created file test1.txt ")


my_path = Path.home() / "my_directory_03"
new_file = my_path / "data.txt"
new_file.touch()
print(f"1- created file data.txt ")
# to delete a file using os.remove() function:
import os

# data_file = "C:\\users\\ssshh\\my_directory_03\\data.txt"
os.remove(new_file)
print(f"1- deleted file data.txt ")


# Deleting a file using os.unlink is similar to how you do it using os.removed():
new_file = my_path / "data.txt"
new_file.touch()
print(f"2- created file data.txt ")
os.unlink(new_file)
print(f"2- deleted file data.txt ")

""" Calling .unlink() or .remove() on a file deletes the file from the
filesystem. These two functions will throw an OSError if the path passed to
them points to a directory instead of a file. To avoid this, you can either
check that what you're trying to delete is actually a file and only delete it
if it is, or you can use exception handling to handle the OSError:"""

import os

new_file = my_path / "data.txt"
new_file.touch()
# new_file = my_path
# if the file exists, delete it:
if os.path.isfile(new_file):
    os.remove(new_file)
    print(f"3- deleted file data.txt ")
else:
    print(f"Error: {new_file} is not a valid filename")

"""os.path.isfile() checks whether data_file is actually a file. If it is, it
is deleted by the call to os.remove(). If data_file points to a folder, an
error message is printed to the console.

The following example shows how to use exception handling to handle errors when
deleting files: """
import os

file_to_delete = my_path / "data.txt"
file_to_delete.touch()
# file_to_delete = my_path

# Using exception handling to control the file delete:
try:
    os.remove(file_to_delete)
    print(f"4- deleted file data.txt ")
except OSError as excp:
    print(f"Exception_1 Error: {file_to_delete} : {excp.strerror}")
# this print: Exception Error: C:\Users\ssshh\my_directory : Access is denied
""" The code above attempts to delete the file first before checking its type.
If file_to_delete isn't actually a file, the OSError that is thrown is handled
in the except clause, and an error message is printed to the console. The error
message that gets printed out is formatted using Python f-strings.

Finally, you can also use pathlib.Path.unlink() to delete files:"""
from pathlib import Path

my_path = Path.home() / "my_directory_03"
file_to_delete = my_path / "data.txt"
file_to_delete.touch()
# file_to_delete = my_path
try:
    file_to_delete.unlink()
    # os.remove(file_to_delete)
    print(f"5- deleted file data.txt ")
except IsADirectoryError as e:
    print(f"IsADirectoryError Exception_2 Error-1: {file_to_delete} : {e.strerror}")
except PermissionError as e:
    print(f"PermissionError Exception_2 Error-2: {file_to_delete} : {e.strerror}")

except PermissionError as e:
    print(f"PermissionError Exception_2 Error: {file_to_delete} : {e.strerror}")
# -->PermissionError Exception_2 Error_2: C:\Users\ssshh\my_directory : Access is denied
""" This creates a Path object called file_to_delete that points to a file.
Calling os.remove() or Path.unlink() on data_file will delete home/data.txt. If
file_to_delete points to a directory, an IsADirectoryError is raised. It is worth
noting that the Python program above has the same permissions as the user
running it. If the user does not have permission to delete the file, a
PermissionError is raised."""


# Deleting Directories
"""The standard library offers the following functions for deleting directories:
os.rmdir()
pathlib.Path.rmdir()
shutil.rmtree()
To delete a single directory or folder, use os.rmdir() or pathlib.rmdir().
These two functions only work if the directory you're trying to delete is empty.
If the directory isn't empty, an OSError is raised. Here is how to delete a
folder: """
import os
from pathlib import Path

my_home_path = Path.home()
trash_dir = my_home_path / "my_directory_03/bad_dir"
trash_dir.mkdir(exist_ok=True)
# file = trash_dir / "file.txt"  # to create the file
# file.touch()  # create the file
try:
    os.rmdir(trash_dir)
    print(f"1- Successful deleted the trash_dir")
except OSError as e:
    print(f"1- DeleteDir OSError: {trash_dir} : {e.strerror}")
# Here, the trash_dir directory is deleted by passing its path to os.rmdir(). If the
# directory isn't empty, an error message is printed to the screen:
# When the trash_dir is not empty --> DeleteDir OSError: C:\Users\ssshh\bad_dir : The
#                                     directory is not empty

# Alternatively, you can use pathlib to delete directories:
my_home_path = Path.home()
trash_dir = my_home_path / "my_directory_03/bad_dir"
trash_dir.mkdir(exist_ok=True)
# file = trash_dir / "file.txt"  # to create the file
# file.touch()  # create the file
try:
    trash_dir.rmdir()
    print(f"2-Successful deleted the trash_dir")
except OSError as e:
    print(f"2-DeleteDir OSError: {trash_dir} : {e.strerror}")
# Here, you create a Path object that points to the directory to be deleted.
# Calling .rmdir() on the Path object will delete it if it is empty.


# Deleting Entire Directory Trees:
# To delete non-empty directories and entire directory trees, Python offers
# shutil.rmtree():
import shutil

trash_dir2 = my_home_path / "my_directory_03/bad_dir"
trash_dir2.mkdir(exist_ok=True)
print(f"** trash_dir2 --> {trash_dir2}")
file = trash_dir2 / "file2.txt"  # to create the file
file.touch()  # create the file
try:
    shutil.rmtree(trash_dir2)
    print(f"directory successfuly deleted with shutil.rmtree()")
except OSError as e:
    print(f"shutil.rmtree Error: {trash_dir2} : {e.strerror}")

"""Everything in trash_dir is deleted when shutil.rmtree() is called on it.
There may be cases where you want to delete empty folders recursively. You can
do this using one of the methods discussed above in conjunction with os.walk():
"""
# Getting ready:
# Traversing Directories and Deleting Files and then Directories
""" Aside from te shutil.rmtree() below is only for the coding exercise purpose,
because we can better use the shutil.rmtree().
below code is walking a directory tree and deleting files and then directories
in the tree. Let's explore how the built-in Python function os.walk() can be
used to do this. os.walk() is used to generate filename in a directory tree by
walking the tree either top-down or bottom-up. For the purposes of this section,
we'll be manipulating the following directory tree:
my_directory_04/
|
├── folder_3/
|   ├── file1.py
|   ├── file2.py
|   └── file3.py
|
├── folder_4/
|   ├── file4.py
|   ├── file5.py
|   └── file6.py
|
├── test1.txt
└── test2.txt   """
from pathlib import Path

top_path = Path.home() / "my_directory_04"
top_path.mkdir(exist_ok=True)
file_to_create = top_path / "test1.txt"
file_to_create.touch()
file_to_create = top_path / "test2.txt"
file_to_create.touch()

folder_1 = top_path / "folder_3"
folder_1.mkdir(exist_ok=True)
file_to_create = folder_1 / "file1.py"
file_to_create.touch()
file_to_create = folder_1 / "file2.py"
file_to_create.touch()
file_to_create = folder_1 / "file3.py"
file_to_create.touch()


folder_2 = top_path / "folder_4"
folder_2.mkdir(exist_ok=True)
file_to_create = folder_2 / "file4.py"
file_to_create.touch()
file_to_create = folder_2 / "file5.py"
file_to_create.touch()
file_to_create = folder_2 / "file6.py"
file_to_create.touch()

# The following is an example that shows you how to delete all files and then
# all sub-directories in and top directory tree using os.walk().
# os.walk() defaults to traversing directories in a top-down manner:
import os

for dirpath_2, dirnames_2, files_2 in os.walk(top_path, topdown=False):
    print(f"*** --> Found directory: {dirpath_2}")
    print(f"dirnames_2 --> {dirnames_2}")
    print(f"files_2 in folder --> {files_2}")
    for file_name in files_2:  # Loop to delete all files in folder
        try:
            file_to_delete = Path(dirpath_2) / file_name
            # os.remove(file_to_delete)  #  delete the file.
            file_to_delete.unlink()  #  delete the file.
            print(f"Deleted file_name --> {file_to_delete}")
        except OSError as excpt_1:
            print(f"Deleting file: {file_to_delete} : {excpt_1.strerror}")

    # after deleting all files, delete the empty directory:
    try:
        os.rmdir(dirpath_2)
        print(f"Deleting directory: {dirpath_2}")
    except OSError as excpt_2:
        print(f"Deleting directory: {dirpath_2} : {excpt_2.strerror}")

"""
*** --> Found directory: C:/Users/ssshh/my_directory_04/folder_3
dirnames_2 --> []
files_2 in folder --> ['file1.py', 'file2.py', 'file3.py']
Deleted file_name --> C:/Users/ssshh/my_directory_04/folder_3/file1.py
Deleted file_name --> C:/Users/ssshh/my_directory_04/folder_3/file2.py
Deleted file_name --> C:/Users/ssshh/my_directory_04/folder_3/file3.py
Deleting directory: C:/Users/ssshh/my_directory_04/folder_3
*** --> Found directory: C:/Users/ssshh/my_directory_04/folder_4
dirnames_2 --> []
files_2 in folder --> ['file4.py', 'file5.py', 'file6.py']
Deleted file_name --> C:/Users/ssshh/my_directory_04/folder_4/file4.py
Deleted file_name --> C:/Users/ssshh/my_directory_04/folder_4/file5.py
Deleted file_name --> C:/Users/ssshh/my_directory_04/folder_4/file6.py
Deleting directory: C:/Users/ssshh/my_directory_04/folder_4
*** --> Found directory: C:/Users/ssshh/my_directory_04
dirnames_2 --> ['folder_3', 'folder_4']
files_2 in folder --> ['test1.txt', 'test2.txt']
Deleted file_name --> C:/Users/ssshh/my_directory_04/test1.txt
Deleted file_name --> C:/Users/ssshh/my_directory_04/test2.txt
Deleting directory: C:/Users/ssshh/my_directory_04
>>>

 The table below lists the functions covered in this section:

Function	Description
--------        -----------------------------------------------------
os.remove()	With Path, Deletes a file and does not delete directories
os.unlink()	With Path, Is identical to os.remove() and deletes a single file
pathlib.Path.unlink()	With Path, Deletes a file and cannot delete directories
os.rmdir()	With dirName, Deletes an empty directory
pathlib.Path.rmdir()	Deletes an empty directory
shutil.rmtree()	With dirPaht, Deletes entire directory tree and can be used to
                delete non-empty directories
"""


# Copying, Moving, and Renaming Files and Directories
"""
Python ships with the shutil module. shutil is short for shell utilities. It
provides a number of high-level operations on files to support copying,
archiving, and removal of files and directories. In this section, you'll learn
how to move and copy files and directories.

Copying Files in Python
shutil offers a couple of functions for copying files. The most commonly used
functions are shutil.copy() and shutil.copy2(). To copy a file from one location
to another using shutil.copy(), do the following:"""
import shutil
from pathlib import Path

dest_dir = Path.home() / "my_directory_05/to/dest_dir"
dest_dir.mkdir(exist_ok=True, parents=True)
src = Path.home() / "my_directory_05/to/file_to_copy.txt"
shutil.copy(src, dest_dir)  # top copy to a directory.
print(f"copied file {src.name} to directory {dest_dir.name}")

dest_file = dest_dir / "second_file.txt"
shutil.copy(src, dest_file)  # to copy to a file.
print(f"copied file {src.name} to file {dest_file.name}")

"""shutil.copy() is comparable to the cp command in UNIX based systems.
shutil.copy(src, dst) will copy the file src to the location specified in dst.
If dst is a file, the contents of that file are replaced with the contents of
src. If dst is a directory, then src will be copied into that directory.
shutil.copy() only copies the file's contents and the file's permissions.
Other metadata like the file's creation and modification times are not preserved
.

To preserve all file metadata when copying, use shutil.copy2():
"""
src2 = Path.home() / "my_directory_05/to/file_to_copy_2.txt"
shutil.copy2(src2, dest_dir)  #  to copy all the metadata of the source file.
print(f"copied file {src2.name} to directory {dest_dir.name}")

# Using .copy2() preserves details about the file such as last access time,
# permission bits, last modification time, and flags.


# Copying Directories
"""
While shutil.copy() only copies a single file, shutil.copytree() will copy an
entire directory and everything contained in it. shutil.copytree(src, dest)
takes two arguments: a source directory and the destination directory where
files and folders will be copied to.

Here's an example of how to copy the contents of one folder to a different
location:   """
import shutil

src_dir = Path.home() / "my_directory_05/to"
dest_dir2 = Path.home() / "my_directory_05/backup_01"
try:
    shutil.copytree(src_dir, dest_dir2)
    print(f"made a backup of {src_dir} into {dest_dir2}")
except OSError as e:
    print(f"FileExistsError for {dest_dir2} : {e.strerror}")
# In this example, .copytree() copies the contents of src_dir to a new location
# dest_dir2 and returns the destination directory. The destination directory
# must not already exist. It will be created as well as missing parent
# directories. shutil.copytree() is a good way to back up your files.

# To avoid the OSError when running the again next delete the backup_01 directory:
try:
    shutil.rmtree(dest_dir2)
    print(f"{dest_dir2} directory successfuly deleted with shutil.rmtree()")
except OSError as e:
    print(f"shutil.rmtree Error: {dest_dir2} : {e.strerror}")


# Moving Files and Directories
"""To move a file or directory to another location, use shutil.move(src, dst).
src is the file or directory to be moved and dst is the destination:"""
import shutil

# Moving a file to a directory:
src_file = Path.home() / "my_directory_05/to/file_to_move.txt"
dest_dir_path = Path.home() / "my_directory_05/to/dest_dir/"
try:
    shutil.move(src_file, dest_dir_path)
    print(f"Moved file {src_file.name} to directory {dest_dir_path.name}")
except shutil.Error as e:
    print(f"shutil.Error moving file {src_file.name} : {e.strerror}")
# The file is only moved if it is not EXISTS in the destination directory.
# if the file already exist in the destination directory, the an shutil.error
# File already exist will be generated, this is why the next reversal:
# Reversing the file move:
src_file = Path.home() / "my_directory_05/to/dest_dir/file_to_move.txt"
dest_dir_path = Path.home() / "my_directory_05/to/"
try:
    shutil.move(src_file, dest_dir_path)
    print(f"Moved file {src_file.name} to directory {dest_dir_path.name}")
except shutil.Error as e:
    print(f"shutil.Error moving file {src_file.name} : {e.strerror}")
# Another way to accomplish the above file moving:
src_file = Path.home() / "my_directory_05/to/file_to_move.txt"
dest_dir_path = Path.home() / "my_directory_05/to/dest_dir/"
checking_file = dest_dir_path / src_file.name
if checking_file.exists():
    print(f"Not moved, file ALREADY Exists in dest dire, {checking_file.name}")
else:
    shutil.move(src_file, dest_dir_path)
    print(f"Moved-2 file {src_file.name} to directory {dest_dir_path.name}")
# now the reversal:
src_file = Path.home() / "my_directory_05/to/dest_dir/file_to_move.txt"
dest_dir_path = Path.home() / "my_directory_05/to/"
checking_file = dest_dir_path / src_file.name
if checking_file.exists():
    print(f"Not moved, file ALREADY Exists in dest dire, {checking_file.name}")
else:
    shutil.move(src_file, dest_dir_path)
    print(f"Moved-2 file {src_file.name} to directory {dest_dir_path.name}")

# Moving directories:
src_dir = Path.home() / "my_directory_05/to/dir_to_move/"
backup_dir = Path.home() / "my_directory_05/to/backup_test_dir/"
try:
    shutil.move(src_dir, backup_dir)
    print(f"directory {src_dir.name} moved to backup dir {backup_dir.name}")
except FileNotFoundError as e:
    print(
        f"FileNotfoundError for source directory {src_dir.name} \
: {e.strerror}"
    )
# No reversing the process:
src_dir = Path.home() / "my_directory_05/to/backup_test_dir/dir_to_move/"
backup_dir = Path.home() / "my_directory_05/to/"
try:
    shutil.move(src_dir, backup_dir)
    print(f"directory-2 {src_dir.name} moved to directory '{backup_dir.name}'")
except FileNotFoundError as e:
    print(
        f"FileNotfoundError-2 for source directory {src_dir.name} \
: {e.strerror}"
    )

# shutil.move(src, dest) moves src dir into/under the dest dir if the 'dest'
# directory exists. If 'dest' direc does not exist, 'src' directory will be
# renamed to 'dest'.


# Renaming Files and Directories
# Python includes os.rename(src, dst) for renaming files and directories:
# Rename file:
import os

src = Path.home() / "my_directory_05/to/file_to_rename.txt"
dest = Path.home() / "my_directory_05/to/renamed_file.txt"
os.rename(src, dest)
# reversing the rename:
os.rename(dest, src)

# The line above will rename the file 'src' to 'dest'. If the destination path
# points to a directory, it will raise an OSError.
# Another way to rename files or directories is to use rename() from the pathlib
# module:
from pathlib import Path

file_to_rename = Path("C:/Users/ssshh/my_directory_05/to/file_to_rename.txt")
file_to_rename.rename("C:/Users/ssshh/my_directory_05/to/new_file_name.txt")

# To rename files using pathlib, you first create a pathlib.Path() object that
# contains a path to the file you want to replace. The next step is to call
# rename() on the path object and pass a new filename for the file or directory
# you're renaming.

# reverse the rename:
file_to_reverse = Path("C:/Users/ssshh/my_directory_05/to/new_file_name.txt")
file_to_reverse.rename("C:/Users/ssshh/my_directory_05/to/file_to_rename.txt")


# Creating Zip Archives -- ARCHIVING:
"""Archiving
Archives are a convenient way to package several files into one. The two most
common archive types are ZIP and TAR. The Python programs you write can create,
read, and extract data from archives. You will learn how to read and write to
both archive formats in this section.

The zipfile module is a low level module that is part of the Python Standard
Library. zipfile has functions that make it easy to open and extract ZIP files.
To read the contents of a ZIP file, the first thing to do is to create a
ZipFile object. ZipFile objects are similar to file objects created using
open(). ZipFile is also a context manager and therefore supports the with
statement:

import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
Here, you create a ZipFile object, passing in the name of the ZIP file to open
in read mode. After opening a ZIP file, information about the archive can be
accessed through functions provided by the zipfile module. The data.zip
archive in the example above was created from a directory named data that
contains a total of 5 files and 1 subdirectory:
.
|
├── sub_dir/
|   ├── bar.py
|   └── foo.py
|
├── file1.py
├── file2.py
└── file3.py
"""

import os
import zipfile
from pathlib import Path

dir_to_zip = Path.home() / "my_directory_06/data/"
print(f"List of files in dir: {os.listdir(dir_to_zip)}")

# To create the list of all the files, subdirectories and subdir files in the
# directory to zip:
files_dirs_list = []

dir_to_zip_path = Path.home() / "my_directory_06/data/"
zipped_dir_path = Path.home() / "my_directory_06/"  #  zip in highier level dir.
for entry in dir_to_zip_path.iterdir():
    if entry.is_file():
        print(f"file --> {dir_to_zip_path / entry.name}")
        files_dirs_list.append(dir_to_zip_path / entry.name)
    else:
        sub_dir = entry.name
        files_dirs_list.append(dir_to_zip_path / sub_dir)
        print(f"sub directory --> {dir_to_zip_path / sub_dir}")

        for entry_subdir in entry.iterdir():
            if entry_subdir.is_file():
                files_dirs_list.append(dir_to_zip_path / sub_dir / entry_subdir.name)
                print(
                    f"file_sub_dir --> {dir_to_zip_path / sub_dir / entry_subdir.name}"
                )
            else:
                pass
print(f"files_dirs_list --> {files_dirs_list}")

zipped_file_path = zipped_dir_path / "file_zipped.zip"

with zipfile.ZipFile(zipped_file_path, "w") as new_zip:
    for name in files_dirs_list:
        new_zip.write(name)

"""In the example, new_zip is opened in write mode and each file in file_list
is added to the archive. When the with statement suite is finished, new_zip is
closed. Opening a ZIP file in write mode erases the contents of the archive and
creates a new archive. """

# Creating archive with password protection:
pwd_zipped_file_path = zipped_dir_path / "pwd_file_zipped.zip"

with zipfile.ZipFile(pwd_zipped_file_path, "w") as new_pwd_zip:
    for name in files_dirs_list:
        new_pwd_zip.write(name)
        new_pwd_zip.pwd = b"Password@1"  # Indicating the password

# To add files, from another directory, to an existing archive, open a ZipFile
# object in append mode and then add the files:
new_dir_to_zip_path_2 = Path.home() / "my_directory_02/"
with zipfile.ZipFile(zipped_file_path, "a") as to_append_zip:
    file_to_append = new_dir_to_zip_path_2 / "file_append_01.txt"
    to_append_zip.write(file_to_append)
    file_to_append = new_dir_to_zip_path_2 / "file3_to_append.py"
    to_append_zip.write(file_to_append)

"""
Here, you open the new.zip archive you created in the previous example in
append mode. Opening the ZipFile object in append mode allows you to add
new files to the ZIP file without deleting its current contents. After adding
files to the ZIP file, the with statement goes out of context and closes the
ZIP file."""

# Reading Zip files:
# To get alist of files in the archive, call the namelist() function on the
# ZipFile object:
import zipfile

with zipfile.ZipFile(zipped_file_path, "r") as zip_file_obj:
    print(f" ** zip_file_obj.namelist() --> {zip_file_obj.namelist()}")
# Output:
#  ** zip_file_obj.namelist() --> ['Users/ssshh/my_directory_06/data/file1.py',
#'Users/ssshh/my_directory_06/data/file2.py', 'Users/ssshh/my_directory_06/data
# /file3.py', 'Users/ssshh/my_directory_06/data/sub_dir/',
#'Users/ssshh/my_directory_06/data/sub_dir/bar.py',
#'Users/ssshh/my_directory_06/data/sub_dir/foo.py',
#'Users/ssshh/my_directory_02/file_append_01.txt',
#'Users/ssshh/my_directory_02/file3_to_append.py']

# The fucntion .namelist() returns a list of names of the files and directories
# in the archive. To retrieve information about the files in the archive, use
# the .getinfo() function:
import zipfile

with zipfile.ZipFile(zipped_file_path, "r") as zip_file_obj:
    bar_file_info = zip_file_obj.getinfo(
        "Users/ssshh/my_directory_06/data/sub_dir/bar.py"
    )
    print(f"bar_file_info.file_size --> {bar_file_info.file_size}")
    print(f"bar_file_info.filename --> {bar_file_info.filename}")
    print(f"bar_file_info --> {bar_file_info}")
    print(f"bar_file_info.date_time --> {bar_file_info.date_time}")  # modified
    print(f"bar_file_info.compress_size --> {bar_file_info.compress_size}")
# Output:
# bar_file_info.file_size --> 2885
# bar_file_info.filename --> Users/ssshh/my_directory_06/data/sub_dir/bar.py
# bar_file_info --> <ZipInfo filename='Users/ssshh/my_directory_06/data/sub_dir/
# bar.py' filemode='-rw-rw-rw-' file_size=2885>
# bar_file_info.date_time --> (2021, 6, 17, 16, 10, 32)
# bar_file_info.compress_size --> 2885
""" .getinfo() returns a ZipInfo object that stores information about a single
member of the archive. To get information about a file in the archive, you pass
its path as an argument to .getinfo(). Using getinfo(), you're able to retrieve
information about archive members such as the date the files were last modified,
their compressed sizes, and their full filenames. Accessing .file_size retrieves
the file's original size in bytes.

The following example shows how to retrieve more details about archived files
in a Python REPL. Assume that the zipfile module has been imported and bar_info
is the same object you created in previous examples:
>>> bar_info.date_time
(2018, 10, 7, 23, 30, 10)
>>> bar_info.compress_size
2856
>>> bar_info.filename
'sub_dir/bar.py'
bar_info contains details about bar.py such as its size when compressed and
its full path.

The first line shows how to retrieve a file's last modified date. The next line
shows how to get the size of the file after compression. The last line shows
the full path of bar.py in the archive.

ZipFile supports the context manager protocol, which is why you're able to use
it with the with statement. Doing this automatically closes the ZipFile object
after you're done with it. Trying to open or extract files from a closed ZipFile
object will result in an error.
"""

# Extracting ZIP Archives:
"""The zipfile module allows you to extract one or more files from ZIP archives
through .extract() and .extractall().

These methods extract files to the current directory by default. They both take
an optional path parameter that allows you to specify a different directory to
extract files to. If the directory does not exist, it is automatically created.
And if it exists then overwrite it.
To extract files from the archive, do the following:"""
import zipfile
import os

print(f"os.listdir(zipped_dir_path) --> {os.listdir(zipped_dir_path)}")
# os.listdir(zipped_dir_path) --> ['data', 'file_zipped.zip']
# 1- Open the zipped file in read mode:
# data_zip = zipfile.ZipFile(zipped_dir_path / "file_zipped.zip", "r")
data_zip = zipfile.ZipFile(zipped_file_path, "r")

# 2- Extract a single file to the current working directory which is:
# C:\PythonBasicsBookExercises\cha12\Users\ssshh\my_directory_06\data\sub_dir
# 2.0: get current working directory information
import os

current_working_dir = os.getcwd()
print(f"\ncurrent_working_dir --> {current_working_dir}")

# 2.1: extract a single file from archive/zipped file:
data_zip.extract("Users/ssshh/my_directory_06/data/sub_dir/bar.py")

# 2.2: Print the listdir/content of CWD to confirm that the single file is
# included there, in this case the "Users" directory which contains the
# extracted file 'bar.py'
print(
    f"\nbar.py -os.listdir(current_working_dir) --> \
{os.listdir(current_working_dir)}"
)
"""current_working_dir --> C:\PythonBasicsBookExercises\cha12
bar.py -os.listdir(current_working_dir) -->
['cha12-01_Files_FileSystem_DirectoryFolder.py',
'cha12-05_Reading_And_Writing_Files.py',
'cha12-06_Reading_And_Writing_CSV_Files.py',
'cha12-08_Additonal_ResourcesReading_And_Writing_Files.py',
'cha12-09_Additonal_ResourcesReading_And_Writing_Files.py', 'new_file_name',
'new_file_name.txt', 'new_file_name2.txt', 'to_dir_backup', 'Users'] """
# The last directory "Users" is the one containig the extracted file.

# now change the Current Working directory to zipped_dir_path
os.chdir(zipped_dir_path)  # change cwd to the path indicated.
# extract file1.py, into the new cwd:
data_zip.extract("Users/ssshh/my_directory_06/data/file1.py")
print(
    f"\nfile1.py -os.listdir(zipped_dir_path) --> \
{os.listdir(zipped_dir_path)}"
)
"""file1.py -os.listdir(zipped_dir_path) --> ['all', 'data', 'file_zipped.zip',
'Users'] """
# The last directory "Users" is the one containig the extracted file.

# 3- Extract all the files & directories in the zipped file to the
# indicated path:
# 3.0: define the dir path receiving the whole zip file
extract_all_path = zipped_dir_path / "all"  # all is the name of the new dir
extract_one_file_path = zipped_dir_path / "one"  # one is the name of the new dir

# 3.1 Extract all files:
data_zip.extractall(path=extract_all_path)
print(
    f"\nNow with 'all' directory -os.listdir(zipped_dir_path) --> \
{os.listdir(zipped_dir_path)}"
)
# Now with 'all' directory -os.listdir(zipped_dir_path) --> ['all', 'data',
# 'file_zipped.zip', 'Users']

# extract single file file1.py, into another receiving path directory:
data_zip.extract(
    "Users/ssshh/my_directory_06/data/file1.py", path=extract_one_file_path
)
print(
    f"\nfile1.py in 'one' directory -os.listdir(extract_one_file_path) --> \
{os.listdir(extract_one_file_path)}"
)
# file1.py in 'one' directory -os.listdir(extract_one_file_path) --> ['Users']

# print the zipped_directory content, to see the new 'one' directory:
print(
    f"\nNow with 'one' directory -os.listdir(zipped_dir_path) --> \
{os.listdir(zipped_dir_path)}"
)
# Now with 'one' directory -os.listdir(zipped_dir_path) --> ['all', 'data',
# 'file_zipped.zip', 'one', 'Users']

# 3- Extract all the files & directories in the zipped file to the
# indicated path:
# 3.0: define the dir path receiving the whole zip file
extract_all_path = zipped_dir_path / "all"  # all is the name of the new dir
extract_one_file_path = zipped_dir_path / "one"  # one is the name of the new dir


# 4- Extracting Data From Password Protected Archives
""" zipfile supports extracting password protected ZIPs. To extract
password protected ZIP files, pass in the password to the .extract() or
.extractall() method as an argument:"""
# Define path of password protected zipped file
pwd_zipped_file_path = zipped_dir_path / "pwd_file_zipped.zip"

# 4.0: define the dir path receiving the password proected unzip file
unzipped_password_file_path = zipped_dir_path / "unzipped_password_dir"

# 4.1 Extract all files:
with zipfile.ZipFile(pwd_zipped_file_path, "r") as pwd_zipped:
    # extract from password protected zipped file:
    pwd_zipped.extractall(path=unzipped_password_file_path, pwd=b"Password@1")
    # password came from line 1521 where the zipped was created. b' is needed
print(
    f"\nNow with 'unzipped_password_dir' directory -os.listdir(zipped_dir_path) --> \
{os.listdir(zipped_dir_path)}"
)
"""This opens the pwd_zipped_file_path archive in read mode. A password is
supplied to .extractall(), and the archive contents are extracted to
unzipped_password_file_path. The archive is closed automatically after the
extraction is complete thanks to the with statement. """

# Conclusion
"""
You now know how to use Python to perform the most common operations on
files and groups of files. You've learned about the different built-in
modules used to read, find, and manipulate them.

You're now equipped to use Python to:

Get directory contents and file properties
Create directories and directory trees
Find patterns in filenames
Create temporary files and directories
Move, rename, copy, and delete files or directories
Read and extract data from different types of archives
Read multiple files simultaneously using fileinput """

# 2222222222
