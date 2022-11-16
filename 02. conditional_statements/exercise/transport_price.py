kilometers = int(input())
part_of_the_day = input()

starting_fee = 0.7
price_for_transport = 0

if kilometers < 20:
    price_for_transport += starting_fee

    if part_of_the_day == "day":
        price_for_transport += kilometers * 0.79
    else:
        price_for_transport += kilometers * 0.9

elif kilometers < 100:
    price_for_transport += kilometers * 0.09

else:
    price_for_transport += kilometers * 0.06

print(f"{price_for_transport:.2f}")
