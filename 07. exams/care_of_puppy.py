puppy_food_bought_in_kg = int(input())

food_counter = 0

command = input()

while command != "Adopted":
    food_eaten_grams = int(command)
    food_counter += food_eaten_grams

    command = input()

puppy_food_bought_in_grams = puppy_food_bought_in_kg * 1000
difference = abs(puppy_food_bought_in_grams - food_counter)

if food_counter <= puppy_food_bought_in_grams:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
