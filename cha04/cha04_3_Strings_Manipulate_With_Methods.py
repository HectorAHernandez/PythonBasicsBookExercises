print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honey Badger".lower())
print("Hector".lower())

print()

print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honey Badger".upper())
print("Hector".upper())

string1 = "    Filet Mignon"
print("string1 -->", string1, ", left strippe -->", string1.lstrip())
string2 = "Brisket     "
print("string2 -->", string2, ", right strip -->", string2.rstrip())
string3 = "   Cheeseburger    "
print("string3 -->", string3, ", both side strip -->", string3.strip())
print()

string1 = "Becomes"
print("'Becomes' string1.startswith(\"be\") False -->", string1.startswith("be"))
string2 = "becomes"
print("'becomes' string2.startswith(\"be\") True -->", string2.startswith("be"))
string3 = "BEAR"
print("'BEAR' string3.startswith(\"be\") False --> ", string3.startswith("be"))
string4 = "  beautiful"
print("'  beautiful' string4.startswith(\"be\") False -->", string4.startswith("be"))
print()

print("'Becomes'.lower() string1.lower().startswith(\"be\") True -->", string1.lower().startswith("be"))
print("'becomes' string2.startswith(\"be\") True -->", string2.startswith("be"))
print("'BEAR'.lower() string3.lower().startswith(\"be\") True --> ", string3.lower().startswith("be") )
print("'  beautiful' string4.lstrip().startswith(\"be\") True -->", string4.lstrip().startswith("be"))
