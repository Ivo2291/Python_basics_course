inherited_money = float(input())
year_to_live = int(input())

spent_money = 0
age = 18

for year in range(1800, year_to_live + 1):

    if year % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + (50 * age)
    age += 1

difference = abs(inherited_money - spent_money)

if spent_money <= inherited_money:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")
