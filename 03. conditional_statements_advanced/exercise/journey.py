budget = float(input())
season = input()

place_to_stay = ""
trip_place = ""
price = 0

if budget <= 100:
    trip_place = "Bulgaria"

    if season == "summer":
        price = budget * 0.3
        place_to_stay = "Camp"
    elif season == "winter":
        price = budget * 0.7
        place_to_stay = "Hotel"

elif budget <= 1000:
    trip_place = "Balkans"

    if season == "summer":
        price = budget * 0.4
        place_to_stay = "Camp"
    elif season == "winter":
        price = budget * 0.8
        place_to_stay = "Hotel"

else:
    trip_place = "Europe"
    place_to_stay = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {trip_place}")
print(f"{place_to_stay} - {price:.2f}")
