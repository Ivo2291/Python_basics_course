import math

square_meters_of_vineyard = int(input())
grape_for_square_meter = float(input())
needed_wine = int(input())
workers_count = int(input())

total_grape = square_meters_of_vineyard * grape_for_square_meter
grape_for_wine = total_grape * 0.4
total_liters_wine = grape_for_wine / 2.5

difference = abs(needed_wine - total_liters_wine)
wine_per_person = difference / workers_count

if total_liters_wine >= needed_wine:
    print(f"Good harvest this year! Total wine: {math.floor(total_liters_wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_per_person)} liters per person.")

else:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
