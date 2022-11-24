film_budget = float(input())
extras_count = int(input())
clothes_price_per_extra = float(input())

money_are_enough = False

if extras_count > 150:
    clothes_price_per_extra -= clothes_price_per_extra * 0.1

decor_sum = film_budget * 0.1
clothes_sum = extras_count * clothes_price_per_extra
total_sum_for_movie = decor_sum + clothes_sum

if total_sum_for_movie <= film_budget:
    money_are_enough = True

difference = abs(film_budget - total_sum_for_movie)

if money_are_enough:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
