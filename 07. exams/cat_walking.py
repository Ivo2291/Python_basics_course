minutes_of_walks = int(input())
count_of_walks_per_day = int(input())
consumed_calories_per_day = int(input())

burned_calories_per_minute = 5

day_minutes_of_walks = count_of_walks_per_day * minutes_of_walks
day_calories_burned = day_minutes_of_walks * burned_calories_per_minute
calories_after_walks = consumed_calories_per_day / 2

if day_calories_burned >= calories_after_walks:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {day_calories_burned:.0f}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {day_calories_burned:.0f}.")
