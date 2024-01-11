# 1: print with as fixed-point with 3 decimal places:
value1 = 3**0.125
print(f"value with 3 decimal: {value1: .3f}")

# 2: print the number 150000 as currency with the thousands grouped and 2 decimal:
value2 = 150000
print(f"Printing as currency: {150000: ,.2f}")
print(f"Printing as currency: {value2: ,.2f}")

# 3: print  2/ 10 as percentage with no decimal places:
value3 = 2 / 10
print(f"percentage format without decimal {value3:.0%}")
