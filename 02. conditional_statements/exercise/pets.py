import math

days_count = int(input())
food_left_kg = int(input())
dog_day_food_kg = float(input())
cat_day_food_kg = float(input())
turtle_day_food_grams = float(input())

turtle_day_food_kg = turtle_day_food_grams / 1000
food_is_enough = False

food_eaten_by_dog = days_count * dog_day_food_kg
food_eaten_by_cat = days_count * cat_day_food_kg
food_eaten_by_turtle = days_count * turtle_day_food_kg
total_eaten_food = food_eaten_by_dog + food_eaten_by_cat + food_eaten_by_turtle

difference = abs(food_left_kg - total_eaten_food)

if food_left_kg >= total_eaten_food:
    food_is_enough = True

if food_is_enough:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
