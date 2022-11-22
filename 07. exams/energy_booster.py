fruit = input()
size_of_the_set = input()
count_of_orders = int(input())

energy_booster_set_price = 0
total_price = 0

if size_of_the_set == "small":
    if fruit == "Watermelon":
        energy_booster_set_price = 56 * 2
    elif fruit == "Mango":
        energy_booster_set_price = 36.66 * 2
    elif fruit == "Pineapple":
        energy_booster_set_price = 42.1 * 2
    elif fruit == "Raspberry":
        energy_booster_set_price = 20 * 2

elif size_of_the_set == "big":
    if fruit == "Watermelon":
        energy_booster_set_price = 28.7 * 5
    elif fruit == "Mango":
        energy_booster_set_price = 19.6 * 5
    elif fruit == "Pineapple":
        energy_booster_set_price = 24.8 * 5
    elif fruit == "Raspberry":
        energy_booster_set_price = 15.2 * 5

total_price = energy_booster_set_price * count_of_orders

if 400 <= total_price <= 1000:
    total_price -= total_price * 0.15

elif total_price > 1000:
    total_price -= total_price * 0.5

print(f"{total_price:.2f} lv.")
