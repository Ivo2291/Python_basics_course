month = input()
count_of_nights = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65

    if 7 < count_of_nights <= 14:
        studio_price -= studio_price * 0.05
    elif count_of_nights > 14:
        apartment_price -= apartment_price * 0.1
        studio_price -= studio_price * 0.3

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70

    if count_of_nights > 14:
        studio_price -= studio_price * 0.2
        apartment_price -= apartment_price * 0.1

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

    if count_of_nights > 14:
        apartment_price -= apartment_price * 0.1

print(f"Apartment: {apartment_price * count_of_nights:.2f} lv.")
print(f"Studio: {studio_price * count_of_nights:.2f} lv.")
