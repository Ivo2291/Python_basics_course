hour_of_the_day = int(input())
day_of_the_week = input()

if day_of_the_week == "Sunday" or hour_of_the_day < 10 or hour_of_the_day > 18:
    print("closed")

else:
    print("open")
