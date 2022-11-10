required_money = int(input())

payed_in_cash = 0
payed_with_card = 0
pay_counter = 0
cash_counter = 0
card_counter = 0
money_are_collected = False

command = input()

while command != "End":
    product_price = int(command)
    pay_counter += 1

    if pay_counter % 2 != 0:
        if product_price > 100:
            print("Error in transaction!")

        else:
            payed_in_cash += product_price
            cash_counter += 1
            print(f"Product sold!")

    elif pay_counter % 2 == 0:
        if product_price < 10:
            print("Error in transaction!")

        else:
            payed_with_card += product_price
            card_counter += 1
            print(f"Product sold!")

    total_money = payed_in_cash + payed_with_card

    if total_money >= required_money:
        money_are_collected = True
        break

    command = input()

if money_are_collected:
    average_cash_pays = payed_in_cash / cash_counter
    average_card_pays = payed_with_card / card_counter
    print(f"Average CS: {average_cash_pays:.2f}")
    print(f"Average CC: {average_card_pays:.2f}")

else:
    print("Failed to collect required money for charity.")
