puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
discount = 0

excursion_price = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

toys_price = number_of_puzzles * puzzle_price + number_of_talking_dolls *\
             talking_doll_price + number_of_teddy_bears * teddy_bear_price + number_of_minions *\
             minion_price + number_of_trucks * truck_price

number_of_toys = number_of_puzzles + number_of_talking_dolls + number_of_teddy_bears +\
                 number_of_minions + number_of_trucks

if number_of_toys >= 50:
    discount = toys_price * 0.25

total_price = toys_price - discount
rent = total_price * 0.1
income = total_price - rent

money_left = income - excursion_price

if money_left < 0:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")

else:
    print(f"Yes! {money_left:.2f} lv left.")
