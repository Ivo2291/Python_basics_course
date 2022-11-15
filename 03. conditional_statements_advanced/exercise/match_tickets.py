def calc_transport_price(some_budget, count_of_people):

    if count_of_people <= 4:
        result = some_budget * 0.75
    elif count_of_people <= 9:
        result = some_budget * 0.6
    elif count_of_people <= 24:
        result = some_budget * 0.5
    elif count_of_people <= 49:
        result = some_budget * 0.4
    else:
        result = some_budget * 0.25

    return result


budget = float(input())
tickets_category = input()
people_count = int(input())

transport_price = 0

if tickets_category == "VIP":
    ticket_price = 499.99

    transport_price = calc_transport_price(budget, people_count)

else:
    ticket_price = 249.99

    transport_price = calc_transport_price(budget, people_count)

tickets_cost = ticket_price * people_count
total_sum = transport_price + tickets_cost
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
