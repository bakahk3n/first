deposit_balances = float(input())
interest = 1.071
year = 0
while deposit_balances < 700000:
    deposit_balances = deposit_balances * interest
    year += 1
print(year)
