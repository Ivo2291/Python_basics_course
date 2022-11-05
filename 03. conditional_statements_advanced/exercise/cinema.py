screening_type = input()
rows = int(input())
columns = int(input())
cinema_capacity = rows * columns

premiere_ticket = 12
normal_ticket = 7.50
discount_ticket = 5
income = 0

if screening_type == "Premiere":
    income = cinema_capacity * premiere_ticket

elif screening_type == "Normal":
    income = cinema_capacity * normal_ticket

elif screening_type == "Discount":
    income = cinema_capacity * discount_ticket

print(f"{income:.2f} leva")
