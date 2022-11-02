length_in_centimeters = int(input())
width_in_centimeters = int(input())
height_in_centimeters = int(input())
percent = float(input())

volume_of_the_aquarium = length_in_centimeters * width_in_centimeters * height_in_centimeters
volume_in_liters = volume_of_the_aquarium * 0.001
occupied_space = percent / 100
needed_liters = volume_in_liters * (1 - occupied_space)

print(needed_liters)
