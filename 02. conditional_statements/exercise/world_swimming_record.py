record_in_sec = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

distance_to_swim = distance_in_meters * time_per_meter
delay = distance_in_meters // 15
added_time = delay * 12.5
total_time = distance_to_swim + added_time

if record_in_sec <= total_time:
    print(f"No, he failed! He was {abs(record_in_sec - total_time):.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
