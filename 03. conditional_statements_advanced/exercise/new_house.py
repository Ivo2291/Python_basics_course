type_of_the_flower = input()
flower_count = int(input())
budged = int(input())

rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50
flowers_sum = 0

if type_of_the_flower == "Roses":
    flowers_sum = flower_count * rose_price

    if flower_count > 80:
        flowers_sum -= flowers_sum * 0.1

elif type_of_the_flower == "Dahlias":
    flowers_sum = flower_count * dahlia_price

    if flower_count > 90:
        flowers_sum -= flowers_sum * 0.15

elif type_of_the_flower == "Tulips":
    flowers_sum = flower_count * tulip_price

    if flower_count > 80:
        flowers_sum -= flowers_sum * 0.15

elif type_of_the_flower == "Narcissus":
    flowers_sum = flower_count * narcissus_price

    if flower_count < 120:
        flowers_sum += flowers_sum * 0.15

elif type_of_the_flower == "Gladiolus":
    flowers_sum = flower_count * gladiolus_price

    if flower_count < 80:
        flowers_sum += flowers_sum * 0.20

if budged >= flowers_sum:
    print(f"Hey, you have a great garden with {flower_count} {type_of_the_flower} and "
          f"{budged - flowers_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {flowers_sum - budged:.2f} leva more.")
