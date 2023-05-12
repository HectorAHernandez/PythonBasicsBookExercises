# Read and Write CSV data:
"""Suppose you have a temperature sensor in your house that records the
temperature every four hours. Over the course of a day, it takes six readings.
You can store each tempeature reading as a list:
"""
temperature_readings_list = [68, 65, 68, 70, 74, 72]

# Each day the sensor generates a new list of numbers. To store these values to
# a file, you can write the values for each day on a new line in a text file and
# separate each value with a comma:
from pathlib import Path

file_path = Path.home() / "temperatures.csv"
file_path.unlink()  # delete the existing file.
with file_path.open(mode="a", encoding="utf-8") as file:
    file.write(f"\n{str(temperature_readings_list[0])}")
    for temp in temperature_readings_list[1:]:
        file.write(f",{temp}")
        print(f"type(temp) --> {type(temp)} --> {temp}")

"""This create a file in your home directory called 'temperatures.csv' and
opens it in append mode. On a new line at the end of the file, the first value
in the temperature_reading_list is written to the file. Then each remaining
value in the list is written, preceded by a comma, to the same line.
The final string text written to the file is "68, 65, 68, 70, 74, 72". You
can verify it by printing the text in the file:
"""
with file_path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    print(f"text --> {text}")
# text -->
# 68,65,68,70,74,72
# >>>
# This format is called comma-separated values, or CSV. The temperatures.csv
# file is called a CSV file.
# CSV files are a great way to store records of sequential data because you can
# RECOVER EACH ROW OF THE CSV FILE AS A LIST:
temperatures_list = text.split(",")  # .split string method create a list of
#                    strings using the separator in the string ",/!:"
print(f"temperatures_list --> {temperatures_list}")
# temperatures_list --> ['\n68', '65', '68', '70', '74', '72']

"""In section 9.2, "Lists Are Mutable Sequences" you learned how to create a
list from a string using the .split() string method. In the example above, a
new list is created from the text read from the temperatures.csv file.
The values in the temperatures_list list are strings, not integers like the
values originally written to the file. This is because VALUES READ FROM A TEXT
FILE ARE ALWAYS READ AS STRINGS. similar to values from input() function.
You can convert the strings to integers using a list comprehension statement::
"""
integer_temperatures_list = [int(temp) for temp in temperatures_list]
print(f"integer_temperatures_list --> {integer_temperatures_list}")
# int_temperatures_list --> [68, 65, 68, 70, 74, 72]
# You have now recovered the list that you originally wrote to the
# temperatures.csv file.

""" What these examples illustrate is that a CSV file is a plain text file.
Using techniques from section 12.5, "Reading And Writting Files" you can store
sequences of values in the rows of the CSV file and then read from the file to
recover the data.

Reading and writing CSV files is so common that the Python standard library has
a module called 'csv' to lessen the workload required for working with CSV files.
"""
# The csv Module:
# The csve module can be used to read and write CSV files. In this section you
# will work the previous example using the csv module so you can see how the
# module works and what operations it handles for you.
# To get started, import the csv module:
import csv

# Let's start by creating a new CSV file containing several days' worth of
# temperature data:
daily_temperatures_lists = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
]

# Now open the temperatures.csv file in write mode:
file_path = Path.home() / "temperatures.csv"
file_obj2 = file_path.open(mode="w", encoding="utf-8", newline="")
# instead of using a 'with' statement, you created a file object and assign it
# to the file variable so you can inspect each step of the writing process.

# IMPORTANT:
"""in the above example, notice that the 'newline' parameter in the .open()
method is set to "". This is because the csv module does its own newline
conversions. If you don't specify newline="" when opening the file, then some
operating systems, such as Windows, will interpret newlines incorrectly and
insert a second newline after each line in the file. 
"""

# Now create a new CSV writer object by passing the file object 'file_obj2' to
# the csv.write() method and assign it to the variable writer_obj2:
writer_obj2 = csv.writer(file_obj2)

# csv.writer() returns a CSV writer object which contains methods for writing
# data to the CSV file.
# For instance, you can use the writer_obj2.writerow() method to write a LIST
# to a new row in the CSV file:
for temp_list in daily_temperatures_lists:
    writer_obj2.writerow(temp_list)

# Just like the file object's .write() method, .writerow() method retuns the
# number of characters written to the file. Each list in the
# daily_temperatures_lists gets converted to a string containing the
# temperatures separated by comma, and each of those strings has 19 characters.

# Now close the file.
file_obj2.close()

