budget = float(input())
season = input()

location = ""
type_of_stay = ""
price = 0

if budget <= 1000:
    type_of_stay = "Camp"

    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    type_of_stay = "Hut"

    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.6

else:
    type_of_stay = "Hotel"
    price = budget * 0.9

    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {type_of_stay} - {price:.2f}")
