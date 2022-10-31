number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

total_time = number_of_pages / pages_per_hour
needed_hours_per_day = total_time / number_of_days

print(round(needed_hours_per_day))