# this is the content of the temperatures.csv file:
# 68,65,68,70,74,72
# 67,67,70,72,72,70
# 68,70,74,76,74,73

# in the above example, yo didn't use the 'with' statement to write to the file
# so that you could inspect each operation in the IDLE's interactive window. In
# practice, it is much better to use the 'with' statement. For example:
with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for temp_list in daily_temperatures_lists:
        writer.writerow(temp_list)

# The main advantage of using csv.writer() method to write to a CSV file is that
# you don't need to worry about converting values to strings with comma before
# writing them to the file. The csv.writer() method handles this for you, which
# results in shorter and cleaner code.

# The .writerow() method writes a single row to a CSV file, but you can write
# multiple rows at once using the .writerows() method. This shorter the code
# even more when you data is already in a LIST of LISTS:
with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(daily_temperatures_lists)

# Now let's read from the temperatures.csv file to recover the
# daily_temperatures_lists LIST of LISTS that you used to create the file.

# Reading CSV Files With csv.reader:
""" To read a CSV file with the csv module, you use the csv.reader class.
Like csv.writer objects, csv.reader objects are instantiated from a file object:
"""
file_obj1 = file_path.open(mode="r", encoding="utf-8", newline="")
reader_obj1 = csv.reader(file_obj1)  # instantiated from a file object.

# The csv.reader() method returns a CSV reader object that can be used to
# iterate over the rows of the CSV file:
for row in reader_obj1:
    print(f"row --> {row}")

file_obj1.close()

""" Each row in the CSV file is returned as a list of strings. To recover the
daily_temperatures_lists LIST of LISTS, you need to convert each list of strings
to a list of integers using a list comprehension.
Here is a full example that opens the CSV file in a 'with' statement, reads each
row in the CSV file, converts the list of strings to a list of integers, and
stores each list of integers in a LIST of LISTS called int_daily_temps_lists
"""
# Create an empty list:
int_daily_temps_lists = []
with file_path.open(mode="r", encoding="utf-8", newline="") as file_obj:
    reader_obj = csv.reader(file_obj)  # create an iterable of all rows
    for temp_list in reader_obj:
        int_row = [int(value) for value in temp_list]  # [] creates a list and
        #  using the comprehension to process it and convert to integer.
        int_daily_temps_lists.append(int_row)  # append the converted row

print(f"int_daily_temps_lists --> {int_daily_temps_lists}")
# --> int_daily_temps_lists --> [[68, 65, 68, 70, 74, 72], [67, 67, 70, 72, 72, 70],
#     [68, 70, 74, 76, 74, 73]]

# >>> int_daily_temps_lists
# [[68, 65, 68, 70, 74, 72], [67, 67, 70, 72, 72, 70], [68, 70, 74, 76, 74, 73]]
# >>>
#
"""
It is much easier to work with CSV fils using the csv module than it is using
the standard tools for reading and writing plain text files.
Sometimes, though, CSV files are more complex tan a file with rows of values
that all have the type. Each row may represent a record with various fields, and
the first row in the file may be a HEADER ROW with the names of the fields.
"""

# Reading and Writing CSV Files With Headers.
# here is an example of a CSV file with a header row containing multiple data
# types:
# name,     department,     salary,     age,gender
# Lee,      Operation,      75000.00,   52, Female
# Jane,     Engineering,    85000.00,   43, Female
# Diego,    Sales,          80000.00,   51, Male
# Jon,      Sales,          80500.00,   63, Male
""" The first row of the file contains field names. Each following line contains
a record with a value for each field.

It is possible to read CSV files such as the one above using csv.reader() method,
but you have to keep track of the header rows, and each row is returned as a
list without the field names attached to it. It makes more sense to return each
row as a dictionary whose keys are the field names and whose values are the
field values in the row. This is precisely what the csv.DictReader objects do!!
NOTE: The csv.DictReader object is of csv.DictReader class type:
>>> type(dict_reader_obj)
<class 'csv.DictReader'>
>>> 

Using a text editor, create a new CSV file in our home directory called
employees.csv and save the example CSV text from above to it.
Now open the employees.csv file and create a new csv.DictRead object:
"""
file_path = Path.home() / "employees.csv"
file_obj3 = file_path.open(mode="r", encoding="utf-8", newline="")
dict_reader_obj = csv.DictReader(file_obj3)

# When you create a DictReader object, the first row of the CSV file is assumed
# to contain the field names. These values get stored in a LIST and are assigned
# to the DictReader instance's .fieldnames attribute:
print(f"\dict_reader_obj.fieldnames --> {dict_reader_obj.fieldnames}")
# --> dict_reader_obj.fieldnames --> ['name', 'department', 'salary', 'age',
#     'gender']
# or:
# >>> dict_reader_obj.fieldnames
# ['name', 'department', 'salary', 'age', 'gender']
# >>>

