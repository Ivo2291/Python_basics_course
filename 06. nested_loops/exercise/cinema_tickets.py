student_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0
total_tickets_count = 0

command = input()

while command != "Finish":
    movie_name = command
    free_places = int(input())
    total_places = free_places
    sold_tickets = 0

    while free_places > 0:
        ticket_type = input()

        if ticket_type == "End":
            break

        elif ticket_type == "student":
            student_tickets_count += 1

        elif ticket_type == "standard":
            standard_tickets_count += 1

        elif ticket_type == "kid":
            kid_tickets_count += 1

        free_places -= 1
        total_tickets_count += 1
        sold_tickets += 1

    print(f"{movie_name} - {sold_tickets / total_places * 100:.2f}% full.")

    command = input()

print(f"Total tickets: {total_tickets_count}")
print(f"{student_tickets_count / total_tickets_count * 100:.2f}% student tickets.")
print(f"{standard_tickets_count / total_tickets_count * 100:.2f}% standard tickets.")
print(f"{kid_tickets_count / total_tickets_count * 100:.2f}% kids tickets.")
