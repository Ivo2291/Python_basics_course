import math

days_count = int(input())
left_food_in_kg = int(input())
dog_day_food_in_kg = float(input())
cat_day_food_in_kg = float(input())
turtle_day_food_in_gr = float(input())

dog_food_needed = days_count * dog_day_food_in_kg
cat_food_needed = days_count * cat_day_food_in_kg
turtle_food_needed = (days_count * turtle_day_food_in_gr) / 1000
total_food = dog_food_needed + cat_food_needed + turtle_food_needed
difference = abs(left_food_in_kg - total_food)

if total_food <= left_food_in_kg:
    print(f"{math.floor(difference)} kilos of food left.")

else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