# Just as csv.reader objects, csv.DictReader objects create an iterable, this
# iterable is a LIST of Dictionaries for each fieldnames and row values:
for row in dict_reader_obj:
    print(f"\nrow --> {row}")
    # now using the keys to return the values in the dictionary:
    print(
        f"name --> {row['name']}  department --> {row['department']} \
 salary --> {row['salary']}  age --> {row['age']}"
    )
file_obj3.close()


"""
row --> {'name': 'Lee', 'department': 'Operation', 'salary': '75000.00',
         'age': '52', 'gender': 'Female'}
name --> Lee  department --> Operation  salary --> 75000.00  age --> 52         

row --> {'name': 'Jane', 'department': 'Engineering', 'salary': '85000.00',
         'age': '43', 'gender': 'Female'}
name --> Jane  department --> Engineering  salary --> 85000.00  age --> 43         

row --> {'name': 'Diego', 'department': 'Sales', 'salary': '80000.00',
         'age': '51', 'gender': 'Male'}
name --> Diego  department --> Sales  salary --> 80000.00  age --> 51         

row --> {'name': 'Jon', 'department': 'Sales', 'salary': '80500.00',
         'age': '63', 'gender': 'Male'}
name --> Jon  department --> Sales  salary --> 80500.00  age --> 63         
>>> 
"""


# Instead of returning each row as a list, DictReader objects retun each row as
# a dictonary. The dictionary's keys are the field names, and the values are
# the field values from each rows in the CSV file.
# Notice that the salary and age fields are read as strings. Since CSV files
# are plain text files, THE VALUES ARE ALWAYS READ AS STRINGS, but you can
# convert them to different data types as needed. For example, you can process
# each row with a function that convertd keys to the correct data types:
def process_row(row):
    row["salary"] = float(row["salary"])
    row["age"] = int(row["age"])
    return row


print("\n\n")
with file_path.open(mode="r", encoding="utf-8", newline="") as file_obj:
    dict_reader_obj = csv.DictReader(file_obj)
    for employee in dict_reader_obj:
        print(f"employee --> {process_row(employee)}")
"""
employee --> {'name': 'Lee', 'department': 'Operation', 'salary': 75000.0,
              'age': 52, 'gender': 'Female'}
employee --> {'name': 'Jane', 'department': 'Engineering', 'salary': 85000.0,
              'age': 43, 'gender': 'Female'}
employee --> {'name': 'Diego', 'department': 'Sales', 'salary': 80000.0,
              'age': 51, 'gender': 'Male'}
employee --> {'name': 'Jon', 'department': 'Sales', 'salary': 80500.0,
              'age': 63, 'gender': 'Male'}
>>> 
"""
# The process_row() function takes a row dictionary read from the CSV file and
# returns a new dictionary with the 'salary' key converted to float and the
# 'age' key converted to integer number.

print("\n\n")

# Writing CSV Files With Headers Using csv.DictWriter class:
""" You can write CSV files with headers using the csv.DictWriter class, which
writes dictionaries with shared keys to rows in a CSV file. This is the common
keys parts are moved the the first row of the CSV file, and the values part to
the corresponding detail row.
The following LIST of dictionaries represents a small database of people and
their ages:
"""
people_list = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24},
]
# To store the data in the 'people_list' list to a CSV file, open a new file
# called people.csv in write mode and create a new csv.DictWriter object, from
# the file object:
file_path = Path.home() / "people.csv"
file_obj4 = file_path.open(mode="w", encoding="utf-8", newline="")
dict_writer_obj = csv.DictWriter(file_obj4, fieldnames=["name", "age"])

# When you instantiate a new DictWriter object, the first parameter is the
# file object for writing the CSV file data. The 'fieldnames' parameter, which
# is required, is a list of strings of the field names or key in each row.

# Just like the csv.writer object, DictWriter objects have .writerow() and
# .writerows() methods for writing rows of data to the file. DictWriter objects
# also have a third method called .writeheader() that writes the header row to
# the CSV file:
dict_writer_obj.writeheader()  # write the header using the fieldnames info.
#            provisioned in the DictWriter object instantiation.

# .writeheader() method returns the number of characters written to the file,
# which is 10 in this case. Writing the header row is optional but recommended
# because it helps to define what the dsata contained inthe CSV file represents.
# It also makes it easy to read the rows from the CSV file as dictionaries using
# the DictReader class.

