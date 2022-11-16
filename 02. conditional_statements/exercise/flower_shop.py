import math

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
present_price = float(input())

magnolias_sum = magnolias_count * 3.25
hyacinths_sum = hyacinths_count * 4
roses_sum = roses_count * 3.5
cacti_sum = cacti_count * 8

flowers_sum = magnolias_sum + hyacinths_sum + roses_sum + cacti_sum
taxes = flowers_sum * 0.05

total_sum = flowers_sum - taxes

difference = abs(total_sum - present_price)

if total_sum >= present_price:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")
