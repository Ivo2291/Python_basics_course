actor_name = input()
total_points = float(input())
number_in_jury = int(input())
is_nominated = False

for current_grade in range(number_in_jury):
    name_of_actor = input()
    current_points = float(input())
    final_points = len(name_of_actor) * current_points / 2
    total_points += final_points

    if total_points > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")

else:
    difference = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
