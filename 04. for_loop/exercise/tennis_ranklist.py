from math import floor
count_of_tournaments = int(input())
starting_points = int(input())

w = 2000
f = 1200
sf = 720
points = 0
winner = 0

for i in range(count_of_tournaments):
    final_stage = input()

    if final_stage == "W":
        starting_points += w
        points += w
        winner += 1

    elif final_stage == "F":
        starting_points += f
        points += f

    elif final_stage == "SF":
        starting_points += sf
        points += sf

average_points = points / count_of_tournaments
winner_percent = winner / count_of_tournaments * 100
total_points = starting_points

print(f"Final points: {starting_points}")
print(f"Average points: {floor(average_points)}")
print(f"{winner_percent:.2f}%")
