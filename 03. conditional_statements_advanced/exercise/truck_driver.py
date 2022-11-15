season = input()
km_per_month = float(input())

driving_season_in_months = 4
earned_money = 0

if km_per_month <= 5000:
    if season == "Summer":
        earned_money = km_per_month * 0.9
    elif season == "Winter":
        earned_money = km_per_month * 1.05
    else:
        earned_money = km_per_month * 0.75

elif 5000 < km_per_month <= 10000:
    if season == "Summer":
        earned_money = km_per_month * 1.1
    elif season == "Winter":
        earned_money = km_per_month * 1.25
    else:
        earned_money = km_per_month * 0.95

elif 10000 < km_per_month <= 20000:
    earned_money = km_per_month * 1.45

taxes = (earned_money * driving_season_in_months) * 0.1
salary = (earned_money * driving_season_in_months) - taxes

print(f"{salary:.2f}")
