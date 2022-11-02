kilometers = int(input())
trip_time = input()
transport_price = 0
starting_fee = 0.70

if kilometers < 20:
    if trip_time == "day":
        transport_price = starting_fee + (kilometers * 0.79)

    else:
        transport_price = starting_fee + (kilometers * 0.90)

elif kilometers < 100:
    transport_price = kilometers * 0.09

else:
    transport_price = kilometers * 0.06

print(f"{transport_price:.2f}")
