budget = int(input())
season = input()
fishermen_count = int(input())

rent_for_ship = 0

if season == "Spring":
    rent_for_ship = 3000
    if fishermen_count <= 6:
        rent_for_ship = rent_for_ship * 0.9
    elif 7 <= fishermen_count <= 11:
        rent_for_ship = rent_for_ship * 0.85
    else:
        rent_for_ship = rent_for_ship * 0.75

elif season == "Summer" or season == "Autumn":
    rent_for_ship = 4200

    if fishermen_count <= 6:
        rent_for_ship = rent_for_ship * 0.9
    elif 7 <= fishermen_count <= 11:
        rent_for_ship = rent_for_ship * 0.85
    else:
        rent_for_ship = rent_for_ship * 0.75

elif season == "Winter":
    rent_for_ship = 2600

    if fishermen_count <= 6:
        rent_for_ship = rent_for_ship * 0.9
    elif 7 <= fishermen_count <= 11:
        rent_for_ship = rent_for_ship * 0.85
    else:
        rent_for_ship = rent_for_ship * 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    rent_for_ship = rent_for_ship * 0.95

if budget >= rent_for_ship:
    print(f"Yes! You have {budget - rent_for_ship:.2f} leva left.")

elif rent_for_ship > budget:
    print(f"Not enough money! You need {rent_for_ship - budget:.2f} leva.")
