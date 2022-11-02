import math

square_meters_of_vineyard = int(input())
grape_per_square_meter = float(input())
needed_wine_liters = int(input())
workers_count = int(input())
kg_grapes_for_one_liter_wine = 2.5

total_grape = grape_per_square_meter * square_meters_of_vineyard
produced_wine = total_grape * 0.4 / kg_grapes_for_one_liter_wine
difference = abs(needed_wine_liters - produced_wine)
wine_for_one_worker = difference / workers_count

if produced_wine < needed_wine_liters:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")

else:
    print(f"Good harvest this year! Total wine: {math.floor(produced_wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_for_one_worker)} liters per person.")
