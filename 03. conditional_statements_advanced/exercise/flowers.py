chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_it_holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
bouquet_price = 0
arranging = 2

if season == "Spring" or season == "Summer":
    chrysanthemums_price = chrysanthemums_count * 2
    roses_price = roses_count * 4.1
    tulips_price = tulips_count * 2.5

    if is_it_holiday == "Y":
        chrysanthemums_price += chrysanthemums_price * 0.15
        roses_price += roses_price * 0.15
        tulips_price += tulips_price * 0.15


elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = chrysanthemums_count * 3.75
    roses_price = roses_count * 4.5
    tulips_price = tulips_count * 4.15

    if is_it_holiday == "Y":
        chrysanthemums_price += chrysanthemums_price * 0.15
        roses_price += roses_price * 0.15
        tulips_price += tulips_price * 0.15

flower_count = chrysanthemums_count + roses_count + tulips_count
bouquet_price = chrysanthemums_price + roses_price + tulips_price

if season == "Spring" and tulips_count > 7:
    bouquet_price -= bouquet_price * 0.05
elif season == "Winter" and roses_count >= 10:
    bouquet_price -= bouquet_price * 0.1

if flower_count > 20:
    bouquet_price -= bouquet_price * 0.2

total_price = bouquet_price + arranging

print(f"{total_price:.2f}")
