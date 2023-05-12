# 1:
for n in range(2, 10):
    print(f"using for --> number: {n}")

# 2:
n = 2
while n < 10:
    print(f"using while --> number: {n}")
    n = n + 1


# 3:
def double(number):
    return number * 2


for n in range(1, 4):
    print(f"for {n} then: {n * double(2)}")
