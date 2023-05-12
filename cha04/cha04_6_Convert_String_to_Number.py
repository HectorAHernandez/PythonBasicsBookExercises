num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print("doubled num is ", doubled_num)

num_pancakes = 10
print("I am going to eat " + str(num_pancakes) + " pancakes")

total_pancakes = 20
pancakes_eaten = 10
print("Only " + str(total_pancakes - pancakes_eaten) + " left")

print("I am going to eat " + str(5) + " pancakes")

# Exercise for section 4.7:
# 1-
total = "125"
int_total = int(total)
print("int_total * 5 = 625 -->", int_total * 5)

# 2:
total = "50.55"
float_total = float(total)
print("float_total * 4 = 202.20 -->", float_total * 4)

# 3:
int_value = 454
string1 = "999"
print("both value side by side: " + string1 + " And " + str(int_value))

# 4:
value1 = input("Enter value1: ")
value2 = input("Enter value2: ")
int_value1 = int(value1)
int_value2 = int(value2)
print("The product of " + value1 + " and " + value2 + " is " + str(float(int_value1 * int_value2)))
