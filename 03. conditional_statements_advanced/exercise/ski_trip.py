days_of_stay = int(input())
room_type = input()
grade = input()

room_for_one_person_per_night = 18
apartment_per_night = 25
president_apartment_per_night = 35
costs = 0
days_of_stay -= 1

if room_type == "room for one person":
    costs = room_for_one_person_per_night * days_of_stay

elif room_type == "apartment":
    costs = apartment_per_night * days_of_stay

    if days_of_stay < 10:
        costs -= costs * 0.3
    elif 10 <= days_of_stay <= 15:
        costs -= costs * 0.35
    elif days_of_stay > 15:
        costs -= costs * 0.5

elif room_type == "president apartment":
    costs = president_apartment_per_night * days_of_stay

    if days_of_stay < 10:
        costs -= costs * 0.1
    elif 10 <= days_of_stay <= 15:
        costs -= costs * 0.15
    elif days_of_stay > 15:
        costs -= costs * 0.2

if grade == "positive":
    costs += costs * 0.25
else:
    costs -= costs * 0.1

print(f"{costs:.2f}")
