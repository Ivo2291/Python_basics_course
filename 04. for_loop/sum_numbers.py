count_of_numbers = int(input())
sum_of_all_numbers = 0

for number in range(1, count_of_numbers + 1):
    current_number = int(input())

    if number <= current_number:
        sum_of_all_numbers += current_number
    else:
        sum_of_all_numbers += current_number

print(sum_of_all_numbers)
