owned_money = float(input())
gender = input()
age = int(input())
sport_type = input()

monthly_membership = 0
owned_money_are_enough = False

if gender == "m":
    if sport_type == "Gym":
        monthly_membership = 42
    elif sport_type == "Boxing":
        monthly_membership = 41
    elif sport_type == "Yoga":
        monthly_membership = 45
    elif sport_type == "Zumba":
        monthly_membership = 34
    elif sport_type == "Dances":
        monthly_membership = 51
    elif sport_type == "Pilates":
        monthly_membership = 39

elif gender == "f":
    if sport_type == "Gym":
        monthly_membership = 35
    elif sport_type == "Boxing":
        monthly_membership = 37
    elif sport_type == "Yoga":
        monthly_membership = 42
    elif sport_type == "Zumba":
        monthly_membership = 31
    elif sport_type == "Dances":
        monthly_membership = 53
    elif sport_type == "Pilates":
        monthly_membership = 37

if age <= 19:
    monthly_membership -= monthly_membership * 0.2

difference = abs(owned_money - monthly_membership)

if owned_money >= monthly_membership:
    owned_money_are_enough = True

if owned_money_are_enough:
    print(f"You purchased a 1 month pass for {sport_type}.")

else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")
