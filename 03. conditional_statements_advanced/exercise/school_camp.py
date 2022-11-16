season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

type_of_sport = ""
price_for_stay = 0
discount = 0

if group_type == "girls":
    if season == "Winter":
        type_of_sport = "Gymnastics"
        price_for_stay = nights_count * (students_count * 9.6)
    elif season == "Spring":
        type_of_sport = "Athletics"
        price_for_stay = nights_count * (students_count * 7.2)
    elif season == "Summer":
        type_of_sport = "Volleyball"
        price_for_stay = nights_count * (students_count * 15)

elif group_type == "boys":
    if season == "Winter":
        type_of_sport = "Judo"
        price_for_stay = nights_count * (students_count * 9.6)
    elif season == "Spring":
        type_of_sport = "Tennis"
        price_for_stay = nights_count * (students_count * 7.2)
    elif season == "Summer":
        type_of_sport = "Football"
        price_for_stay = nights_count * (students_count * 15)

else:
    if season == "Winter":
        type_of_sport = "Ski"
        price_for_stay = nights_count * (students_count * 10)
    elif season == "Spring":
        type_of_sport = "Cycling"
        price_for_stay = nights_count * (students_count * 9.5)
    elif season == "Summer":
        type_of_sport = "Swimming"
        price_for_stay = nights_count * (students_count * 20)

if 10 <= students_count < 20:
    discount = price_for_stay * 0.05
elif 20 <= students_count < 50:
    discount = price_for_stay * 0.15
elif students_count >= 50:
    discount = price_for_stay * 0.5

total_sum = price_for_stay - discount

print(f"{type_of_sport} {total_sum:.2f} lv.")
