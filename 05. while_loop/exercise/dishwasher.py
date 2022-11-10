bottles_of_detergent = int(input())

milliliters_per_bottle = 750
ml_needed_for_dish = 5
ml_needed_for_pot = 15
detergent_is_enough = True
total_detergent = bottles_of_detergent * milliliters_per_bottle
dishwasher_loads = 0
dishes = 0
pots = 0
difference = 0

command = input()

while command != "End":
    dishes_or_pots_count = int(command)
    dishwasher_loads += 1

    if dishwasher_loads % 3 == 0:
        needed_detergent = dishes_or_pots_count * ml_needed_for_pot

        if total_detergent >= needed_detergent:
            total_detergent -= needed_detergent
            pots += dishes_or_pots_count

        else:
            detergent_is_enough = False
            difference = abs(total_detergent - needed_detergent)
            break

    else:
        needed_detergent = dishes_or_pots_count * ml_needed_for_dish

        if total_detergent >= needed_detergent:
            total_detergent -= needed_detergent
            dishes += dishes_or_pots_count

        else:
            detergent_is_enough = False
            difference = abs(total_detergent - needed_detergent)
            break

    command = input()

if detergent_is_enough:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")

else:
    print(f"Not enough detergent, {difference} ml. more necessary!")
