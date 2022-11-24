count_of_days = int(input())
total_food = float(input())

dog_food_counter = 0
cat_food_counter = 0
biscuits_eaten = 0

for day in range(1, count_of_days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())

    if day % 3 == 0:
        biscuits_eaten = (food_eaten_by_dog + food_eaten_by_cat) * 0.1

    dog_food_counter += food_eaten_by_dog
    cat_food_counter += food_eaten_by_cat

total_food_eaten = dog_food_counter + cat_food_counter

food_eaten = (total_food_eaten / total_food) * 100
eaten_by_dog = (dog_food_counter / total_food_eaten) * 100
eaten_by_cat = (cat_food_counter / total_food_eaten) * 100

print(f"Total eaten biscuits: {round(biscuits_eaten)}gr.")
print(f"{food_eaten:.2f}% of the food has been eaten.")
print(f"{eaten_by_dog:.2f}% eaten from the dog.")
print(f"{eaten_by_cat:.2f}% eaten from the cat.")
