import math

length_in_meters = float(input())
width_in_meters = float(input())

length_in_centimeters = length_in_meters * 100
width_in_centimeters = width_in_meters * 100

offices_in_row = math.floor((width_in_centimeters - 100) / 70)
rows = math.floor(length_in_centimeters / 120)
seats_count = offices_in_row * rows - 3

print(seats_count)
