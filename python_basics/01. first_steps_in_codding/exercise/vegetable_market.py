vegetables_kilo_price = float(input())
fruits_kilo_price = float(input())
vegetables_kilos = int(input())
fruits_kilos = int(input())

vegetables_price = vegetables_kilo_price * vegetables_kilos
fruits_price = fruits_kilo_price * fruits_kilos

total_price_lv = vegetables_price + fruits_price
total_price_eu = total_price_lv / 1.94
print(f"{total_price_eu:.2f}")
