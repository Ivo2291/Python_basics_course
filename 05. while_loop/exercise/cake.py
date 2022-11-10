width_of_cake = int(input())
length_of_cake = int(input())

number_of_pieces = width_of_cake * length_of_cake
pieces_are_over = False

command = input()

while command != "STOP":
    taken_pieces = int(command)
    number_of_pieces -= taken_pieces

    if number_of_pieces < 0:
        pieces_are_over = True
        break

    command = input()

if pieces_are_over:
    print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")

else:
    print(f"{number_of_pieces} pieces are left.")
