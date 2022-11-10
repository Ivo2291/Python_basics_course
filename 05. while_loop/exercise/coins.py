float_sum = float(input())
int_sum = int(float_sum * 100)

coins_counter = 0

coins_counter += int_sum // 200
int_sum %= 200

coins_counter += int_sum // 100
int_sum %= 100

coins_counter += int_sum // 50
int_sum %= 50

coins_counter += int_sum // 20
int_sum %= 20

coins_counter += int_sum // 10
int_sum %= 10

coins_counter += int_sum // 5
int_sum %= 5

coins_counter += int_sum // 2
int_sum %= 2

coins_counter += int_sum // 1
int_sum %= 1

print(coins_counter)
