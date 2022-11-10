needed_money = float(input())
owned_money = float(input())

spending_counter = 0
days_counter = 0
you_saved_money = False

while spending_counter < 5:
    action = input()
    money = float(input())
    days_counter += 1

    if action == "spend":
        spending_counter += 1
        owned_money -= money

        if owned_money < 0:
            owned_money = 0

    elif action == "save":
        spending_counter = 0
        owned_money += money

    if owned_money >= needed_money:
        you_saved_money = True
        break

if you_saved_money:
    print(f"You saved the money for {days_counter} days.")

else:
    print("You can't save the money.")
    print(f"{days_counter}")