# With the header written, you can write the data in the 'people_list' LIST to
# the CSV file using the .writerows() method:
dict_writer_obj.writerows(people_list)  # write the whole list of dictionaries
# to the CSV file ONLY SELECTING THE VALUES part of each row and separating with
# comma ','

# Now using the DictWriter.writerow() method. for one row at a time we need to:
# 2- Create a loop on the LIST of dictionaries containig the data 'people_list'
for person in people_list:
    dict_writer_obj.writerow(person)
    print(f"person --> {person}")
# The above code duplicate the 3 rows in the CSV file, but this is fine for now.

file_obj4.close()

""" In the example above, the list literal ["name", "age"] is passed to the
'fieldnames' parameter.
But you can also set fieldnames using the dictionary keys() method, to create
a LIST of keys items in one of the rows in the LIST of dictionary people_list:
This is 'fieldnames=people_list[0].keys()' since people_list[0] is a dictionary
whose keys are the field names. This is useful when the field names are
unknown or when there are so many fields that a LIST is impractical.
"""
file_path = Path.home() / "people2.csv"
with file_path.open(mode="w", encoding="utf-8", newline="") as file_obj5:
    dict_writer_obj5 = csv.DictWriter(file_obj5, fieldnames=people_list[2].keys())
    dict_writer_obj5.writeheader()
    for person in people_list:
        dict_writer_obj5.writerow(person)
    # Now writing the whole LIST of dictionaries using DictWriter.writerows()

    dict_writer_obj5.writerows(people_list)
# The above code duplicate the 3 rows in the CSV file, but this is fine for now.


# CSV files are a flexible and convenient way of storing data. They are
# frequently used in business worldwide, and knowing how to work with them is
# a valuable skill!


# Review Exercises
# 1:
# Write a program that writes the following list of lists to a file in your
# home directory called numbers.csv
from pathlib import Path
import csv

numbers_lists = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

file_path = Path.home() / "numbers.csv"
with file_path.open(mode="w", encoding="utf-8", newline="") as file_obj:
    writer_obj = csv.writer(file_obj)

    for numbers_list in numbers_lists:
        writer_obj.writerow(numbers_list)

    # Now adding all at once with writer_obj.writerows()
    writer_obj.writerows(numbers_lists)  # duplicate the rows in file, but okay
""" numbers.csv file:
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
"""

# 2:
# Write a program that reads the numbers in the numbers.csv file from exercise
# 1 into a list of lists of integers called numbers. Print the list of lists.
# Your output should look like this:
# the list of lists numbers --> [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
# [11, 12, 13, 14, 15], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

print(f"\n\nExercise # 2 ***")

# Create an empty list:
numbers = []

with file_path.open(mode="r", encoding="utf-8", newline="") as file_obj:
    reader_obj = csv.reader(file_obj)
    for number_list in reader_obj:
        numbers.append([int(value) for value in number_list])

    print(f"the list of lists numbers --> {numbers}")
# the list of lists numbers --> [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
# [11, 12, 13, 14, 15], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# 3:
# Write a program that writes the following list of directories to a file in
# your home directory called favorite_colors.csv:
# list of dictionaries:
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]
# The output CSV file should have the following format:
# name,favorite color
# Joe, blue
# Anne, green
# Bailey, red

file_path = Path.home() / "favorite_colors.csv"
with file_path.open(mode="w", encoding="utf-8", newline="") as file_obj:
    dict_writer_obj = csv.DictWriter(file_obj, fieldnames=favorite_colors[0].keys())

    dict_writer_obj.writeheader()
    dict_writer_obj.writerows(favorite_colors)

    # Now using dict_writer_obj.writerow() to add one at a time:
    for dict_color in favorite_colors:
        dict_writer_obj.writerow(dict_color)  # duplicate the rows in the file
"""
This is how the CSV "favorite_colors.csv" file looks like:
name,favorite_color
Joe,blue
Anne,green
Bailey,red
Joe,blue
Anne,green
Bailey,red
"""

# 4:
# Write a program that reads the data from the favorite_colors.csv file from
# exercise 3 into a list of dictionaries called favorite_colors. Print the list
# of dictionaries. the output should look something like this:
# Create the list of dictoinaries:
print(f"\n\nExercise # 4 ***")
favorite_colors_list = []

with file_path.open(mode="r", encoding="utf-8", newline="") as file_obj:
    dict_reader_obj = csv.DictReader(file_obj)
    for favorite_color in dict_reader_obj:
        favorite_colors_list.append(favorite_color)
        print(
            f"favorite_color['name']--> {favorite_color['name']} --> \
 {favorite_color['favorite_color']}"
        )

    print(
        f"The list of dictionaries favorite_colors_list --> \
{favorite_colors_list}"
    )

