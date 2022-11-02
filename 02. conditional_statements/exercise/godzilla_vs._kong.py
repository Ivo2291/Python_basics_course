film_budget = float(input())
number_of_extras = int(input())
clothes_price_per_extra = float(input())

if number_of_extras > 150:
    clothes_price_per_extra = clothes_price_per_extra - (clothes_price_per_extra * 0.1)

decor = film_budget * 0.1
sum_clothes = number_of_extras * clothes_price_per_extra
total_sum = decor + sum_clothes
money_left = film_budget - total_sum

if total_sum <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")
