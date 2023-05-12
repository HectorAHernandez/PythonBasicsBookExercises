import random
from statistics import mean
def flip_fair():
    if random.randint(0,1) == 0:
        return "heads"
    else:
        return "tails"

total_flips_list = []

for trial in range(10_000):
    result_1 = flip_fair()
    # print(f"result_1: {result_1}")
    count = 0
    while True:
        count += 1
        if flip_fair() == result_1:
            continue
        else:
            break
    total_flips_list.append(count)
        
# print(f"total_flips_list: {total_flips_list}")

print(f"*** Average of flips needed for the sequence to contain both \
heads and tails: {round(mean(total_flips_list))}")


# version # 2: Created when double checking my first solution:
total_flips_list_2 = []

for trial in range(10):
    result_1 = flip_fair()
    print(f"result_1: {result_1}")
    count = 0
    while True:
        count += 1
        result_n = flip_fair()
        print(f"result_n --> {result_n} on count = {count}")
        if result_n == result_1:
        # if flip_fair() == result_1:
            continue
        else:
            break
    total_flips_list_2.append(count)
        
print(f"total_flips_list_2: {total_flips_list_2}")

print(f"Average of flips needed for the sequence to contain both\
 heads and tails: {round(mean(total_flips_list_2))}")
