game_moves = int(input())

result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for move in range(game_moves):
    number = int(input())

    if 0 <= number <= 50:

        if number <= 9:
            result += number * 0.2
            from_0_to_9 += 1
        elif number < 20:
            result += number * 0.3
            from_10_to_19 += 1
        elif number < 30:
            result += number * 0.4
            from_20_to_29 += 1
        elif number < 40:
            result += 50
            from_30_to_39 += 1
        elif number <= 50:
            result += 100
            from_40_to_50 += 1

    else:
        result /= 2
        invalid_numbers += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {from_0_to_9 / game_moves * 100:.2f}%")
print(f"From 10 to 19: {from_10_to_19 / game_moves * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / game_moves * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / game_moves * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / game_moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / game_moves * 100:.2f}%")
