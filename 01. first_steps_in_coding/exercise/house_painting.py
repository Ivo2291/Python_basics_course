height_of_the_house = float(input())
length_of_the_side_wall = float(input())
height_of_the_roof_wall = float(input())

side_area = height_of_the_house * length_of_the_side_wall
window_area = 1.5 * 1.5

total_sides_area = (side_area * 2) - (window_area * 2)

back_wall_area = height_of_the_house * height_of_the_house
door_area = 1.2 * 2

front_and_back_walls = (back_wall_area * 2) - door_area

total_wall_area = total_sides_area + front_and_back_walls
green_paint_needed = total_wall_area / 3.4

roof_front_side = (height_of_the_house * height_of_the_roof_wall) / 2
roof_left_side = height_of_the_house * length_of_the_side_wall

total_roof_area = (2 * roof_left_side) + (2 * roof_front_side)
red_paint_needed = total_roof_area / 4.3

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")
