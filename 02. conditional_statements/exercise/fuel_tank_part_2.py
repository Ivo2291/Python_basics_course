fuel_type = input()
fuel_liters = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_price = 0

if fuel_type == "Gas":
    if club_card == "Yes":
        gas_price -= 0.08
        total_price += fuel_liters * gas_price
    else:
        total_price += fuel_liters * gas_price

elif fuel_type == "Gasoline":
    if club_card == "Yes":
        gasoline_price -= 0.18
        total_price += fuel_liters * gasoline_price
    else:
        total_price += fuel_liters * gasoline_price

elif fuel_type == "Diesel":
    if club_card == "Yes":
        diesel_price -= 0.12
        total_price += fuel_liters * diesel_price
    else:
        total_price += fuel_liters * diesel_price

if 20 <= fuel_liters <= 25:
    total_price -= total_price * 0.08

elif fuel_liters > 25:
    total_price -= total_price * 0.1

print(f"{total_price:.2f} lv.")
