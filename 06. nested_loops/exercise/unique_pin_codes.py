first_number = int(input())
second_number = int(input())
third_number = int(input())

for first_num in range(2, first_number + 1, 2):
    for second_num in range(2, second_number + 1):
        for third_num in range(2, third_number + 1, 2):
            if second_num == 2 or second_num == 3 or second_num == 5 or second_num == 7:
                print(f"{first_num} {second_num} {third_num}")