"""
The list of dictionaries favorite_colors_list -->
[{'name': 'Joe', 'favorite_color': 'blue'},
{'name': 'Anne', 'favorite_color': 'green'},
{'name': 'Bailey', 'favorite_color': 'red'},
{'name': 'Joe', 'favorite_color': 'blue'},
{'name': 'Anne', 'favorite_color': 'green'},
{'name': 'Bailey', 'favorite_color': 'red'}]
>>> 
"""

print(f"\n\nExercise Challenge ***")
# challenge: Create a High Scores List.
""" Using the scores_csv file in your home directory:
name, score
hector, 45
Paul, 41
hector, 89
...
Write a program  that reads  the data from this CSV file and create a new file
called high_score.csv in which each row contains the player's name and their
highest score.
"""
# create the empty player highest score dictionary :
dict_player_highest_score = {}

# define input and output files Path:
from pathlib import Path

scores_file_path = Path.home() / "scores.csv"
highest_scores_path = Path.home() / "high_score.csv"


with scores_file_path.open(mode="r", encoding="utf-8", newline="") as scores_file_obj:
    dict_reader_obj = csv.DictReader(scores_file_obj)

    for current_player in dict_reader_obj:
        # add or update to the dict_player_highest_score
        print(f"****** current_player --> {current_player}")

        if current_player["name"] in dict_player_highest_score.keys():
            if (
                current_player["score"]
                > dict_player_highest_score[current_player["name"]]
            ):
                dict_player_highest_score[current_player["name"]] = current_player[
                    "score"
                ]
                print(
                    f"changed current_player['name'] \
{current_player['name']}"
                )
            else:
                # continue
                print(f"{current_player['name']} score less")
        else:
            dict_player_highest_score[current_player["name"]] = current_player["score"]
            print(f"appended as new --> {current_player}")

    print(f"dict_player_highest_score --> {dict_player_highest_score}")

# convert dict_player_highest_score to Dict_List so that it can be moved to the
# output CSV file:
dict_player_highest_score_list = []
for player, score in dict_player_highest_score.items():
    dict_player_highest_score_list.append({"name": player, "highest_score": score})

# create the dict_writer for the output CSV file high_score_path:
with highest_scores_path.open(
    mode="w", encoding="utf-8", newline=""
) as highest_score_file_obj:
    dict_writer_obj = csv.DictWriter(
        highest_score_file_obj, fieldnames=dict_player_highest_score_list[0].keys()
    )

    # add the whole dictionaries list to the outpue CSV file
    dict_writer_obj.writeheader()

    dict_writer_obj.writerows(dict_player_highest_score_list)

#    for player_highest_score in dict_player_highest_score_list:
#        print(f"player_highest_score --> {player_highest_score}")
#        dict_writer_obj.writerow(player_highest_score)
""" Below the content of the output csv file high_score.csv:
name,highest_score
LLCoolDave,27
red,12
tom123,26
O_O,7
Misha46,25
Empiro,23
MaxxT,25
L33tH4x,42
johnsmith,30
Hector,525
Juan,90
"""

""" Code from the solution for the chapter support/verification """

print(f"\n\n Challenge Solution from book")

import csv
from pathlib import Path

scores_csv_path = Path.home() / "scores.csv"

with scores_csv_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    scores = [row for row in reader]  # create a list of Dict from reader
    print(f"score row from input --> {scores}")
# score row from input --> [{'name': 'LLCoolDave', 'score': '23'},
# {'name': 'LLCoolDave', 'score': '27'}, ... ]

high_scores = {}  # Create the Dictionary to hold the temp data.

for item in scores:
    name = item["name"]
    score = int(item["score"])

    if name not in high_scores:
        high_scores[name] = score
    else:
        if score > high_scores[name]:
            high_scores[name] = score

output_csv_file = Path.home() / "highest_scores2.csv"
with output_csv_file.open(mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "highest_score"])

    writer.writeheader()
    for name in high_scores:
        row_dict = {"name": name, "highest_score": high_scores[name]}
        writer.writerow(row_dict)
""" Below the content of the output csv file highest_scores2.csv:
name,highest_scoreLLCoolDave,27red,12tom123,26O_O,22Misha46,25Empiro,23MaxxT,25L33tH4x,42johnsmith,30Hector,525Juan,90
"""


# xxxxxxxxxxx
