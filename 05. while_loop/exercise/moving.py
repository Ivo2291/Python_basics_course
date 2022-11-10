width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())

total_free_space = width_of_free_space * length_of_free_space * height_of_free_space
there_is_more_free_space = True

command = input()

while command != "Done":
    boxes_to_move = int(command)
    total_free_space -= boxes_to_move

    if total_free_space <= 0:
        there_is_more_free_space = False
        break

    command = input()

if there_is_more_free_space:
    print(f"{total_free_space} Cubic meters left.")

else:
    print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")
