budget = float(input())
category_of_ticket = input()
people_in_the_group = int(input())
transport_price = 0
ticket_price = 0
total_price = 0

if people_in_the_group < 5:
    transport_price = budget * 0.75
elif people_in_the_group < 10:
    transport_price = budget * 0.60
elif people_in_the_group < 25:
    transport_price = budget * 0.50
elif people_in_the_group < 50:
    transport_price = budget * 0.40
else:
    transport_price = budget * 0.25

if category_of_ticket == "VIP":
    ticket_price = 499.99
else:
    ticket_price = 249.99

total_price = (ticket_price * people_in_the_group) + transport_price
difference = abs(budget - total_price)

if budget > total_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
