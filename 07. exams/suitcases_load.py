trunk_volume = float(input())

suitcases_counter = 0

command = input()

while command != "End":
    suitcase_volume = float(command)

    if (suitcases_counter + 1) % 3 == 0:
        suitcase_volume += suitcase_volume * 0.1

    if suitcase_volume > trunk_volume:
        print("No more space!")
        break

    suitcases_counter += 1
    current_space = trunk_volume - suitcase_volume
    trunk_volume = current_space

    command = input()

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

print(f"Statistic: {suitcases_counter} suitcases loaded.")
