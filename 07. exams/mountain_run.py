import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

delay = math.floor(distance_in_meters / 50) * 30

runer_time = distance_in_meters * time_in_seconds_per_meter
time_with_delay = runer_time + delay
difference = abs(record_in_seconds - time_with_delay)

if record_in_seconds > time_with_delay:
    print(f"Yes! The new record is {time_with_delay:.2f} seconds.")

else:
    print(f"No! He was {difference:.2f} seconds slower.")
