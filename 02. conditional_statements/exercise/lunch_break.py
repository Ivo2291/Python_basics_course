from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
relax_time = break_duration * 1/4
free_time = break_duration - lunch_time - relax_time

if free_time >= episode_duration:
    print(f"You have enough time to watch {series_name} "
          f"and left with {ceil(free_time - episode_duration)} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name},"
          f" you need {ceil(episode_duration - free_time)} more minutes.")
