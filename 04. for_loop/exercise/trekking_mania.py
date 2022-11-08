count_of_groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for i in range(count_of_groups):
    number_of_people = int(input())
    total_people += number_of_people

    if number_of_people <= 5:
        musala += number_of_people
    elif number_of_people <= 12:
        monblan += number_of_people
    elif number_of_people <= 25:
        kilimanjaro += number_of_people
    elif number_of_people <= 40:
        k2 += number_of_people
    else:
        everest += number_of_people

musala = musala / total_people * 100
monblan = monblan / total_people * 100
kilimanjaro = kilimanjaro / total_people * 100
k2 = k2 / total_people * 100
everest = everest / total_people * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")
