days_of_tournament = int(input())

total_money = 0
win_days = 0
lost_days = 0

for day in range(1, days_of_tournament + 1):
    current_money = 0
    won_games = 0
    lost_games = 0

    command = input()

    while command != "Finish":
        game = command
        result = input()

        if result == "win":
            current_money += 20
            won_games += 1
        else:
            lost_games += 1

        command = input()

        if command == "Finish":
            if won_games > lost_games:
                win_days += 1
                current_money += current_money * 0.1
                total_money += current_money
            else:
                lost_days += 1
                total_money += current_money

if win_days > lost_days:
    total_money += total_money * 0.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
