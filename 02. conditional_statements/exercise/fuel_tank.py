fuel_type = input()
liters_fuel = float(input())

if fuel_type == "Diesel":
    if liters_fuel >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")

elif fuel_type == "Gasoline":
    if liters_fuel >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")

elif fuel_type == "Gas":
    if liters_fuel >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")

else:
    print(f"Invalid fuel!")
