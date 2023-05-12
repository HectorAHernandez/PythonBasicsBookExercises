def invest(amount, rate, years):
    principal_amount = amount
    for year in range(1, years + 1):
        principal_amount = principal_amount + principal_amount * rate
        print(f"year {year}: {principal_amount: ,.2f}")


amount = float(input("Enter Amount: "))
annual_percentage_rate = float(input("Enter Annual Percentage Rate: "))
number_of_years = int(input("Enter the number of years: "))

invest(amount, annual_percentage_rate, number_of_years)
