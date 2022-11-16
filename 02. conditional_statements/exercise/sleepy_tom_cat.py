days_off = int(input())

minutes_of_play_time_for_year = 30000
year_days = 365

working_days_play_minutes = (year_days - days_off) * 63
days_off_play_minutes = days_off * 127
total_play_minutes = working_days_play_minutes + days_off_play_minutes

difference = abs(minutes_of_play_time_for_year - total_play_minutes)

hours = int(difference / 60)
minutes = int(difference % 60)

if total_play_minutes > minutes_of_play_time_for_year:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
